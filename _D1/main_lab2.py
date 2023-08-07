# Step 1: Make the application Interactive
print('Hello World!!!')
name = input('Enter your name: ')
print('Welcome', name)


# Step 2: Input some numbers
input1 = int(input('Please enter a number: '))
input2 = int(input('Please enter another number: '))

value = input1 + input2
print(f'The result of {input1} + {input2} is {value}')
print('The type of the value is', type(value))


# Step 3: Input two strings
input_string1 = input('Please enter a string: ')
input_string2 = input('Please enter another string: ')
str_value = input_string1 + input_string2
print(f'The result of {input_string1} + {input_string2} is {str_value}')
print('The type of the value is', type(str_value))


# Step 4: Concatenate a number and a String
title = 'Data Processing App Version' + str(1.0)
print(f'The title of this app is {title}')


# Step 5: Using None
user = None
print('user:', user) # user: None
print('user is None:', user is None) # user is None: True
print('user is not None:', user is not None) # user is not None: False
print('The type of the user', type(user)) # The type of the user <class 'NoneType'>



