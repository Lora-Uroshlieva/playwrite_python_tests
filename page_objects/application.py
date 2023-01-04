from playwright.sync_api import Browser

from .test_cases import TestCases


class App:
    def __init__(self, browser: Browser, base_url: str, **kwargs):
        self.browser = browser
        self.context = self.browser.new_context(**kwargs)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.test_cases = TestCases(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def navigate_to_menu(self, menu: str):
        self.page.locator(f"text={menu}").click()
        self.page.wait_for_load_state()

    def login(self, login: str, password: str):
        self.page.locator("input[name=\"username\"]").fill(login)
        self.page.locator("input[name=\"password\"]").fill(password)
        self.page.locator("text=Login").click()

    def create_test(self, test_name: str, test_description: str):
        self.page.locator("text=Create new test").click()
        self.page.locator("input[name=\"name\"]").fill(test_name)
        self.page.locator("textarea[name=\"description\"]").fill(test_description)
        self.page.locator("input:has-text(\"Create\")").click()

    def click_menu_button(self):
        self.page.locator(".menuBtn").click()

    def is_menu_button_visible(self):
        return self.page.locator(".menuBtn").is_visible()

    def get_location(self):
        return self.page.locator('.position').text_content()

    def close(self):
        self.page.close()
        self.context.close()
