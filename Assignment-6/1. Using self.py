
# Define a class named Student
class Student:
    # Constructor method to initialize name and marks
    def __init__(self, name, marks):
        # 'self.name' and 'self.marks' are instance variables
        # 'name' and 'marks' are parameters passed during object creation
        self.name = name
        self.marks = marks

    # Method to display student details
    def display(self):
        # Print the student's name
        print(f"Student Name: {self.name}")
        # Print the student's marks
        print(f"Marks: {self.marks}")

# Example usage:

# Create an instance of the Student class with name "Mathias" and marks 90
student1 = Student("Mathias", 90)

# Call the display method to print the student's details
student1.display()
