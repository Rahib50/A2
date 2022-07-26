def bubble(list):
    sorted = False
    count = 0

    while not sorted:
        sorted = True 
        count += 1
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                sorted = False
    
    print(list)
    print("number of iterations:", count)

import random

alist = [random.randint(0,1024) for i in range(10)]
print(alist)
bubble(alist)