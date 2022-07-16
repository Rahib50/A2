#This algorithm looks through a sorted list to find a match with input
#Much more efficient than linear search which will be made apparent by the number of iterations needed for result.

def Bin(alist, upper, lower, inp):
    counter = 0
    flag = False    #Will turn True when a match is found
    
    while not flag and lower <= upper:
        counter += 1

        mid = (upper + lower) // 2  #The index of the mid value of list
        if alist[mid] == inp: flag = True #Exit to loop
        else:
            if alist[mid] > inp: upper = mid - 1 #Gets rid of the right half of list to search
            else: lower = mid + 1                #Gets rid of the left half of list to search

    if flag == True: 
        print(f"The item has been found after {counter} iteration(s) on index: {mid}")
    else: print("Item not found!")

import random

alist = [random.randint(0,1024) for i in range(10)] #random list formed and sorted afterwards
alist = sorted(alist)
print(alist)
inp = int(input("Enter the number you wish to look for: "))

Bin(alist, len(alist) - 1, 0, inp)
