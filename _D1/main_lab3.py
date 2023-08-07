print('Starting Factorial Calculation')

while True:
    input_number = input('Please input the number: ')

    if input_number.isnumeric():
        print('Valid Input')
        break
    else:
        print('Invalid Input')

print(f'The number to calculate the factorial for is {input_number}')

number = int(input_number)

if number == 0:
    print('0! factorial is 1')
elif number == 1:
    print('1! factorial is 1')
else:
    # Algorithm to calculate the factorial for an integer number
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    print(f'{number}! is {factorial}')

print('Done')

# age = (int(input('Please input your age: ')))
# print(f'You are {age}')
#
#
# if age < 13:
#
#     print('Child!')
#     print('-----')
# elif 12 < age < 20:
#     print('Teenager')
# else:
#     print('Adult')
#
# print('Done')
#
# status = 'Teenager' if 12 > age < 18 else 'not teenager'
# print(status)
#
#
# validData = False
# print(validData)
#
# while not validData:
#     age = int(input('Please enter your age: '))
#     if age < 0 or age > 120:
#         print('Invalid age')
#         print(validData, '', end='')
#     else:
#         break
