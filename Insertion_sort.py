#Another sorting algorithm where elements are placed in a sorted sub-list one at a time

def sort(alist):
    
    for i in range(1, len(alist)):
        if alist[i] < alist[i-1]:
            for j in range(i):
                if alist[i] < alist[j]:
                    alist[i], alist[j] = alist[j], alist[i]

    return alist

import random
alist = [random.randint(0, 1024) for i in range(10)]
print(alist)
print(sort(alist))