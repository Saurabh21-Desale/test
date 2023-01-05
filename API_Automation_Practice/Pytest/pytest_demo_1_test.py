
# pytest file name should be start or end with 'test' keyword
# pytest method name should be start with 'test' keyword

# to run pytest file use py.test it will run all test methods from project
# to run all methods file name should start or end with 'test' keyword

# to run specific test use py.test -k login(specific keyword from test method) -v
# -k= it will use to run specific test
# -v= It gives more varbles(gives more information about test on console)

# @pytest.mark.skipif= use to skip conditionally

# to run by group use pytest -m groupname -v

# If we wnat to run single test case from file then use = py.test Package name/file name::method name -v

#pytest -v -k "special word from method name"
#pytest -v -k "special name from method name or another name" run those test case which contains either of name
#pytest -v -k "special name from method name or another name" only run those test cases which contains both the names

import pytest

@pytest.mark.skip  # skip the test case
def test_1():
    a=3
    b=4
    assert a+1==b

@pytest.mark.group2  # group2= it is group name
def test_2():
    assert True

@pytest.mark.xfail  # xfail= it will execute but will not consider as a passed or failed
def test_3():
    assert False

@pytest.mark.group2
def test_4():
    var="arrk"
    assert var.upper()=="ARRK"


def test_login_1():
    assert 100==90