# Assignment 2, Exercise 3

import random
import sys


def createSortedRandomList(len):
    # Create sorted random list (0 ~ 10)
    randomList = []
    for i in range(0, len):
        n = random.randint(0, 10)
        randomList.append(n)

    randomList.sort()

    return randomList


def compress(list_in):
    # Compress list
    # Write code here!
    list_compressed = []
    num = sys.maxsize
    duple = []

    for i in list_in:
        if num != i:
            if len(duple) > 0:
                list_compressed.append(duple)
            duple = []
            duple.append(i)
            num = i
        else:
            duple.append(i)
    list_compressed.append(duple)

    return list_compressed


# Test
input_list = createSortedRandomList(12)
print("Input")
print(input_list)

output_list = compress(input_list)
print("Output")
print(output_list)
