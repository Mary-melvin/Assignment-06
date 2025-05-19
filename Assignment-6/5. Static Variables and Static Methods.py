
# Define a class named MathUtils
class MathUtils:
    # Define a static method to add two numbers
    @staticmethod
    def add(a, b):
        # Simply return the sum of a and b
        return a + b

# Example usage:

# Call the static method directly using the class name (no need to create an object)
result = MathUtils.add(10, 5)

# Print the result
print("Sum:", result)
