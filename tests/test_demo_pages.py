import allure


@allure.title("Test for wait more than 30 seconds")
def test_wait_more_30s(desktop_app_auth):
    desktop_app_auth.navigate_to_menu('Demo pages')
    desktop_app_auth.demo_pages.open_page_after_wait(3)
    assert desktop_app_auth.demo_pages.check_wait_page()


def test_ajax(desktop_app_auth):
    desktop_app_auth.navigate_to_menu('Demo pages')
    desktop_app_auth.demo_pages.open_page_and_wait_ajax(3)
    assert 3 == desktop_app_auth.demo_pages.get_ajax_responses_count()


def test_testcase_does_not_exist(desktop_app_auth):
    desktop_app_auth.navigate_to_menu('Demo pages')
    assert not desktop_app_auth.test_cases.check_test_exists('this test definitely does not exist')
    assert False, "This is intentionally failed"


def test_handlers(desktop_app_auth):
    desktop_app_auth.navigate_to_menu('Demo pages')
    desktop_app_auth.demo_pages.click_new_page_button()
    desktop_app_auth.demo_pages.inject_js()
    desktop_app_auth.navigate_to_menu('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exists("Successfull registration check")
