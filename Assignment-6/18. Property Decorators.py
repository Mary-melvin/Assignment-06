
# Define the Product class
class Product:
    # Constructor to initialize the private attribute _price
    def __init__(self, price):
        self._price = price  # Conventionally private attribute

    # Getter method to access the price (read-only access)
    @property
    def price(self):
        print("Getting the price...")
        return self._price

    # Setter method to update the price (write access)
    @price.setter
    def price(self, value):
        print("Setting the price...")
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

    # Deleter method to delete the price (delete access)
    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Example usage:

# Create a Product object with an initial price
product = Product(100)

# Access the price using the getter
print(product.price)  # Output: 100

# Update the price using the setter
product.price = 150

# Confirm updated price
print(product.price)  # Output: 150

# Delete the price using the deleter
del product.price

# Try accessing again after deletion (will raise an AttributeError)
try:
    print(product.price)
except AttributeError as e:
    print("Error:", e)
