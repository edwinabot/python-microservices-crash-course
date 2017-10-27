# pylint: disable=unused-variable, C0111
"""
This is the docstring for this module
"""
import random
import uuid
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
        clean_key = key.replace('_', ' ')   # Let's replace underscores for spaces
        print(f"The {clean_key} is {value}")


class Dog:
    _all_known_dogs = []                    # When declared in the body of the class
                                            # the attributes are "Class attributes"

    def __init__(self, name, color):        # The init method is for initialization
        self._name = name                   # of new instances not to be confused
        self._color = color                 # with a constructor. The 'self' param
        self._all_known_dogs.append(self)   # has the reference to the instance

    def bark(self):                         # this is an instance method
        print('Bark bark!!...')             # the 'self' param contains the reference
                                            # to the instance

    @classmethod
    def survive_a_cataclysm(cls):      # this is a class method
        randint = random.randint(1, 100)    # the 'cls' param has a reference
        if randint < 65:                    # to the class. Ergo we use it to access
            cls._all_known_dogs.clear()     # class methods and attributes.
                                            # We can do Dog.survive_a_cataclysm()

    @property
    def color(self):                        # This is a getter property for color
        return self._color

    @color.setter                           # This is the setter for color
    def color(self, value):                 # we can add validations and
        self._color = value                 # some other logic related to access control

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @classmethod
    def get_all_known_dogs(cls):
        return cls._all_known_dogs

class Machine:

    def __init__(self, serial_number):
        self._serial_number = serial_number


class Robot(Machine):  # Robot inherits Machine

    def __init__(self, serial_number, behaviour):
        super().__init__(serial_number)
        self._behaviour = behaviour

    def do_behaviour(self):
        self._behaviour()


class CyborgDog(Dog, Robot):  # CyborgDog inherits from Dog and Robot

    def __init__(self, name, color='Silver'):
        Dog.__init__(self, name, color)
        Robot.__init__(self, str(uuid.uuid4()), CyborgDog.some_cyborg_behaviour)

    @staticmethod
    def some_cyborg_behaviour():
        print('Im a CyborgDog... I do CyborgDog stuff')

    def bark(self):
        super().bark()
        print(f"I'm {self.name}")
        print('\a')
