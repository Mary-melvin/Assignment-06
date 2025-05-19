
# Define the Multiplier class
class Multiplier:
    # __init__() sets the multiplier factor when the object is created
    def __init__(self, factor):
        self.factor = factor  # Store the factor for later use

    # __call__() allows the object to be called like a function
    def __call__(self, number):
        return number * self.factor  # Multiply input by the stored factor

# Example usage:

# Create a Multiplier object with a factor of 3
triple = Multiplier(3)

# Use callable() to check if the object is callable
print("Is 'triple' callable?", callable(triple))  # Output: True

# Call the object like a function
result = triple(10)  # Equivalent to triple.__call__(10)

# Print the result of the multiplication
print("Result of triple(10):", result)  # Output: 30
