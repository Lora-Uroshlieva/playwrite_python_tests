def test_new_testcase(desktop_app_auth):
    test_name = "This is test name 1"
    test_description = "This is description for test 1"
    desktop_app_auth.create_test(test_name, test_description)
    desktop_app_auth.navigate_to_menu("Test Cases")
    desktop_app_auth.test_cases.check_test_exists(test_name)
    desktop_app_auth.test_cases.delete_test_by_name(test_name)


def test_new_testcase_no_description(desktop_app_auth):
    test_name = "This is test name 1"
    desktop_app_auth.create_test(test_name, '')
    desktop_app_auth.navigate_to_menu("Test Cases")
    desktop_app_auth.test_cases.check_test_exists(test_name)
    desktop_app_auth.test_cases.delete_test_by_name(test_name)


def test_new_testcase_digits_in_name(desktop_app_auth):
    test_name = "12345"
    test_description = "This is description for test 1"
    desktop_app_auth.create_test(test_name, test_description)
    desktop_app_auth.navigate_to_menu("Test Cases")
    desktop_app_auth.test_cases.check_test_exists(test_name)
    desktop_app_auth.test_cases.delete_test_by_name(test_name)
