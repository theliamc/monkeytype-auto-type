# Auto-typer for Monkeytype
# DISCLAIMER: STILL A WORK IN PROGRESS, NOT FUNCTIONAL YET, IF READING THIS WAIT ~24 HOURS AND CHECK BACK!

### Requirements:

- [Python](https://www.python.org/downloads/release/python-3121/) (Use 3.12 if possible, version 3.12 will be the most tested)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) (Download most recent version for your system)
    *know that there is a chance of Geckodriver being auto-installed on launch but Selenium is inconsentent, to be safe, install it manually*
- Extras in requirements.txt (installation instructions in setup section)

### Setup:

1. Download / clone and extract this repository
2. Open cmd in repo folder and run the following code:
```py
pip install -r requirements.txt
```

3. Run the main file based on your python version using code below

Python 3.4+:
```py
py main.py
```
Python 3.x:
```py
python3 main.py
```
Python 2:
```py
python main.py
```

### Notes:

- This opens a local server on port 5000, not changable at the moment
- May require firefox's geckodriver in requirements section
- Completely open source or whatever, make as much money or change as you want
