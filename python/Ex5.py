# Assignment 1, Exercise 5

# Receives a positive integer number from the keyboard and stores it in x
x = int(input("Input a positive integer number : "))

# Write code here!
even_odd = ''
if x % 2 == 0:
    even_odd = 'even'
else:
    even_odd = 'odd'

print(f'{x} is an {even_odd} number!')
