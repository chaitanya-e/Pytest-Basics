import pytest

@pytest.fixture     # similar to brefore test and after test in testng
def setup():
    print("Fixture setup() that runs before Test Execution")

def test_fixture():
    print("test_fixture() without passing fixture method name as argument")

def test_fixtures(setup):
    print("test_fixtures(setup) a valid fixture which has fixture method name as argument")

def setupAndTeardown():     
    print("Before test execution code")
    yield       # anything after YIELD will be executed after test execution completes
    print("After Test execution code")

@pytest.fixture
def setupAndTeardown2():     
    print("Before test execution code")
    yield       # anything after YIELD will be executed after test execution completes
    print("After Test execution code")

def test_fixture2(setupAndTeardown):    # fixture 'setupAndTeardown' not found
    print("Fixture with setup and Teardown")

def test_fixture3(setupAndTeardown2):
    print("Fixture with setup and Teardown")

def test_global_fixture(globalfixture):
    print("Test method that uses global fixture")

@pytest.mark.dataprovider
def test_fixture_as_data_provider(fixture_as_data_provider):
    print(fixture_as_data_provider)