import sys
import random

from . import gest_form_or_gestform as gf

help = '''
gest_form_or_gestform script

gest_form_or_gestform randoms_to_generate [min_value] [max_value]

Translates randomly generated numbers by "Geste", "Forme", or "Gestform",
according to their divisibility.
Returns the number value if no business defined divisibility found. 
'''

def print_value_error_message(invalid_value):
    print(f'Invalid value: {invalid_value}')

def main():
    randoms_to_generate = 1
    min_value = -1000
    max_value = 1000

    try:
        randoms_to_generate = abs(int(sys.argv[1]))
    except IndexError:
        pass
    except ValueError:
        print_value_error_message(sys.argv[1])
        sys.exit()

    try:
        min_value = int(sys.argv[2])
    except IndexError:
        pass
    except ValueError:
        print_value_error_message(sys.argv[2])
        sys.exit()
    
    try:
        max_value = int(sys.argv[3])
    except IndexError:
        pass
    except ValueError:
        print_value_error_message(sys.argv[3])
        sys.exit()

    if min_value > max_value:
        min_value, max_value = max_value, min_value

    print(f'Generating and translating {randoms_to_generate} random numbers.')

    i = 0
    while i < randoms_to_generate:
        try:
            print(gf.translate_number(random.randint(min_value, max_value)))
            i += 1
        except KeyboardInterrupt:
            print('Try with less randoms to generate next time :).')
            sys.exit()
    
    print('Finished')
    