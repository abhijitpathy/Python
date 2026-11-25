#  predict the output
#A 20 10
#B unboundlocalerror
#C value is not defined
#D 1
#E 1
#f 9

#pratice problems
#1
def place():
    city = "tokyo"
    print(city)
place()
#2
school = "kv"
def study():
    global school
    print(school)
study()
#3
age= 23
if age >=18 :
    gender = "male"
    print("adult")
print(gender)
#4
for i in range(3):
    name = "Abhi"
    print(i)
print(name)
#5
#scope means from which part of the program the variable can be excessed is known as scope but lifetime means how long a variable can keep binding or kepp reference of an object

#6 200 100
#7 fix code
clicks = 0
def click():
    global clicks
    clicks += 1
    print(clicks)
click()
#8
# this code raises an error beacause here the variable is readed after the print statement due to which python cant acess the value of the variable
# 8
# 9
def outer():
    msg = "hlo"
    def inner():
        print(msg)
    inner()
outer()
#10
def get_list():
    return [10, 20, 30]

numbers = get_list()

print("Original list:", numbers)

numbers.append(40)

print("Modified list:", numbers)
# 11
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
print(counter())
#12 3 2 1
#13
# The loop variable is created in a separate local scope that exists only for the comprehension. This prevents it from overwriting a variable with the same name in the surrounding scope.

#14
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
# here only the inner function is active and outer functions runs only once whereas the count remains alive because it can be acessed by the inner most  function

#15
# variable names such as list , str, sum is avoided beause these are keywords in python and these shouldn't be used as for the naming convention of variable in python and it does causes error and bugs in code if used.
