import logging
import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pytest import fixture

import settings
from helpers.web_service import WebService
from page_objects.application import App
from settings import *

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('BASE_URL')


@fixture(scope='session')
def get_webservice():
    web = WebService(BASE_URL)
    web.login(LOGIN, PASSWORD)
    yield web
    web.close()


@fixture(autouse=True, scope='session')
def setup_preconditions():
    logging.info("----------Set init state one time before running all tests (scope=session)")


@fixture(autouse=True, scope='session')
def teardown_preconditions():
    yield
    logging.info("--------- Reset state one time after running all tests (scope=session)")


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session', params=['chromium', 'firefox', 'webkit'], ids=['chromium', 'firefox', 'webkit'])
def get_browser(get_playwright, request):
    browser_type = request.param
    if browser_type == 'chromium':
        browser = get_playwright.chromium.launch(headless=settings.HEADLESS)
    elif browser_type == 'firefox':
        browser = get_playwright.firefox.launch(headless=settings.HEADLESS)
    elif browser_type == 'webkit':
        browser = get_playwright.webkit.launch(headless=settings.HEADLESS)
    else:
        assert False, "Unsupported browser type, configure valid browser in settings.py file"
    yield browser
    browser.close()


@fixture(scope='session')
def desktop_app(get_browser, request):
    app = App(get_browser, base_url=BASE_URL, **BROWSER_OPTIONS)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def desktop_app_auth(desktop_app):
    desktop_app.goto('/')
    desktop_app.login(LOGIN, PASSWORD)
    yield desktop_app


@fixture(scope='session', params=['iPhone 11', 'Pixel 2'], ids=['iPhone 11', 'Pixel 2'])
def mobile_app(get_playwright, get_browser, request):
    # device = request.param
    browser_name = get_browser.browser_type.name
    if browser_name == 'firefox':
        pytest.skip(reason="Playwright mobile  is not supported on firefox browser, skipping")
    device_config = get_playwright.devices.get(request.param)
    if device_config is not None:
        device_config.update(settings.BROWSER_OPTIONS)
    else:
        device_config = BROWSER_OPTIONS
    app = App(get_browser, base_url=BASE_URL, **device_config)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def mobile_app_auth(mobile_app):
    mobile_app.goto('/')
    mobile_app.login(LOGIN, PASSWORD)
    yield mobile_app
