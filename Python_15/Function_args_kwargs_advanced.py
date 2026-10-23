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
