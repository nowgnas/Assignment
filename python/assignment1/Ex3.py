# Assignment 1, Exercise 3
import sys

x = int(input("Input a positive integer : "))

# Write code here! (Modify str_out)
str_out = ''

remain = sys.maxsize

while True:
    if remain < 16:
        str_out += str(remain)
        break
    mul = x // 16
    remain = x % 16
    str_out += str(mul)

print(str_out)
