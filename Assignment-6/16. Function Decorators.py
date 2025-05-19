
# Define the decorator function
def log_function_call(func):
    # Define a wrapper function that adds extra behavior
    def wrapper():
        print("Function is being called")  # Code to run before the function
        return func()  # Call the original function
    return wrapper  # Return the wrapper function

# Apply the decorator to say_hello() using the @ syntax
@log_function_call
def say_hello():
    print("Hello, world!")

# Call the decorated function
say_hello()
