import pytest


def test_assert():
    msg = "Hello"
    assert  msg == "Hi"

def test_assert():  #This overwrites earlier method as it has same name
    msg = "Hello"
    assert msg == "Hello"

def addition(): # No test is prefixed so it wont execute as test
    a = 4
    b = 6
    assert a+b == 7

@pytest.mark.smoke
def test_subtraction():
    a = 4
    b = 7
    assert b-a == 3

def test_paymentNotReceived():
    msg = "payment not received"
    assert  msg == "payment not received"