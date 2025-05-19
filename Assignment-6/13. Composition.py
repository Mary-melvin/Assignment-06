
# Define the Engine class
class Engine:
    # Constructor to initialize engine type
    def __init__(self, engine_type):
        self.engine_type = engine_type

    # Method to describe the engine
    def start(self):
        print(f"{self.engine_type} engine is starting...")

# Define the Car class that uses composition to include an Engine object
class Car:
    # Constructor accepts an Engine object as a parameter
    def __init__(self, brand, engine):
        self.brand = brand          # Car brand (instance variable)
        self.engine = engine        # Composition: Engine object as an attribute

    # Method to start the car using its engine
    def start_car(self):
        print(f"Starting {self.brand} car.")
        self.engine.start()         # Access Engine's start method via composition

# Example usage:

# Create an Engine object
engine1 = Engine("V8")

# Create a Car object and pass the Engine object to it
car1 = Car("Ford Mustang", engine1)

# Start the car, which uses the Engine's start method
car1.start_car()
