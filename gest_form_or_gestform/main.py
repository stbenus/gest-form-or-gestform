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

def main():
    try:
        randoms_to_generate = int(sys.argv[1])
    except IndexError:
        print('You need to pass in a number of randoms to generate.')
        print(help)
        sys.exit()
    try:
        min_value = int(sys.argv[2])
    except IndexError:
        min_value = -1000
    try:
        max_value = int(sys.argv[3])
    except IndexError:
        max_value = 1000

    print(f'Generating and translating {randoms_to_generate} random numbers.')

    for i in range(randoms_to_generate):
        print(gf.translate_number(random.randint(min_value, max_value)))
    
    print('Finished')
    