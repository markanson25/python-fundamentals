'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet:

    '''Defines name, position in solar system relative to the sun, and whether planet is gaseous or terrestrial'''
    def __init__(self, name, position, composition):
        self.name = name
        self.position = position
        self.composition = composition

    '''Provdies name, position, and composition output to user'''
    def __str__(self):
        return f"{self.name} is {self.position} in the solar system from the Sun, and is a {self.composition} planet."

my_planet = Planet('Mercury', 1, 'Terrestrial')
print(f"{my_planet.__str__()}")

