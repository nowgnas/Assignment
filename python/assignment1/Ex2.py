# Assignment 1, Exercise 2

# Check condition
def checkCondition(x):
    # Write code here!
    boolean = True
    if 100 <= x < 200 or 300 <= x < 350:
        boolean = True
    else:
        boolean = False
    print(f'{x}:{boolean}')


# Test
checkCondition(150)
checkCondition(400)
checkCondition(800)
