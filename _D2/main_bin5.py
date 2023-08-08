def print_msg(massage):
    """Print out a hello world massage,
    to use ut call:
    print_msg"""
    print(massage)


print('Starting')

print_msg('Hellow word')
print_msg('Good bye')

print('Done', ("-" * 30))

def greeter(name,
            title='Mx',
            prompt='Welcome',
            message='Hello'):
    print(f'{prompt} {title} {name} -  {message}')


print('Starting')
greeter('John', 'Dr')
greeter('Denise')
greeter('Adam', message='Hi', title='Mr')
greeter(title='Ms',
        prompt='Hola',
        name='Natalia',
        message='Buenus Dias')
print('Done', ("-" * 30))

