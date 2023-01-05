from pytest import mark

#data provider

@mark.parametrize("num, result", [(1,11),(2,22),(3,34),(4,44)])
def test_multiplication(num, result):
    assert num*11 == result

@mark.parametrize("num1, num2, result",{(1,2,3),(4,5,9),(2,3,4)})
def test_addition(num1, num2, result):
    assert num1+num2 == result