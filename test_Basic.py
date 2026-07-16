import pytest


def test_exercise():
    info = "hi pytest"
    assert info == 'hi pytest', 'Test failed because string didnt match'

@pytest.mark.smoke
def test_exercise2():
    info = "Hello pytest"
    assert info == 'Hello pytest', 'Test failed because string didnt match'
