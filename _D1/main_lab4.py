readings = []
continue_to_enter_data = True

while continue_to_enter_data:
    input_string = input("Please enter a temperature reading (-1 to end): ")

    if input_string == '-1':
        continue_to_enter_data = False
    else:
        # Check for validity of input
        if input_string.count('.') == 1 and input_string.replace('.', '').isnumeric():
            temperature = float(input_string)
            readings.append(temperature)
            print(f"Added temperature {temperature:.2f} to readings.")
        else:
            print("Invalid input. Must be a valid positive floating-point number.")

# Display the entered temperature readings
print("Temperature readings input:", readings)

# Print the length of the list
print("Number of readings:", len(readings))


readings.reverse()
print('Temperature readings in reverse:', readings)

print(f'There are {readings.count(0.0)} Zero readings')

readings_copy = readings.copy()
print('Copy of temperature readings:', readings_copy)

readings_copy.append(5.5)
print('Modified copy of temperature readings:', readings_copy)

print('Original Temperature readings:', readings)
print('Copy of Original Temperature readings:', readings_copy)

print(f'Popping element from end of copy list: {readings_copy.pop()}')
print('Modified copy after popping:', readings_copy)