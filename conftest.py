import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pytest import fixture

from page_objects.application import App

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('BASE_URL')


@fixture(autouse=True, scope='session')
def setup_preconditions():
    print("Set init state one time before running all tests (scope=session)")


@fixture(autouse=True, scope='session')
def teardown_preconditions():
    yield
    print("\n --------- Reset state one time after running all tests (scope=session)")


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def desktop_app(get_playwright):
    app = App(get_playwright, base_url=BASE_URL)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def desktop_app_auth(desktop_app):
    desktop_app.goto('/')
    desktop_app.login(LOGIN, PASSWORD)
    yield desktop_app
