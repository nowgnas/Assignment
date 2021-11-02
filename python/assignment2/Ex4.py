# Assignment 2, Exercise 4


def countUpperAndLower(s):
    d = {"UC": 0, "LC": 0}

    # Write code here!
    for i in s:
        if i.islower():
            d["LC"] += 1
        elif i.isupper():
            d["UC"] += 1

    print("Input string: ", s)
    print("Number of upper case characters: ", d["UC"])
    print("Number of lower case characters: ", d["LC"])


# Test
countUpperAndLower("Inchoen University")
