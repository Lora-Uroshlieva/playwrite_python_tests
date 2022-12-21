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
def test_new_testcase(desktop_app_auth, name, description):
    desktop_app_auth.navigate_to_menu('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to_menu("Test Cases")
    desktop_app_auth.test_cases.check_test_exists(name)
    desktop_app_auth.test_cases.delete_test_by_name(name)
