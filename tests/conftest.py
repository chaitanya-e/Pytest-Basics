import pytest

# @pytest.fixture(scope="class")
@pytest.fixture
def globalfixture():
    print("global fixture - before test")
    yield
    print("global fixture - after test")

@pytest.fixture(scope="class")
def classfixture():
    print("executed for class - not for every test")
    yield
    print("fixture - after class")

@pytest.fixture
def fixture_returning_data():
    return ["pytest tutorial","vscode","python"]

@pytest.fixture(params=[('a','b','c'), (1,2), ('#')])
def fixture_as_data_provider(request):
    return request.param