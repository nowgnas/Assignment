# Assignment 2, Exercise 5


def writeFile(input_list):
    # Write code here!
    with open('hw2_Ex5.txt', 'w') as file:
        for i in input_list:
            file.write(f'{i}\n')
    pass


# Test
input_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Input")
print(input_list)

# save file name hw2_Ex5.txt
writeFile(input_list)
