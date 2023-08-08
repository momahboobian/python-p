class Quantity:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Quantity(value={self.value})'

    def __add__(self, other):
        return Quantity(self.value + other.value)

    def __sub__(self, other):
        return Quantity(self.value - other.value)


print('Starting')

q1 = Quantity(5)
q2 = Quantity(2)
q3 = q1 + q2
q4 = q1 - q2

print(q1)
print(q2)
print(q3)
print(q4)

print('Done', ("." * 30))