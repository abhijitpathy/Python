# Pratice  questions
#1
def multiply(*args):
    total = 1
    for i in args:
        total*=i
    return total
multiply(12,12)

# If you call the function with no arguments (multiply()), the loop is skipped, and it returns 1 because of your initial total = 1.

#2
def print_profles(**kwargs):
    print(kwargs)
    return kwargs
print_profles(p=12,k=13,l=13)

#3
def make_message(name,/,*,greeting="Hello"):
    print(name,greeting)

make_message("Abhi")
# if you call this function with incorrect argument it will show type error 
# and here befotre the slash are positional paramenters whereas after the asterisk  there is default parameters

#4
def values(a,b,c):
    return a,b,c

numbers = [4,5,6]
print(values(*numbers))

#5
def introduce(name, age):
    print(f"Name: {name}, Age: {age}")

person = {"name": "Ravi", "age": 21}

introduce(**person)

#6
def add(a, b):
    """Add two numbers together.

    Parameters:
    a - first number
    b - second number

    Returns:
    The sum of a and b
    """
    return a + b
print(add.__doc__)


#9
#  if the  same parameter  gets a value both in positional and kwargs the function sti;ll works because the value which is in kwargs is packed inside the dictionary.

#10
# here *args is used for packing the arguments into a single tuple
# whereas *values is used to unpack a tuple during fuction calling which converts a list or a tuple to speparate positional arguments 
