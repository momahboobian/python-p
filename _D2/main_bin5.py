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