import pytest

@pytest.mark.smoke
def test_addition():
    a = 8
    b = 8
    assert  a + b == 13

@pytest.mark.skip
def test_skipped():
    assert False

@pytest.mark.xfail
def test_xfail_example():
    print("This is an xpass example")
    assert 5 == 4