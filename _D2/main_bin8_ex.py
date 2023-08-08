class Quantity:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Quantity(value={self.value})'

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Quantity(self.value + int(other))
        elif isinstance(other, Quantity):
            return Quantity(self.value + other.value)
        else:
            return None

    def __lt__(self, other):
        return self.value < other.value

    def __sub__(self, other):
        return Quantity(self.value - other.value)


def adder(x, y):
    return x + y


print('Starting', ("." * 30))

q1 = Quantity(5)
q2 = Quantity(2)
q3 = q1 + q2
q4 = q1 - q2
q5 = q1 + 6
q6 = q1 + 'John'

print(q1)
print(q2)
print(q3)
print(q4)
print(q5)
print(q6)

print('Done', ("." * 30))

print(adder(q1, q2))
print(adder(q1, 9))

print("." * 30)
# Comparison Operators
print(q1 < q2)