# Assignment 1, Exercise 10

def modify_list(l):
    l_new = []
    # Write code here!
    tmp = ('TMP',)
    for i in l:
        if type(i) is tuple:
            i = i[:-1]
            i += tmp
        l_new.append(i)
    return l_new


# Test
l_in = [3, -1, ('a', 20, 'x'), (40, 'b', 'k'), (70, 80, 'c')]
l_out = modify_list(l_in)
print("Before:")
print(l_in)
print("After:")
print(l_out)
