a_global_var = 100


def adder(x, y):
    return x + y


def do_something():
    a_local_var = 1
    print('In do_something()')
    print(a_global_var)
    print(a_local_var)
    print('Exiting do_something()')


print('Starting')
print(do_something())
print(a_global_var)
a_global_var = 10
print('Done', ("-" * 30))
