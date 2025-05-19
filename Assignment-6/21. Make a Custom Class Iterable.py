
# Define the Countdown class
class Countdown:
    # Constructor to initialize the starting number
    def __init__(self, start):
        self.current = start  # Store the current number

    # __iter__ returns the iterator object itself (self)
    def __iter__(self):
        return self

    # __next__ defines what happens on each iteration
    def __next__(self):
        if self.current < 0:
            # StopIteration signals the end of iteration
            raise StopIteration
        else:
            # Store the value to return, then decrement
            value = self.current
            self.current -= 1
            return value

# Example usage:
# Create a Countdown object starting from 5
cd = Countdown(5)

# Use it in a for loop — it will count down from 5 to 0
for number in cd:
    print(number)
