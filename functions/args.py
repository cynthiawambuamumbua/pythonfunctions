def mycountry(country="Rwanda"):
    print(f"Hello from {country}")


def greet(*names):
    for name in names:
        print(f"Hello {name}")

def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
    return answer

def multiply(*numbers):
    product=1
    for number in numbers:
        product*=number
    return product

def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

def my_function(*args,**kwargs):
    print(f"hello world,args,kwargs")


def myFun(*args):
    for arg in args.list():
        print(arg)


def person(*data):
    print(data)

def my_function(*kids):
    print(f"The youngest child is"+kids[2])

#A function named concatenate_args that takes any number of string arguments 
#inpositional arguments format and concatenates them into a single string
def concatenate_args(*names):
    string=""
    for name in names:
        string += name
    return string

# A function named concatenate_kwargs that takes any number of string arguments in 
# keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    result = ""
    for key,value in kwargs.items():
        result += value
    return result

def greet(name):
    print("Hello",name)
    print("How do you do?")
greet("jack")


def add(num1,num2):
    result=num1+ num2
    print("The sum is",result)
add(12,45)