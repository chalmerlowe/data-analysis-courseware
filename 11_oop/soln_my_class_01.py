# * Create a class called `Animal`
# * Define an `__init__()` method that takes in one argument: `self`
#   * In the `__init__()` method, create a label called `self.fur_color` and assign it to an empty string
# * Define two methods for your class:
#   * a method called `set_fur_color` that takes in two arguments (`self` and `color`) and assigns the value of color to `self.fur_color`
#   * a second method called `print_fur_color` that prints the value associated with `self.fur_color`
# * Now, create a new object based on your `Animal` class, called: `pet`
# * Call your `pet.set_fur_color()` method and provide a color argument
# * Call your `pet.print_fur_color()` method and ensure that it successfully prints the fur color


class Animal:
    def __init__(self):
        self.fur_color = ''
    
    def set_fur_color(self, color):
        self.fur_color = color
        
    def print_fur_color(self):
        print(self.fur_color)

pet = Animal()
pet.set_fur_color('blue')
pet.print_fur_color()