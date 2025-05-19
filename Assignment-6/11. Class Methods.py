
# Define a class named Book
class Book:
    # Class variable to track total number of books created
    total_books = 0

    # Constructor to initialize book details
    def __init__(self, title, author):
        self.title = title      # Instance variable for title
        self.author = author    # Instance variable for author

        # Call class method to increment the book count
        Book.increment_book_count()

    # Class method to increment the class variable total_books
    @classmethod
    def increment_book_count(cls):
        # 'cls' refers to the class itself
        cls.total_books += 1

    # Method to display book details
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Example usage:

# Create multiple Book objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Pride and Prejudice", "Jane Austen")

# Display the total number of books created
print("Total books created:", Book.total_books)
