from .context import gf

# Tests the structure of the translation rules.
def test_get_business_formats():
    business_formats = gf.get_business_formats()
    divisors_dict_key = 'divisors'
    str_dict_key = 'str'

    # TODO Complexity: It may was possible to put all the tests in a minimum
    # number of for...

    # The function must returns a List.
    assert isinstance(business_formats, list)

    # All List elements must are Dictionaries.
    for business_format in business_formats:
        assert isinstance(business_format, dict)
    
    # All Dictionaries must contain a key that contains the Divisors.
    for business_format in business_formats:
        assert divisors_dict_key in business_format
    
    # Puts all values contained in Divisor keys in a list.
    divisors_list = [d[divisors_dict_key] for d in business_formats]
    
    # All Divisor keys must contain a list.
    for divisors in divisors_list:
        assert isinstance(divisors, list)

    # Puts all Divisors in a flatlist.
    divisors = [val for sublist in divisors_list for val in sublist]
    
    # All Divisors must are an integer.
    for divisor in divisors:
        assert isinstance(divisor, int)
    
    # All Dictionaries must contain a key that contains the Translation.
    for business_format in business_formats:
        assert str_dict_key in business_format
    
    # Puts all values contained in Translation keys in a list.
    strs = [d[str_dict_key] for d in business_formats]

    # All Translation keys must contain a string.
    for str_element in strs:
        assert isinstance(str_element, str)

def test_translate_number():
    for business_format in gf.get_business_formats():
        # TODO I no longer count the number of times I should have used
        # numpy... :)
        #numpy.prod(business_format)
        prod = 1
        for divisor in business_format['divisors']:
            prod = prod * divisor
        
        # A math trick ...
        assert gf.translate_number(prod) == business_format['str']
    
    # Division by 0 must returns 0.
    assert gf.translate_number(0) == 0