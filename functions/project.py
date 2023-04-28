# write a function that returns the Nth Fibonacci number
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(11))
# write a python function that takes a list of numbers that returns the sum of all even numbers in the list
def evenNumbers(*nums):
    sum=0
    newList=[]
    for num in nums:
        if num%2==0:
            sum+=1
            return num
        print(evenNumbers())
        