import pytest

@pytest.mark.usefixtures("globalfixture")
class Test_fixtures3:
    def test_fixture_in_class(self):
        print("Test method 1")
    
    def test_fixture_in_class2(self):
        print("Test method 2")

    def test_fixture_in_class3(self):
        print("Test method 3")

@pytest.mark.usefixtures("classfixture")
class Test_Fixtures4:
    def test_fixture_at_class_level(self):
        print("Fixture at class level - method 1")

    def test_fixture_at_class_level2(self):
        print("Fixture at class level - method 2")


@pytest.mark.usefixtures("fixture_returning_data")
class Test_Fixture_returning_data:
    def test_fixture_returning_data(self, fixture_returning_data):
        print("test1")
        print(fixture_returning_data)

    def test_fixture_returning_data2(self, fixture_returning_data):
        print("test2 "+fixture_returning_data[2])