from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, devtools=True)
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://127.0.0.1:8000/login/?next=/")
    page.locator("input[name=\"username\"]").fill("alice")
    page.locator("input[name=\"password\"]").fill("Qamania123")
    page.locator("input[name=\"password\"]").press("Enter")
    page.wait_for_url("http://127.0.0.1:8000/")

    page.locator("text=Create new test").click()
    page.wait_for_url("http://127.0.0.1:8000/test/new")
    page.locator("input[name=\"name\"]").click()
    page.locator("input[name=\"name\"]").fill("Test 27-09")
    page.locator("input[name=\"name\"]").press("Tab")
    page.locator("textarea[name=\"description\"]").fill("test body 27-09")
    page.locator("input:has-text(\"Create\")").click()
    page.wait_for_url("http://127.0.0.1:8000/test/new")
    page.locator("text=Test Cases").click()
    page.wait_for_url("http://127.0.0.1:8000/tests/")

    assert page.locator('//td[text()="hello"]') is not None

    page.goto('http://127.0.0.1:8000/tests')

    page.locator("text=Test 27-09 test body 27-09 alice Norun None PASS FAIL Details Delete >> button").nth(
        3).click()
    # ---------------------
    page.close()
    context.close()
    browser.close()


def test_new_testcase():
    with sync_playwright() as playwright:
        run(playwright)
