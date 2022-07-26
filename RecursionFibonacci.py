#Fibonacci series is where the next number is the sum of the 2 preceding numbers
#First few numbers of the series are: 1,1,2,3,5,8, etc

#This number will give the nth term in the fibonacci sequence
def fibo(n):
    ans = 0
    if n == 1: return 1
    elif n == 2: return 1
    else: 
        ans = fibo(n-1) + fibo(n-2)
        return ans

i = int(input("Enter the nth fibonacci term you want: "))
print(f"{i}th term in the fibonacci series is: {fibo(i)}")