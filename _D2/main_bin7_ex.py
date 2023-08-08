class Person:
    """Represents people using a name and age"""
    def __init__(self, name, age=18):
        print('Person.__init__()')
        self.name = name
        self.age = age
        self.address = 'London'

    def __str__(self):
        return f'Person {self.name} - {self.age}: {self.address}'

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age} at={self.address})'


print('Starting')

p = Person('John', age=21)
print(p.name, p.age, p.address)
p.name = 'Bob'
print(p.name, p.age, p.address)

b = Person('Melly', age=19)
b.address = 'Manchester'
print(b)


data = [b, b]
print(*data)

print('Done', ("." * 30))

