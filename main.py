import random

max_number_value = 1000
min_number_value = -1000
numbers_to_generate = 100
gest_str = 'Geste'
form_str = 'Forme'
gestform_str = 'Gestform'

def number_to_string(number):
    if number % 5 == 0 and number % 3 == 0:
        return gestform_str
    if number % 3 == 0:
        return gest_str
    if number % 5 == 0:
        return form_str
    return number

def test_number_to_string():
    numbers_dictionary = {
        3: gest_str,
        5: form_str,
        15: gestform_str,
        1: 1,
    }

    for number in numbers_dictionary:
        if number_to_string(number) != numbers_dictionary[number]:
            return False
    
    return True

def print_numbers(numbers):
    for number in numbers:
        print(number_to_string(number))

def test_app(tests):
    tests_dictionary = dict.fromkeys(tests, False)

    for test in tests_dictionary:
        tests_dictionary[test] = test()

    if list(tests_dictionary.values()).count(False) == 0:
        return True
    
    return False

def main():
    tests = [
        test_number_to_string,
    ]

    numbers = []

    if test_app(tests) == False:
        print('Ooops! The App seems to not work properly.')
        return

    for i in range(numbers_to_generate):
        numbers.append(random.randint(min_number_value, max_number_value))

    print_numbers(numbers)

main()