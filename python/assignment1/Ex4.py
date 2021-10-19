# Assignment 1, Exercise 4

def find_max_min(data):
    # Write code here!
    d_max = 0
    d_min = 0
    for i in data:
        if d_max < i:
            d_max = i
        if d_min > i:
            d_min = i

    return d_max, d_min


# Test
data_in = [3, -10, 4, 90, 100, 101.2, 243.9]
max_data, min_data = find_max_min(data_in)
print("maximum: {:f}".format(max_data))
print("minimum: {:f}".format(min_data))
