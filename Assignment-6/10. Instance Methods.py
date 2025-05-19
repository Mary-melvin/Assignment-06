
# Define a class named Dog
class Dog:
    # Constructor to initialize instance variables
    def __init__(self, name, breed):
        # 'self.name' and 'self.breed' are instance variables
        self.name = name
        self.breed = breed

    # Instance method that makes the dog bark
    def bark(self):
        # Print a message that includes the dog's name
        print(f"{self.name} says: Woof!")

# Example usage:

# Create an object of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Call the bark() method
dog1.bark()
