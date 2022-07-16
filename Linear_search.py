# A very simple searching algorithm
# Looks through each element of list in order until a match with input is found

def linear(alist, inp):
    found = False
    i = 0
    while i < len(alist) and not found:
        if alist[i] == inp:
            found = True
        else: i += 1
    
    if found == True: print("Found in index:", i)
    else: print("Item not found!")

import random
alist = [random.randint(0,1024) for i in range(10)]
print(alist)
inp = int(input("Enter number You want: "))
linear(alist, inp)