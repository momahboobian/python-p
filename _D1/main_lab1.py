name = input('Please enter your name: ')
print(name)

flag = bool(input('Can you drive: '))
print(type(flag))
print(flag)

age = input('What is you age: ')
print(type(age))
print(age)

print('Hello ' + name + ' you are ' + age + ' and you can drive is ' + str(flag))

print('Hello', name, ' you are', age, 'and you can drive is', flag)

print(f'Hello {name} you are {age} and you can drive is {flag}')
