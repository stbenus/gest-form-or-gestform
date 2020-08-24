# Return True or False according to the divisibility of the passed dividend by
# the passed divisor.
def is_number_divisible_by_divisor(dividend, divisor):
    if dividend % divisor == 0:
        return True
    
    return False

# Return True or False according to the divibility of the passed dividend by
# the passed divisors.
# Based on is_number_divisible_by_divisor() function.
def is_number_divisible_by_divisors(dividend, divisors):
    # Return False when an impossible case of division is encountered.
    for divisor in divisors:
        if not is_number_divisible_by_divisor(dividend, divisor):
            return False
    
    return True