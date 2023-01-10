from pytest import mark

data = [("This is test name 1", "This is description for test 1"),
        ("This is test name 1", ""),
        ("12345", "This is description for test 1")
        ]

ddt = {'argnames': 'name,description',
       'argvalues': [("This is test name 1", "This is description for test 1"),
                     ("This is test name 1", ""),
                     ("12345", "This is description for test 1")],
       'ids': ['general test', 'test with no description', 'test with digits']}


@mark.parametrize(**ddt)
def test_new_testcase(desktop_app_auth, name, description, get_db):
    test_cases_list_initial = get_db.list_testcases()
    desktop_app_auth.navigate_to_menu('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to_menu("Test Cases")
    assert desktop_app_auth.test_cases.check_test_exists(name)
    assert len(test_cases_list_initial) + 1 == len(get_db.list_testcases())


def test_delete_testcase(desktop_app_auth, get_webservice):
    test_name = "test for delete"
    test_description = "Dont forget to delete me"
    get_webservice.create_test(test_name, test_description)
    desktop_app_auth.navigate_to_menu('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exists(test_name)
    desktop_app_auth.test_cases.delete_test_by_name(test_name)
    assert not desktop_app_auth.test_cases.check_test_exists(test_name)
