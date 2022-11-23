def test_new():
    x = 5
    x+=1
    assert 1 == 1

def test2_new():
    assert 2==3


def test_3_failure():
    print("before   "*5)
    assert False, "This test failed intentionally"
    print("after  "*8)