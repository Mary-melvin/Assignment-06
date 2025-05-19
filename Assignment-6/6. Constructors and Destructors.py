
# Define a class named Logger
class Logger:
    # Constructor method: called when an object is created
    def __init__(self):
        print("Logger object has been created.")

    # Destructor method: called when an object is destroyed
    def __del__(self):
        print("Logger object has been destroyed.")

# Example usage:

# Create an object of the Logger class
log = Logger()

# Do something with the object (optional)
print("Logger is active...")

# Delete the object explicitly (optional, or wait for garbage collection)
del log

# Note: The destructor is also called automatically when the program ends
