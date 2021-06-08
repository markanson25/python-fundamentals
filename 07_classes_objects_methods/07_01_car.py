'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    """This is a car along with year, model, and speed."""
    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = year
        self.speed = speed

    '''This adds 5 kph to the speed each time it is called'''
    def __accelerate__(self, speed):
        self.speed = speed
        self.speed += 5
        return self.speed

    '''This subtracts 5 kph to the speed each time it is called'''
    def __brake__(self, speed):
        self.speed = speed
        if self.speed == 0:
            self.speed = 0
        else:
            self.speed -= 5
        return self.speed

    '''This prints the horn sound when it is called'''
    def __str__(self):
        return f"{self.model} goes 'beep beep'"

new_car = Car('Ford', 2007, 10)
print(f"{new_car.model}, {new_car.year}, {new_car.speed}, {new_car.__accelerate__(new_car.speed)}, {new_car.__brake__(new_car.speed)}, {new_car.__str__()}")

