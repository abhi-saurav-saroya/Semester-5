def celsius_to_fahrenheit(c: float) -> float:
    """
        Function to convert Celsius to Fahrenheit
    """
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """
        Function to convert Fahrenheit to Celsius
    """
    return (f - 32) * 5 / 9

# Taking input from the user
choice = input("Enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ")

if choice.strip().upper() == "C":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice.strip().upper() == "F":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid choice")