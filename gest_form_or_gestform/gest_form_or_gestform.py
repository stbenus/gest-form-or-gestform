from . import helpers

business_formats = [
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
def number_to_gestform_format(number):
    ordered_formats = sorted(
        business_formats,
        key = lambda i: len(i['divisors']),
        reverse = True
    )

    for business_format in ordered_formats:
        if helpers.is_number_divisible_by_divisors(
                number, business_format['divisors']):
            return business_format['str']

    return number