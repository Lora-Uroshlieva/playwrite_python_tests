from playwright.sync_api import Playwright

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


class App:
    def __init__(self, playwright: Playwright):
        # self.playwright = playwright
        self.browser = playwright.chromium.launch(headless=False, devtools=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def login(self):
        self.page.goto("http://127.0.0.1:8000/login/?next=/")
        self.page.locator("input[name=\"username\"]").fill("alice")
        self.page.locator("input[name=\"password\"]").fill("Qamania123")
        self.page.locator("text=Login").click()

    def create_test(self):
        self.page.locator("text=Create new test").click()
        self.page.locator("input[name=\"name\"]").fill("test111")
        self.page.locator("textarea[name=\"description\"]").fill("description111")
        self.page.locator("input:has-text(\"Create\")").click()

    def open_tests(self):
        self.page.locator("text=Test Cases").click()
        self.page.wait_for_url("http://127.0.0.1:8000/tests/")

    def check_tests_created(self):
        assert self.page.query_selector('//td[text()="test111"]') is not None

    def delete_test(self):
        self.page.locator("text=test111 description111 alice Norun None PASS FAIL Details Delete >> button").nth(
            3).click()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
