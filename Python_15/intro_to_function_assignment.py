# Basic lvl
#1
def greet():
    print("Hello python !")
greet()

#2
def show_name():
    print("Abhijit")
show_name()
show_name()
show_name()

#3
def print_line():
    print("----------------------------------------")
print_line()
print("Heading")
print_line()

#4
def show_rules():
    print("keep silence")
    print("have dicipline")
    print("be attentive")

show_name()

#5
def show_square():
    for i in range(4):
        for j  in range(4):
            print("*",end=" ")
        print()

show_square()

#6
def show_menu():
    print("Settings")
    print("apps")
    print("login")

show_menu()
show_menu()
show_menu()
#7
def morning_message():
    print("good morning")
def evening_message():
    print("good evening")

evening_message()
morning_message()

#8
def show_student_card():
    print("Heading")
    print("Alex")
    print("12")

show_student_card()

#9
def print_numbers():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)

print_numbers()
print_numbers()

#10
def show_patterns():
    for i in range(1,4):
        for j in range(1,i+1):
            print("*",end="")
        print()

show_patterns()
show_patterns()

#11
def show_header():
    print("header")
def show_body():
    print("body")
def show_footer():
    print("footer")

show_header()
show_body()
show_footer()


#12
def show_separator():
    print("===============")

show_header()
print("===============")
show_body()
print("===============")
show_footer()

#13
def step_one():
    print("step_1")
def step_two():
    print("step_2")
def step_three():
    print("step_3")

step_three()
step_one()
step_two()

#14
def show_table_heading():
    print("column heading")
def show_table_r1():
    print("student row 1")
def show_table_r2():
    print("student row 2")

show_table_heading()
show_table_r1()
show_table_r2()

#15
def pattern():
    print("*****")
pattern()
pattern()
pattern()
pattern()

#16
def show_welcome():
    print("wellcome to xyz learning to learn python ")

show_welcome()

#17 
def show_help():
    print("1 for addition")
    print("2 for subtraction")
    print("3 for Division")
    print("4 for multiplication")
show_help()

#18
def receipt_start():
    print("welcome to shopsy")
def receipt_end():
    print("Thank you for shopping with us")
receipt_start()
receipt_end()

#19
def print_box():
    print("welcome to xyz Ai")
    print("here we have features")
    print("enjoy the features")
print_box()

#20
def program_title():
    print("welcome to codinggita Annual festival")
def program_menu():
    print('''event
    dinner''')
def program_end():
    print("thank you for visiting codinggita")

program_title()
program_menu()
program_end()

#21
def greet():
    print("hello")
greet()

#22
def welcome():
    print("welcome")
welcome()

#23
# show()

# def show():
#     print("Hello")

# this shows error because here we are calling the function before we declare it and python doest support hoisting so this shows an error

# correct code

def show():
    print("hello")

show()

#24
# def print_report():
#     print("Report")

# Print_Report()

# in this code during calling the function there is a spelling mistake and python is case sensitive so it shows a error

def print_report():
    print("Report")

print_report()

#25
def a():
    print("A")

def b():
    print("B")

a()
b()
a()

# output ABA beacuse after declaring functions we can call them in any sequence and python doest show any error

# 26
def message():
    print("Python")

message()
message()
message()
message()

# the fuction body run for 4 times

#27
def example():
    print("One")
    print("Two")

print("Three")

# here print("one") and print("two") are within the function body
#28

def _f():
    print("Rename the following functions clear snake_case")

def do_task():
    print("tasks to complete")
def student_details():
    print("Name of the student")
def x_one():
    print('''1 for dine in
    2 for takeaway''')

_f()
student_details()
x_one()
do_task()

#29
def defi_one():
    print("defining function one")
def defi_two():
    print("defining function two")

defi_one()
#output here only the first function get recalled and prints defining function one

#30
def addition(a,b):
    print(a+b)

print("a msg outside the function")
addition(12,13)
print("called the function addition above")


## 14
#1
# What is a function?  # a function is a block of code which is recalled when needed

#2 why do we use functions ? # we use functions for better code readibility, to recall the function we needed , it gives better time complexity and space complexity

#3 what is code reuse ? # to use a code a specific code again and again we can make it easy by defining the the code as function

#4 does defining a function automatically execute its body ? # no we need to recall the function to execute it

#5 what does def do ? # def is a keyword which defined our function 

#6 what is a function body ? # a function body s a place we write the code inside the function

#7  why is identation important? # indentation is important becuase it  defined whether a code is inside the block or not 

#8 what is defining and caslling a function ? # defining a function means to set a block of code into function and calling them means to call the defined function when needed . 
# without calling the function does't execute


#9 how do you call a function named display_menu?  # display_menu()

#10 why should function name describe their task ?  # becuase by defining the name according to function its easier to understand what does the function does and why we are recalling the function 

#11 what naming style is commonly used for python functions?  # snake_case is used for naming a function

#12 What happens if a function is called before its definition has executed in a normal script?  # the called function does't get executed as python does't support hoisting and python reads the calling first then the defining which get resulted to error


#13 how many times does a function body runs if it is called four times?  # it runs for 4 times

#14 is print_Total a valid python function name? is it the usual style?  # no it is not valid as its not in snake_case the corrected function name is print_total

#15 why might a function make a program easier to maintain? # beacuse in a regular code we have to redifine the values again and again and then print them which takes much space we can solve this by making a function which is good for redability and its also easier to reassign values insie the function 