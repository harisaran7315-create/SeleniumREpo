import pytest

@pytest.mark.smoke
@pytest.mark.usefixtures("profile_normal")
@pytest.mark.usefixtures("profile2")
@pytest.mark.usefixtures("params_exercise")
class Test_exercise:

    def test_exercise1(self, profile):
        print(profile[0])

    def test_exercise2(self, profile2, profile):
        print(self)
        print(profile2[2])
        print(profile[1])

    def test_exercise(self, params_exercise):
        print(params_exercise[1])

