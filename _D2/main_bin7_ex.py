class Person:
    """Represents people using a name and age"""
    def __init__(self, name, age=18, rate=5.5):
        print('Person.__init__()')
        self.name = name
        self.age = age
        self.address = 'London'
        self.rate = rate

    # def __str__(self):
    #     return f'Person {self.name} - {self.age}: {self.address}'

    def birthday(self):
        print(f'Happy birthday {self.name} you were {self.age}')
        self.age = self.age + 1
        print(f'You are now {self.age}')

    def calculate_pay(self, hours_worked):
        """calculate the pay for the person
        hours should be a positive integer"""
        return hours_worked * self.rate

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age} at={self.address})'


print('Starting')

p = Person('John', 21)
print(p.name, p.age, p.address)
p.name = 'Bob'
print(p.name, p.age, p.address)

b = Person('Melly', age=19)
b.address = 'Manchester'
print(b)
print('id(b):', id(b))
print(b.__doc__)

data = [b, b]
print(*data)
print('Done', ("." * 30))


print('Starting')
p1 = Person('John', 21)
print(p1)
p1.birthday()
print(p1)
print('Done', ("." * 30))

print('Starting')
p2 = Person('John', 21, rate=7.55)
print(p2.calculate_pay(40))
print('Done', ("." * 30))