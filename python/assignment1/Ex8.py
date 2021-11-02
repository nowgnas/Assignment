# Assignment 1, Exercise 8

def swap_case_str(str1):
    # Tip) use .lower() and .upper()
    # Write code here!

    result_str = ""
    for i in str1:
        if i.islower():
            result_str += i.upper()
        else:
            result_str += i.lower()

    return result_str


print(swap_case_str("Python Homework!"))
print(swap_case_str("Incheon University"))
