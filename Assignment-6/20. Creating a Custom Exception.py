
# Define a custom exception class that inherits from the built-in Exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        super().__init__(message)  # Pass the custom message to the base class

# Function to check age and raise the custom exception if age is invalid
def check_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise the custom exception
    else:
        print("Access granted. Age is valid.")

# Example usage:
try:
    user_age = int(input("Enter your age: "))  # Take input from user
    check_age(user_age)  # Call the function that may raise the exception
except InvalidAgeError as e:
    print("InvalidAgeError:", e)  # Handle the custom exception
except ValueError:
    print("Please enter a valid integer age.")  # Handle non-integer inputs
