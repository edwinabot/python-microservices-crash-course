# pylint: disable=unused-variable, C0103
"""
This module contains a brief showcase of Python
"""
from showcase import show_me_some_syntax, CyborgDog, Dog


if __name__ == '__main__':

    print('Hey Sparker! welcome to Python.')
    print('Now we will call the show_me_some_syntax function.')
    print('Checkout the code on showcase.py or use the debugger.')

    show_me_some_syntax()

    # Create a list of dog names
    dog_names = ['Fido', 'Bobi', 'Tito', 'Toto', 'Scooby']

    # Iterate the list and create some CyborgDogs
    for name in dog_names:
        cyborg_dog = CyborgDog(name)
        cyborg_dog.do_behaviour()
        cyborg_dog.bark()

    # Check how many dogs do we have
    number_of_dogs = len(Dog.get_all_known_dogs())
    print(f"There are {number_of_dogs} dogs")

    # Now a cataclysm happens
    CyborgDog.survive_a_cataclysm()

    # Tell me how many dogs do we have now
    print(f"Now there are {len(Dog.get_all_known_dogs())} dogs")
