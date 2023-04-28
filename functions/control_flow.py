# Write a function that uses while, if and continue 
# statements to print all the even numbers between 0 and 50. 
def numbers():
    x=0
    while x<50:
        x+=1
        if x%2==0:
             continue
        print(x)
           
# Write a function that takes an integer argument and 
# prints "Prime" if the number is prime, 
# and "Not prime" if the number is not prime.
def integer_argument():
    x=range(30)
    for i in x:
        if i%2==0:
            print(f"{i} Prime ")
        else:
            print(f"{i} Not Prime")

# Write a function that takes a list of integers 
# as input and prints the sum of all the even numbers in the list.
def list_integers(list):
    sum=[]
    list=[1,4,7,10,13,16]
    for i in list:
       if i % 2 == 0:
           sum=sum+list(i)
    print(i)

# Write a function that takes any two integers as input,
#  and prints the sum of all the numbers between 
# the two integers (inclusive) that are divisible by 3.
def sum_input():
    total = 0
    nums = [3,18]
    for num in nums:
        if num % 3 == 0:
            total += num
        print(total)
 


