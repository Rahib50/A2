#Recursion is when a function calls itself. 
#They have a winding and unwinding phase.
#Algorithms using recursive approach usually are smaller than iterative
#Drawback: there is a limit to the amount of input (recursion depth) it can take unlike iterative

#factorial is just the multiplication of an input number and all number less than it till 1
def factorial(n):
    result = 0
    if n == 0: return 1 #Base case
    else: 
        result = n * factorial(n - 1) #General case
        return result

i = int(input("Enter the number factorial: "))
print(f"The result of {i}! = {factorial(i)}")