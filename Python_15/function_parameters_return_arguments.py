#begineer
#1
def welcome():
    print("welcome to python")
welcome()
welcome()
welcome()

#2
def greet(name):
    print("Hlo nice to meet you",name)

greet("afrox")

#3
def show_number(number):
    print("the passed number in the function is",number)
show_number(12)

#4
def add(a,b):
    return a +b
print(add(12,13))

#5 
def square(number):
    return number**2
print(square(12))

#6 
def is_even(number):
    if  number % 2 ==0:
        return True
    else:
        return False

print(is_even(12))

#7
def get_full_name(first_name,last_name):
    return first_name + last_name
print(get_full_name("Abhi", "rathore"))

#8
def introduce(name,city="pune"):
    return f"my name is {name} and i live in {city}"
print(introduce("abhi","pune"))
print(introduce("Abhi",))
# it works in both cases as city is already defined as pune in the function

#9
def subtract(a,b):
    return a - b
print(subtract(12,13))
print(subtract(13,12))

#10
def get_min_max(a,b):
    if a>b:
        return f"{a} is greater value and {b} is smaller value"
    elif b>a:
        return f"{b} is greater value and {a} is smaller value"
    else:
        return F"both {a} and {b} are same values"

print(get_min_max(14,13))


# intermediate
#11
def calculate(a,b):
    sum = a +b
    sub = a -b
    multiply = a * b
    division = a / b
    return f"the sum is {sum}, the difference is  {sub}, the product is {multiply}, the quotient is {division}"
print(calculate(24,12))

#12
def count_digits(number):
    count = 0
    for i in number:
        count+=1
    return count

print(count_digits("112"))

#13
def classify_number(number):
    if number>0:
        return "positive"
    elif number<0:
        return "negative"
    else:
        return "number is zero"

print(classify_number(0))

#14
def calculate_total(price,quantity=1):
    total_price = price*quantity
    return total_price

print(calculate_total(12))

#15
def create_email(username,domain="example.com"):
    return username + domain
print(create_email("Abhi@1234"))

#16
def format_name(first, last, uppercase=False):
    full_name = f"{first} {last}"
    if uppercase:
        return full_name.upper()
    return full_name
print(format_name("abhi","parth",True))

#17
def percentage(marks,total=100):
    percentage = (marks/total)*100
    return percentage
print(percentage(80))

#18
def convert_minutes(minutes,seconds_per_minute=60):
    total_seconds = minutes*seconds_per_minute
    return total_seconds
print(convert_minutes(12))

#19
def student_details(name,age,city):
    return f"my name os {name}, my age is {age} and i live in {city}"
print(student_details("abhi",18,"dehradun"))

#20
def bill(item,quantity=1,price=100):
    return f"the item is {item}, the quantity is {quantity} and the price is {price} "
print(bill("milton bottle"))

# challenging
#21
#using loops
def analyze_number(number):
    abs_value = -number if number < 0 else number
    
    is_even = (number % 2 == 0)
    if abs_value == 0:
        num_digits = 1
    else:
        num_digits = 0
        temp = abs_value
        while temp > 0:
            num_digits += 1
            temp //= 10
            
    return abs_value, is_even, num_digits
print(analyze_number(-13))

# without using loops
def analyze_number(number):
    absolute_value = -number if number < 0 else number
    is_even = (number % 2 == 0)
    num_digits = len(str(absolute_value))
            
    return absolute_value, is_even, num_digits

#22
def calculate_stats(a,b,c):
    sum = a+b+c
    print("sum of three is ",sum)
    if a>b>c:
        return f"{a} is the largest and {c} is the smallest"
    if a>c>b:
        return f"{a} is the largest and {b} is the smallest"
    if b>a>c:
        return f"{b} is the largest and {c} is the smallest"
    if b>c>a:
        return f"{b} is the largest and {a} is the smallest"
    if c>b>a:
        return f"{c} is the largest and {a} is the smallest"
    if c>a>b:
        return f"{c} is the largest and {b} is the smallest"

print(calculate_stats(12,14,13))

#23
def make_sentence(subject,verb,object):
    print(subject,verb,object)

make_sentence(verb="speaks",object="loudly",subject="He")

#24
def apply_discount(price, discount=0):
    final_price = price - (price * (discount / 100))
    return final_price

print(apply_discount(1200,40))

#25
def calculate_pay(hours,rate=200,bonus=0):
    return hours*rate+bonus
print(calculate_pay(rate = 120,hours = 4,bonus=12))


#26
def get_coordinate(x=0,y=0):
    return f"the cordinates are {x},{y}"
print(get_coordinate(x=12))

#27
def compare(a, b):
    if a > b:
        comparison = "A is greater"
    elif b > a:
        comparison = "B is greater"
    else:
        comparison = "Equal"
        
    diff = a - b if a >= b else b - a
    
    return comparison, diff

print(compare(67,84))

#28
def convert_temperature(value, scale="C"):
    if scale.upper() == "C":
        return (value * 9/5) + 32
    elif scale.upper() == "F":
        return (value - 32) * 5/9

#29
def calculate_results(marks,passing_marks=35):
    if marks >=passing_marks:
        return "pass"
    else:
        return "fail"

print(calculate_results(35))

#30
def order_summary(item,quantity=1,price=100,delivery_fee=40):
    total_cost = quantity *price + delivery_fee
    return f"The item is {item} and the total cost is {total_cost}"
print(order_summary("milton",delivery_fee=100,quantity=12,price=1200))

        



    