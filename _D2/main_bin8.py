class TemperatureReading:
    """
    Add an equals method
    """

    CELSIUS = "Celsius"
    FAHRENHEIT = "Fahrenheit"

    def __init__(self, temp, date, location, scale=CELSIUS):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def __repr__(self):
        return f"TemperatureReading(temp={self.temp}, date='{self.date}', location='{self.location}', scale='{self.scale}')"

    def __eq__(self, other):
        return self.temp == other.temp

    def __ne__(self, other):
        return self.temp != other.temp

    def __gt__(self, other):
        return self.temp > other.temp

    def __ge__(self, other):
        return self.temp >= other.temp

    def __lt__(self, other):
        return self.temp < other.temp

    def __le__(self, other):
        return self.temp <= other.temp

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.temp + other
        elif isinstance(other, TemperatureReading):
            new_value = self.temp + other.temp
        else:
            raise TypeError("Unsupported operand type for +")
        return TemperatureReading(new_value, self.date, self.location, self.scale)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.temp - other
        elif isinstance(other, TemperatureReading):
            new_value = self.temp - other.temp
        else:
            raise TypeError("Unsupported operand type for -")
        return TemperatureReading(new_value, self.date, self.location, self.scale)



print('Starting', ("." * 30))

temperature1 = TemperatureReading(20.0, "2023-08-07", "City A", TemperatureReading.CELSIUS)
temperature2 = TemperatureReading(68.0, "2023-08-07", "City B", TemperatureReading.FAHRENHEIT)
another_temperature = TemperatureReading(14.6, '05/05/20', 'London')

# Add temperatures together
sum_temperature = temperature1 + temperature2
print("Add two temperatures:", sum_temperature)

# Add an int to a temperature
new_temperature1 = temperature1 + 5
print("Add a temperature and an int:", new_temperature1)

# Add a float to a temperature
new_temperature2 = temperature1 + 5.5
print("Add a temperature and a float:", new_temperature2)

# Subtract temperatures
diff_temperature = temperature2 - temperature1
print("Subtract two temperatures:", diff_temperature)

# Subtract an int from a temperature
new_temperature3 = temperature2 - 10
print("Subtract an int from a temperature:", new_temperature3)

# Subtract a float from a temperature
new_temperature4 = temperature2 - 7.5
print("Subtract a float from a temperature:", new_temperature4)


print('Done', ("." * 30))


# Define Further operators
print(temperature1 != temperature2)
print(temperature1 > temperature2)
print(temperature1 >= temperature2)
print(temperature1 == temperature2)
print(temperature1 != temperature2)
print(temperature1 < temperature2)
print(temperature1 <= temperature2)

print(temperature1 != another_temperature)
print(temperature1 > another_temperature)
print(temperature1 >= another_temperature)
print(temperature1 == another_temperature)
print(temperature1 != another_temperature)
print(temperature1 < another_temperature)
print(temperature1 <= another_temperature)

print('Done', ("." * 30))


# Revise the sort functions

# Create a list of temperature readings
readings = [
    TemperatureReading(13.5, '01/05/20', 'London', TemperatureReading.CELSIUS),
    TemperatureReading(12.6, '02/05/20', 'London', TemperatureReading.CELSIUS),
    TemperatureReading(15.3, '03/05/20', 'London', TemperatureReading.CELSIUS),
    # ... other readings ...
]

# Sort the list of temperature readings using the default sorting order (ascending)
sorted_readings = sorted(readings)
print("Sorted temperature readings:")
for reading in sorted_readings:
    print(reading)