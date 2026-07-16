import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_Greet():

    print("HI, Good morning")
    a = 1
    b = 5
    assert 4 + a == b

def test_Greet2():
    print("Thank you")
    a = 1
    b = 10
    assert a + 9 == b
