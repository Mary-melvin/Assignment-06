
# Define the Employee class
class Employee:
    # Constructor to initialize employee details
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    # Method to display employee information
    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

# Define the Department class that aggregates Employee objects
class Department:
    # Constructor to initialize department name and employee reference
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name    # Name of the department
        self.employee = employee      # Aggregation: Reference to an external Employee object

    # Method to display department and associated employee information
    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_info()  # Accessing Employee's method through aggregation

# Example usage:

# Create an independent Employee object
emp1 = Employee("Melvin", 95)

# Create a Department object and pass the Employee object to it
dept1 = Department("Human Resources", emp1)

# Show department and employee details
dept1.show_details()
