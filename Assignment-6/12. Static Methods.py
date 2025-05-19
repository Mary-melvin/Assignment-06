
# Define a class named TemperatureConverter
class TemperatureConverter:
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Use the formula: (C × 9/5) + 32
        return (c * 9/5) + 32

# Example usage:

# Call the static method directly using the class name (no need to create an object)
celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)

# Print the result
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
