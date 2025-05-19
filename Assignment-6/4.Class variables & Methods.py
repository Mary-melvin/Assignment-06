
# Define a class named Bank
class Bank:
    # Class variable shared by all instances
    bank_name = "Default Bank"

    # Constructor to initialize the customer's name
    def __init__(self, customer_name):
        self.customer_name = customer_name

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        # 'cls' refers to the class, and we update the class variable
        cls.bank_name = name

    # Method to display customer and bank information
    def display(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Bank Name: {Bank.bank_name}")

# Example usage:

# Create two instances of the Bank class
customer1 = Bank("Melvin")
customer2 = Bank("Paul")

# Display initial bank information
print("Before changing bank name:")
customer1.display()
customer2.display()

# Change the bank name using the class method
Bank.change_bank_name("National Trust Bank")

# Display updated bank information
print("\nAfter changing bank name:")
customer1.display()
customer2.display()
