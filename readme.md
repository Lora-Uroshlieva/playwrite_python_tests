# Project to learn and demonstrate web testing using pytest + playwright

## Install guide

Test app can be installed locally and run on http://127.0.0.1:8000. There is sqlite3 database with preinstalled test
data and test user.
#### To set up  application to test: 
  - copy the test project from github https://github.com/Ypurek/TestMe-TCM
  - unzip the project
  - run pip install -r requirements.txt
  - run python ./manage.py runserver
The app will be up. To check the credentials for test db - watch Qamania channel 
  - on youtube https://www.youtube.com/playlist?list=PLGE9K4YL_ywj4F7cSA4oDptnqTmyS7hZp

Install the test project:
$ pip install -r requirements.txt
$ python -m playwright install ##to install browsers

To add user credentials - add .env file into root of the project with next params defined: LOGIN, PASSWORD, BASE_URL.

## Useful links

https://playwright.dev/python/docs/intro
https://github.com/Microsoft/playwright-python
