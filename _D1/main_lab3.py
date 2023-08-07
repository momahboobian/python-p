print('Starting factorial calculation program')
number = input('Please input the number: ')

# Validate that the user entered a non-negative integer value
if number.isnumeric():
    print(f'The number to calculate functional for is {number}')

    num = int(number) # Convert the input string to an integer

    if num == 0:
        print('0! factorial is 1')
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print(number + '! factorial is', str(factorial))

else:
    print('Not an integer number')




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
