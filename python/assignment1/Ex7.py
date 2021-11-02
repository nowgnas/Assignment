# Assignment 1, Exercise 7

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

# Write code here!
key = ''
value = 0

for _xk, _xv in x.items():
    for _yk, _yv in y.items():
        if _xk == _yk and _xv == _yv:
            key = _xk
            value = _xv

print(f'{key}: {value} is present in both x and y')
