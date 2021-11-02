# Assignment 1, Exercise 9

def concat_dic(d1, d2, d3):
    d4 = {}
    # Write code here!
    d4.update(d1)
    d4.update(d2)
    d4.update(d3)
    return d4


dic1 = {'a': 10, 'b': 20}
dic2 = {'c': 30, 'd': 40}
dic3 = {'e': 50, 'f': 60}

# Concatenate
dic4 = concat_dic(dic1, dic2, dic3)

# Print
print(dic4)
