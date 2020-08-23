from .context import gf

def test_is_number_divisible_by_divisor():
    assert gf.helpers.is_number_divisible_by_divisor(15, 3) == True
    
def test_is_number_divisible_by_divisors():
    assert gf.helpers.is_number_divisible_by_divisors(15, [3, 5]) == True