#problem 1
num1 = int(input("enter number :"))
num2 = int(input("enter number :"))
if num1>num2:
    print("num1 is greater than num2")
else :
    print("num2 is greater than num1")

#problem 2
marks = int(input("enter marks :"))
if marks >=90 and marks<100 :
    print("A")
elif marks >=75 and marks<=89:
    print("B")
elif marks >=50 and marks<=74:
    print("C")
elif marks <50 and marks>=0 :
    print("fail")
else :
    print("invalid marks !!")

#problem 3
l = int(input("enter lenght :"))
b = int(input("enter width :"))
area = l * b 
print(area)
perimeter = 2*l + 2*b
print(perimeter)

#problem 4

num = int(input("enter a number :"))
if num>0 :
    print("positive")
elif num<0 :
    print("negative")
else:
    print("number is zero")


#problem 5
price1 = int(input("enter the price of item :"))
if price1 >=1000:
    discount_percentage = 10
    discount = price1 * 10/100
    final_price = price1 - discount 
    print(final_price)
else :
    print("item price is less than 1000")

#problem 6
num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))
sum = num1 + num2
print(sum)


# problem 7
num = int(input("enter number 1 :"))
if num%2 == 0:
    print("num is even")
elif num%2 == 1:
    print("num is odd")
else:
    print("no is zero")

#problem 8
num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))
num3 = int(input("enter number 3 :"))
if num1>num2 and num1>num3 :
    print("num1 is greater")
elif num2>num1 and num2>num3:
    print("num2 is greatest")
elif num3>num1 and num3>num2 :
    print("num3 is greatest")
else :
    print("all no are same")

#problem 9
age = int(input("enetr your age :"))
if age>=18 :
    print("eligible to vote")
else :
    print("not eligible to vote")

#problem 10
price1 = int(input("enter the price of item :"))
if price1 >=2000:
    discount_percentage = 20
    discount = price1 * 20/100
    final_price = price1 - discount 
    print(final_price)
else :
    print("item price is less than 2000")

#problem 11
#25
marks1 = int(input("enter first subject marks :"))
marks2 = int(input("enter second subject marks :"))
marks3 = int(input("enter third subject marks : "))
#for marks1
if marks1>= 0 and marks1<=100:
    print("correct values")
    if marks1>=40:
      print("pass in subject 1")
    elif marks1<40:
      print("fail in subject 1 ")
else:
   print("invalid values")
#for marks2
if marks2>= 0 and marks2<=100:
    print(" correct values")
    if marks2>=40:
      print("pass in subject 2")
    elif marks2<40:
      print("fail in subject 2 ")
else:
   print("invalid values")
# for marks3
if marks3>= 0 and marks3<=100:
    print(" correct values")
    if marks1>=40:
      print("pass in subject 3")
    elif marks1<40:
      print("fail in subject 3 ")
else:
   print("invalid values")
#for calculating average
average = (marks1 + marks2 + marks3)/3
if average >=40:
   print("pass")
elif average >100:
   print("invalid")
else:
   print("you are failed")