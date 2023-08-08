class Person:
    """Represents people using a name and age"""
    def __init__(self):
        print('Person.__init__()')


print('Starting')

p = Person()
print(p)

print('Done', ("." * 30))
