import pytest

@pytest.fixture()
def launch():
    print("Launching the Browser")
    yield #after testcases
    print("Closing the Browser")