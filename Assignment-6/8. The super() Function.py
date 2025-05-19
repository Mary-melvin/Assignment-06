
# Define the base class named Person
class Person:
    # Constructor to initialize the name attribute
    def __init__(self, name):
        self.name = name  # Public attribute

# Define the derived class named Teacher that inherits from Person
class Teacher(Person):
    # Constructor to initialize name and subject
    def __init__(self, name, subject):
        # Call the base class constructor using super()
        super().__init__(name)
        # Initialize the subject attribute specific to Teacher
        self.subject = subject

    # Method to display teacher information
    def display_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage:

# Create an object of the Teacher class
teacher1 = Teacher("Mr. Melvin", "Mathematics")

# Display the teacher's information
teacher1.display_info()
