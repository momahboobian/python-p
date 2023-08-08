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
f1 = lambda x: x * x
f2 = lambda x, y: x
print(f1)
print(f2)
print(adder)
print('.' * 25)
print(f1(5))
print(adder(2, 3))
print(f2(2, 3))
print('Done', ("-" * 30))


def is_even(item):
    return item % 2 == 0


def multplier(item):
    return item * item


print('Starting')

data = [1, 3, 5, 6, 7, 9, 10]

even_data = []
for item in data:
    if item % 2 == 0:
        even_data.append(item)
print(even_data)


# Functional Style using a HoF
even_data2 = list(filter(is_even, data))
for d in even_data2:
    print(d, ",", even_data2)

even_data3 = list(filter(
    lambda item: item % 2 == 0,
    data))
print(even_data3)


result = []
for item in data:
    temp = item * item
    result.append(temp)
print(result)

# Functional Style HOF approach
results2 = list(map(lambda x: x * x, data))
print(results2)

results3 = list(map(multplier, data))
print(results3)

print('Done', ("-" * 30))


# Functional Style nesting
results2 = (list(map(multplier,
                 filter(is_even, data))))
print(results2)

results3 = (list(map(lambda x: x * x,
                     filter(lambda x: x % 2 == 0, data))))
print(results3)