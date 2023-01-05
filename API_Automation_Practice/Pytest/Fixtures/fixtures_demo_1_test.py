
import pytest


# def setup_module(module):   #pass module as a argument
#     print("launch browser")
#
# def test_add():
#     print("abcdefgh")
# def test_remove():
#     print("123456789")

# def setup_module(module):
#     print("launch browser")
#
# def teardown_module(module):
#     print("close browser")
#
# def test_add():
#     print("abcdefgh")
#
# def test_remove():
#     print("123456789")


@pytest.yield_fixture() #scope=module
def setup():
    print("Launching the Browser")
    yield #after testcases
    print("Closing the Browser")

def test_add(setup):
    print("abcdefgh")
def test_remove(setup):
    print("123456789")

