def is_number_divisible_by_divisor(dividend, divisor):
    if dividend % divisor == 0:
        return True
    
    return False

def is_number_divisible_by_divisors(dividend, divisors):
    is_divisible = True

    for divisor in divisors:
        if not is_number_divisible_by_divisor(dividend, divisor):
            is_divisible = False
    
    return is_divisible