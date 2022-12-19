def test_new_testcase(desktop_app):
    desktop_app.login()
    desktop_app.create_test()
    desktop_app.open_tests()
    desktop_app.check_tests_created()
    desktop_app.delete_test()
