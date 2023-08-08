a_global_var = 100


def adder(x, y):
    return x + y


def do_something():
    global a_global_var
    a_local_var = 1
    print('In do_something()')
    a_global_var = 50
    print(a_local_var)
    print('Exiting do_something()')


print('Starting')
print(a_global_var)
print(do_something())
print(a_global_var)
print('Done', ("-" * 30))
