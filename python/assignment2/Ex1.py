# Assignment 2, Exercise 1

def sortList(list_in):
    # Sort input list
    sorted_list = sorted(list_in)
    return sorted_list


def sortDict(dic_in):
    # Write code here!
    sorted_dict = {}
    for key, val in dic_in.items():
        sorted_dict[key] = sortList(val)
    return sorted_dict


# Test
test_in = {'n1': [4, 1, 5], 'n2': [3, 1, 0], 'n3': [-1, 1, 9]}
print("Input")
print(test_in)

test_out = sortDict(test_in)
print("Output")
print(test_out)
