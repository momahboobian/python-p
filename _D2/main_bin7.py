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
#
# # Add string representation behaviour to the class
# print("\nUsing __str__:")
# print((readings))
#
#
# print('Done', ("." * 30))


# Print the list of readings
print(TemperatureReading.__doc__)

for reading in readings:
    print(reading)

print('Done', ("." * 30))