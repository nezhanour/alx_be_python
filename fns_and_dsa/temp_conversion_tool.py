FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    #°C = (°F - 32) × 5/9
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    # (°C * 1.8) + 32 = °F
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input("Enter the temperature to convert: "))
celsiusOrFahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
if celsiusOrFahrenheit == "c":
    print(f"{temperature}°{celsiusOrFahrenheit.upper()} is {convert_to_fahrenheit(temperature)}°F")
elif celsiusOrFahrenheit == "f":
    print(f"{temperature}°{celsiusOrFahrenheit.upper()} is {convert_to_celsius(temperature)}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")
