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
