
# Define a class decorator that adds a greet() method
def add_greeting(cls):
    # Define a new method greet to be added to the class
    def greet(self):
        return "Hello from Decorator!"
    
    # Attach the greet method to the class
    cls.greet = greet

    # Return the modified class
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"My name is {self.name}")

# Example usage:

# Create an object of Person
p = Person("Melvin")

# Call the original method
p.say_name()

# Call the method added by the decorator
print(p.greet())
