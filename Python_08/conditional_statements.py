# Task 1
num = int(input("Enter a number : "))
if num>10 :
    print("Greater than 10")

# Task 2

age = int(input("Enter your age :"))
if age>=18 :
    print("Adult")

# Task 3
num = int(input("Enter a number :"))
if num>0 :
    print("positive")

# Task 4
marks = int(input("enter your mark :"))
if marks>=40 :
    print("pass")


# task 5
num  = int(input("enter a number :"))
if num==0 :
    print("Zero")

# task 6

num = int(input("enter a number :"))
if num>0 :
    print("positive")
else :
    print("not positive")


# task 7
num = int(input("enetr your age :"))
if age>=18 :
    print("adult")
else :
    print("minor")

# task 8
num = int(input("enter a number : "))
if num%2==0 :
    print("the number is even")
if num%2==1 :
    print("the number is odd")

# task 9
marks = int(input("enter marks :"))
if marks>=40 :
    print("pass")
else :
    print("fail")

# task 10
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")

# task 11
marks = int(input("enter marks :"))
marks = 75

if marks >= 90:
    print("A")
elif marks >=75 :
    print("B")
elif marks >= 60:
    print("c")
elif marks >= 40:
    print("d")
else:
    print("F")

# task 12
num = int(input("enter a number :"))
if num >0 :
    print("posititve")
elif num< 0 :
    print("Negativity")
else :
    print("zero")

# task 13
num = int(input("enter a number between 1 to 7 :"))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3 :
    print("Wednesday")
elif num==4 :
    print("thursday")
elif num==5 :
    print("friday")
elif num==6 :
    print("Saturday")
else :
    print("sunday")

# task 14
marks = int(input("Enter student's marks: "))

if marks >= 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


#  task 15
num = int(input("Enter a number: "))

if num == 1:
    print("1")
elif num == 2:
    print("2")
elif num == 3:
    print("3")
else:
    print("Other")

# 16
age = int(input(" enter your age :"))
if age>= 18 :
    if age<=60 :
        print("between 18 and 60")

# task 17
marks = int(input("Enter student's marks: "))
if marks>= 40:
    if marks<=75:
        print("Good")
    else :
        print("passed")
else :
    print("failed")

# task 18
num = int(input("Enter a number: "))
if num>0 :
    if num>100:
        print("GREATERTHAN 100")
    else :
        print("positive number")

# task 19
age = int(input(" enter your age :"))
if age>=18 :
    if age<=60:
        print("adult")
else :
    print("other")

# task 20
num = int(input("enter a number :"))
if num!=0:
    if num>0:
        print("positive")
    else :
        print("negative")
else :
    print("zero")

# task 21
age = int(input(" enter your age :"))
marks = int(input("Enter marks: "))
if age>=18 and marks>=40:
    print("special")
else:
    print("false")

# task 22
num = int(input("enter a number"))
if num<10 or num<100 :
    print("special")

# task 23
age = int(input("enter your age"))
has_id = bool(input("enter a boolean value :"))
if age>=18 and  has_id==True  :
    print("Allowed")
else :
    print("not allowed")

# task 24
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
if num1>10 and num>10 :
    print("Both are greater than 10")

# task 25
num = int(input("enter a number"))
if num<0 or num>100 :
    print("checked")

# task 26
is_closed = bool(input("Enter a boolean value :"))
if  not is_closed :
    print("open")
else :
    print("closed")

# task 27 
num = int(input("enter a number :"))
if num>10 and num<50 :
    print("inside")
else :
    print("outside")

# taskk 28
num = int(input("enter a number :"))
if num>10 or num>50 :
    print("outside")
else :
    print("inside")

# task 29
is_student = bool(input("enter a boolean :"))
has_id = bool(input("enter a boolean :"))
has_ticket = bool(input("enter a boolean value :"))
if is_student and has_id and has_ticket == True :
    print("Allowed")

# task 30
age = int(input("enter an age :"))
marks = int(input("enter marks :"))
has_id = bool(input("enter a boolean value :"))
if age>=18 and marks>=40 and has_id == True :
    print("Eligible")
else :
    print("Not eligible")

# and is appropiate beacuse it shows value is true if all conditions are true otherwise shows false.
