# Task 1
name = input("Enter your name:")
print(name)
# Task 2
city = input("Enter your city:")
print(f"your city is{city}")

# Task 3
name = input("Enter your name:")
age = input("Enter your age")
print(name,age)

# Task 4
input("Enter your age:")
print( type(input))

#task 5
name = input("Enter you name:" )
print(type(name))

# task 6
first_name = input("Enter  first your name:" )
last_name = input("Enter your last name :")

print(f"My name is {first_name} {last_name}.")

# task 7
name = input("Enter your name:")
city = input("Enter your city:")
college = input("Enter your college:")

print(name,city,college)

#task 8
a,b = input("enter two number:").split()
print(a,b)

# task 9
a = input(" select course :").split()
print(a)

# task 10
a, b, c = input("Enter three words: ").split()

print(a)
print(b)
print(c)

# task 11
a = "25"
b = int(a)
print(b)

# task 12
c= "25.5"
d= float(c)
print(d)

# task 13
h = 100
l = str(h)
print(l)

# task 14
a = int(input("enter a no :"))
print(type(a))

# task 15
b = float(input("enter a float :"))
print(type(b))

# task 16
# a = input()
# b - input()
# print(a +b)
# this produces a string concatenation instead of numeric addition beacuse here the values are string and not in integer

# task 17

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

# task 18
name = "Rahul"
age = 20
print(f" My name is {name} and my age is {age}.")

# task 19
a = 10
b = 20

print(f"sum : {a +b}")

# task 20

name = input("Enter   your name:" )
age = input("Enter your age :")

print(f"My name is {name} and age is  {age}.")

# task 21
price = 28.6970

print(f"Price: {price:.2f}")

# task 22

# :.2f is used to format a number as a floating point value with exactly 2 digits after the point

# task 23
product_name = input("Product_name :")
product_price = input("product_price  :")
quantity = input( "No of product purchased :")

print(f" The product which i have purchased is {product_name}, price is {product_price} and the quantity is {quantity}")

# task 24
# print("a","b","c") will display the values separately in the same line

# task 25
print("2026", "08", "19", sep="-")

# task 26
print("Hello", end=" ")
print("World")

# task 27
a = int(input("Enter first no :"))
b = int(input("Enter second no :"))

print(f"sum : {a + b}")

# task 28
product_name = input("Product_name :")
product_price = input("product_price  :")
quantity = input( "No of product purchased :")
total_expense = float(product_price)*int(quantity)

print(f" The product which i have purchased is {product_name}, price is {product_price} and the quantity is {quantity} , so toal expense is {total_expense}")

# task 29
name = input(" Enter student name :")
age = int(input(" Enter student age :"))
marks = float(input( "Marks obtained by the student :"))

print(f"Name of the student is {name} , age of the student {age} and marks obtained is {marks}.")

# task 30
name = input(" Enter student name :")
age = int(input(" Enter student age :"))
height = float(input( "Height of the student :"))
city = input("Enter student city :")
print(f"Name of the student is {name} , age is {age} ,height is {height:.2f} and his city is {city}.")
