
# Import the ABC and abstractmethod from abc module
from abc import ABC, abstractmethod

# Define an abstract base class named Shape
class Shape(ABC):
    # Declare an abstract method 'area' (no implementation here)
    @abstractmethod
    def area(self):
        pass  # This method must be implemented in any subclass

# Define a subclass named Rectangle that inherits from Shape
class Rectangle(Shape):
    # Constructor to initialize width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the abstract method 'area'
    def area(self):
        return self.width * self.height

# Example usage:

# Create an instance of the Rectangle class
rect = Rectangle(10, 5)

# Call the implemented area() method
print("Area of rectangle:", rect.area())
