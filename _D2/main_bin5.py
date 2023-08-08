readings = [13.5, 11.1, 17.5, 12.6, 15.3, 12.2, 16.6, 14.6]


# Step 1: Implement a function to average the temperatures
def average(data):
    return sum(data) / len(data)


print('Starting')
print(average(readings))
print('Average temperature = {:.2f}'.format(average(readings)))
print(f'Average temperature = {average(readings):.2f}')
print('Done', ("-" * 30))


# Step 2: Calculate the median of the data
def median(data):
    sorted_data = sorted(data)  # Sort the data
    data_length = len(data)  # Get the length of the data
    index = (data_length - 1) // 2  # Calculate the index for the median

    if data_length % 2 == 1:  # Check if the data length is odd
        return sorted_data[index]  # Return the value at the calculated index
    else:
        # If the data length is even, calculate the average of the two middle values
        return (sorted_data[index] + sorted_data[index + 1]) / 2.0


# Print the median
print(f'Median temperature value = {median(readings)}')
print('Done', ("-" * 30))


# minimum and maximum functions
def minimum(data, start=0):
    if start < 0 or start >= len(data):
        return None  # Invalid start position

    min_value = float('inf')  # Initialize with positive infinity

    for i in range(start, len(data)):
        if data[i] < min_value:
            min_value = data[i]

    return min_value


print(f'Min temp in list = {minimum(readings)}')
print(f'Min temp in list starting position 4 = {minimum(readings, 3)}')
print('Done', ("-" * 30))


def maximum(data, start=0):
    if start < 0 or start >= len(data):
        return None  # Invalid start position

    max_value = float('-inf')  # Initialize with negative infinity

    for i in range(start, len(data)):
        if data[i] > max_value:
            max_value = readings[i]

    return max_value


print(f'Max temp in list = {maximum(readings)}')
print(f'Max temp in list starting position 4 = {maximum(readings, 3)}')
print('Done', ("-" * 30))


# Return a data range tuple
def data_range(data):
    if not readings:
        return None  # Return None if the list is empty

    min_temp = float('inf')
    max_temp = float('-inf')

    for temperature in data:
        if temperature < min_temp:
            min_temp = temperature
        if temperature > max_temp:
            max_temp = temperature

    return min_temp, max_temp  # Return a tuple


min_temp, max_temp = data_range(readings)
print(f'Range of temperatures from {min_temp} to {max_temp}')
print('Done', ("-" * 30))


# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temperature_celsius = 13.5
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

print(f'{temperature_celsius} Celsius as Fahrenheit: {temperature_fahrenheit:.2f}')
print('Done', ("-" * 30))


# Convert Fahrenheit into Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(f'56.3 fahrenheit as celsius - {fahrenheit_to_celsius(56.3):.1f}')
print('Done', ("-" * 30))
