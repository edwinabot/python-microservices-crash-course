# pylint: disable=unused-variable

"""
This is the docstring for this module
"""

from datetime import date


def show_me_some_syntax():
    """
    The first comment is the docstring for this function
    """

    # This is a one line comment

    '''
    This is
    a multiline comment
    '''

    an_int = 10
    a_float = 25.32
    a_string = "Jane Doe"
    an_interpolated_string = f"The name is: {a_string}"
    a_date = date(1990, 10, 25)
    an_object = object()
    a_list = [1, 5, 25, -58]    # We can access an item by its index: a_list[2]
    a_tuple = (1, 5, 25, -58)   # the same can be done with a tuple: a_tuple[2]
    a_dictionary = {'name': a_string, 'birthday': a_date, 'number_of_freckles': an_int}
                                # A dict's item by it's key value: a_dictionary['name']

    # Lets iterate over a list with a for loop
    print('\n=== Looping a list [] with a for loop ===')
    for item in a_list:
        print(f"The list item: {item}")

    # Lets iterate some over a tuple with a while loop
    # We could have used a for loop too
    print('\n=== Looping a tuple () with a while loop ===')
    counter = 0
    while counter < len(a_tuple):
        the_value = a_tuple[counter]
        print(f"The tuple item: {the_value}")
        counter += 1

    # Now lets iterate over a dict
    print('\n=== Looping a dict {} with a for loop ===')
    for key, value in a_dictionary.items():
        clean_key = key.replace('_', ' ')  # Let's replace underscores for spaces
        print(f"The {clean_key} is {value}")
