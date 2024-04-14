import pyautogui as pyag
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from flask import Flask, request

app = Flask(__name__)
os.environ['FLASK_ENV'] = 'production'

if sys.version_info[0] < 3:
    raise Exception("NOTE: YOU ARE USING PYTHON VERSION 2, RECOMMENDED THAT YOU UPGRADE TO VERSION 3.")

# initialize | get on the website & accept cookies
driver = webdriver.Firefox()
driver.get("https://monkeytype.com/")
driver.find_element(By.XPATH, "/html/body/div[8]/dialog/div[2]/div[2]/div[2]/button[1]").click()

def setupTest():

    # put textbox on screen
    # put start button on screen
    driver.execute_script("""
        var delayTextbox = document.createElement("input");
        delayTextbox.setAttribute("type", "text");
        delayTextbox.setAttribute("id", "myInput");
        delayTextbox.setAttribute("placeholder", "Keypress delay (seconds)");

        var startButton = document.createElement("button");
        startButton.setAttribute("type", "button");
        startButton.setAttribute("id", "startBotButton");
        startButton.textContent = "Start bot";

        var targetElement = document.querySelector(".page > div:nth-child(5)");
        targetElement.appendChild(delayTextbox);
        targetElement.appendChild(startButton);
    """)

    # put code for checking text
    # put code for when button is pressed -> trigger python
    # ajax/xhr bs made by chatgpt
    driver.execute_script("""
        document.getElementById("startBotButton").addEventListener("click", function() {
            var inputValue = document.getElementById("myInput").value;
                          
            if (!inputValue) {
                inputValue = 0;
            }

            // Use AJAX to send the value to a server-side Python script
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "http://localhost:5000/python_script?inputValue=" + encodeURIComponent(inputValue), true);
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    console.log(xhr.responseText);
                }
            };
            xhr.send();
        });
    """)

# dedicated function for listening to api calls
@app.route('/python_script')
def python_script():
    inputValue = request.args.get('inputValue')
    botScript(inputValue)
    return "win"

def botScript(delay):
    print("Delay set: " + delay)

    while True:

        try: # find & type the active word
            
            activeLetters = driver.find_elements(By.CSS_SELECTOR, "div.word.active > letter")
           
            wordDone = ""
            
            driver.find_element(By.ID, "typingTest").click()

            for letter in activeLetters:
                wordDone = wordDone + letter.text
                
            wordDone = wordDone + " "
            textInput = driver.find_element(By.CSS_SELECTOR, "#wordsInput")
            textInput.send_keys(wordDone)

            print(wordDone + " | done")
            wordDone = ""

        except: # if active word isn't found, test was restarted or finished

            print("no more words")
            break
        
        time.sleep(int(delay)) # delay


if __name__ == "__main__":
    setupTest()
    print("\n\nIf no errors occurred below, then you can minimize this window unless you're debugging\nIf no errors occurred below, then you can minimize this window unless you're debugging\nIf no errors occurred below, then you can minimize this window unless you're debugging\n\n")
    app.run(debug=False)