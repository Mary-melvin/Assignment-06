
# Define a class named Employee
class Employee:
    # Constructor to initialize the variables
    def __init__(self, name, salary, ssn):
        self.name = name         # Public variable (can be accessed directly)
        self._salary = salary    # Protected variable (should be accessed with caution)
        self.__ssn = ssn         # Private variable (name mangled, not directly accessible)

    # Method to display all values (internal access is allowed)
    def display_info(self):
        print("Inside class:")
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

# Create an object of the Employee class
emp = Employee("Melvin Paul", 70000, "123-45-6789")

# Accessing the public variable
print("Public Access:")
print("Name:", emp.name)  # ✅ Accessible

# Accessing the protected variable
print("\nProtected Access:")
print("Salary:", emp._salary)  # ⚠️ Technically accessible, but not recommended (by convention)

# Accessing the private variable
print("\nPrivate Access:")
try:
    print("SSN:", emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError:
    print("Cannot access private variable '__ssn' directly!")

# Accessing the private variable using name mangling (not recommended)
print("\nAccessing private variable with name mangling:")
print("SSN (via name mangling):", emp._Employee__ssn)  # ✅ Works, but discouraged

# Display all info using the class method
print("\nCalling method inside class:")
emp.display_info()
