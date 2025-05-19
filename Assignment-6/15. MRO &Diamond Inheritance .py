
# Define base class A with a method show()
class A:
    def show(self):
        print("Show method in class A")

# Class B inherits from A and overrides the show() method
class B(A):
    def show(self):
        print("Show method in class B")

# Class C also inherits from A and overrides the show() method
class C(A):
    def show(self):
        print("Show method in class C")

# Class D inherits from both B and C (multiple inheritance)
class D(B, C):
    pass  # No show() method here; it will use MRO to resolve

# Create an object of class D
d = D()

# Call the show() method on object d
d.show()  # MRO determines which class's show() is called

# Print the Method Resolution Order
print("\nMethod Resolution Order (MRO):")
print(D.__mro__)
