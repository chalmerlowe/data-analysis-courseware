# * Create a class called `Car`
# * Define an `__init__()` method that takes two additional parameters (besides `self`) and assigns them to `self.color` and `self.mpg` (miles per gallon) attributes respectively
# * Define a method called `change_color` that takes in two arguments (`self` and `color`) and assigns that to `self.color`
# * Define a method called `print_specs` that prints the values associated with `color` and `mpg`
# * Create an object called `sportscar`, based on your `Car` class, and pass in two arguments: a `string` for the color and an `integer` for the miles per gallon.

class Car:
    def __init__(self, color, mpg):
        self.color = color
        self.mpg = mpg
        
    def change_color(self, color):
        self.color = color
    
    def print_specs(self):
        print('Your car is {} and has a mpg of: {}'.format(self.color, self.mpg))

sportscar = Car('red', 42)        
        
