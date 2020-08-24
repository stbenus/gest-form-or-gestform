from . import helpers

# Returns the translations rules.
def get_business_formats():
    return [
        {
            'divisors': [3],
            'str': 'Geste',
        }, {
            'divisors': [5],
            'str': 'Forme',
        }, {
            'divisors': [3, 5],
            'str': 'Gestform',
        }
    ]

# Returns passed number or a string according to the value divisibily.
def translate_number(number):
    # Division by 0 must returns 0
    if number == 0:
        return 0
    
    # To process cases of multiple divisors first.
    ordered_formats = sorted(
        get_business_formats(),
        key = lambda i: len(i['divisors']),
        reverse = True
    )

    # Returns the str of the first possible case of division.
    for business_format in ordered_formats:
        if helpers.is_number_divisible_by_divisors(
                number, business_format['divisors']):
            return business_format['str']

    return number