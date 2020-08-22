from . import helpers

formats_dict = {
    'gest': {
        'divisors': [3],
        'str': 'Geste',
    },
    'form': {
        'divisors': [5],
        'str': 'Forme',
    },
    'gestform': {
        'divisors': [3, 5],
        'str': 'Gestform',
    },
}

# Returns passed number or a string according to the value divisibily.
def number_to_gestform_format(number):
    return None