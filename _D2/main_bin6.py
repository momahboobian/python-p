def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


celsius_temperatures = [25.0, 30.5, 15.8, 20.2]
fahrenheit_temperatures = []

print('Starting')
# Convert all temperatures to Fahrenheit
for celsius in celsius_temperatures:
    fahrenheit = celsius_to_fahrenheit(celsius)
    fahrenheit_temperatures.append(fahrenheit)

print(f'Fahrenheit Temperatures: {fahrenheit_temperatures}')

# Convert back to Celsius
converted_celsius_temperatures = []
for fahrenheit in fahrenheit_temperatures:
    celsius = fahrenheit_to_celsius(fahrenheit)
    converted_celsius_temperatures.append(celsius)


print(f'Converted Celsius Temperatures: {converted_celsius_temperatures}')
print('Done', ("-" * 30))


# Select all temperatures above 14.0
temperatures = [25.0, 30.5, 15.8, 20.2, 10.0, 18.7]
higher_temperatures = [temp for temp in temperatures if temp > 14.0]

print('Starting')
print(f'Temperatures above 14.0: {higher_temperatures}')
print('Done', ("-" * 30))

