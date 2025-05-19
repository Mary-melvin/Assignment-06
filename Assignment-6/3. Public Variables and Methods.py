
# Define a class named Car
class Car:
    # Constructor to initialize the public variable 'brand'
    def __init__(self, brand):
        # Public variable 'brand' (accessible from outside the class)
        self.brand = brand

    # Public method to simulate starting the car
    def start(self):
        print(f"The {self.brand} car is starting...")

# Example usage:

# Create an instance of the Car class with brand name 'Toyota'
my_car = Car("Toyota")

# Access and print the public variable 'brand' from outside the class
print("Car Brand:", my_car.brand)

# Call the public method 'start()' from outside the class
my_car.start()
