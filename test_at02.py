import pytest
from at02 import check

def test_check():
    assert check(4) == True

def test_check2():
    assert check(3) == False

@pytest.mark.parametrize('num,exp', [
    (2, True),
    (3, False),
    (4, True),
    (-4, False),
    ])
def test_check3(num, exp):
    assert check(num) == exp
