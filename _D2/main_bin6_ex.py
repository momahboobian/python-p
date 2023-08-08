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

print('Starting')
def f1(x): return x * x
def f2(x, y): return x


print(f1)
print(f2)
print(adder)
print('.' * 25)
print(f1(5))
print(adder(2, 3))
print(f2(2, 3))
print('Done', ("-" * 30))
