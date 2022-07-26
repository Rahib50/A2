#Binary search may also have a recursive approach

def binary_search(inp, alist, high, low):
    found = False
    if high >= low:
         mid = (high + low) // 2
 
         if alist[mid] == inp: return mid
         elif alist[mid] > inp: return binary_search(inp, alist, mid-1, low)
         else: return binary_search(inp, alist, high, mid+1)
    else: return found     

import random
alist = sorted([random.randint(0,1024) for i in range(10)])

print(alist)

inp = int(input("Enter number you're looking for: "))
out = binary_search(inp, alist, len(alist)-1, 0)

if not out: print("ITEM DOESN'T EXIST!")
else: print(f"Item found at index: {out}")