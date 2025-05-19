
# Define a class named Counter
class Counter:
    # Class variable to keep track of the number of objects created
    object_count = 0

    # Constructor method (called when a new object is created)
    def __init__(self):
        # Increment the class variable each time an object is created
        Counter.object_count += 1

    # Class method to display the current object count
    @classmethod
    def display_count(cls):
        # Use 'cls' to refer to the class itself and access the class variable
        print(f"Number of Counter objects created: {cls.object_count}")

# Example usage:

# Create multiple objects of the Counter class
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Call the class method to display how many objects have been created
Counter.display_count()
