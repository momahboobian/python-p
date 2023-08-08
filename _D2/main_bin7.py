class TemperatureReading:
    """
    A class to represent a temperature reading.

    Attributes:
        temp (float): The temperature value.
        date (str): The date of the reading.
        location (str): The location of the reading.
        scale (str): The scale of the temperature (Celsius or Fahrenheit).

    Methods:
        __init__(temp, date, location, scale): Initialize a TemperatureReading object.
        __repr__(): Return a string representation of the object for debugging.
        __str__(): Return a formatted string representation of the object.
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

    def __str__(self):
        return f"TemperatureReading[{self.scale}]({self.temp} on {self.date} at {self.location})"

    def convert(self, new_scale):
        if new_scale == self.scale:
            return self  # No need to convert if scales are the same

        if new_scale == self.CELSIUS:
            new_temp = (self.temp - 32) * 5 / 9
        elif new_scale == self.FAHRENHEIT:
            new_temp = (self.temp * 9 / 5) + 32
        else:
            raise ValueError("Invalid scale")

        return TemperatureReading(new_temp, self.date, self.location, new_scale)


# Example usage
# readings = TemperatureReading(25.0, "2023-08-07", "City A")
readings = [
    TemperatureReading(13.5, '01/05/20', 'London', 'Celsius'),
    TemperatureReading(12.6, '02/05/20', 'London', 'Celsius'),
    TemperatureReading(15.3, '03/05/20', 'London', 'Celsius'),
    TemperatureReading(12.2, '04/05/20', 'London', 'Celsius'),
    TemperatureReading(16.6, '05/05/20', 'London', 'Celsius'),
    TemperatureReading(14.6, '05/05/20', 'London', 'Celsius'),
    TemperatureReading(15.6, '05/05/20', 'London', 'Celsius')
]
print("Using __repr__:")
print(repr(readings))

print('Done', ("." * 30))

# Add string representation behaviour to the class
print("\nUsing __str__:")
print(*readings)
print(readings[1])


# print('Done', ("." * 30))


# Print the list of readings
print(TemperatureReading.__doc__)

for reading in readings:
    print(reading)

print('Done', ("." * 30))

# Conversion method
reading_celsius = TemperatureReading(25.0, "2023-08-07", "City A", TemperatureReading.CELSIUS)
converted_reading_fahrenheit = reading_celsius.convert(TemperatureReading.FAHRENHEIT)
print("Original Reading:")
print(reading_celsius)
print("\nConverted Reading:")
print(converted_reading_fahrenheit)


# Utility function to extract temperature from a TemperatureReading object
def extract_readings(reading):
    return reading.temp

# Example usage
temp1 = TemperatureReading(13.5, '01/05/20', 'London', TemperatureReading.CELSIUS)
temp2 = temp1.convert(TemperatureReading.FAHRENHEIT)
print(f'temp1: {temp1}')
print(f'temp2: {temp2}')

# Create a list of readings
readings = [
    TemperatureReading(13.5, '01/05/20', 'London', TemperatureReading.CELSIUS),
    TemperatureReading(12.6, '02/05/20', 'London', TemperatureReading.CELSIUS),
    # ... other readings
]

# Print list of temperature readings using __repr__()
print("List of temperature readings using __repr__():")
print(readings)

# Print list of temperature readings using __str__()
print("\nList of temperature readings using __str__():")
print(*readings, sep="\n")