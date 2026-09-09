#1
num = int(input("enter a num :"))
if num >0:
    print("num is positive")
elif num<0:
    print("num is negative")
else :
    print("num is zero")

#2
num = int(input("enter a num : "))
if  num > 0 and num % 2 == 0:
    print("positive even")
elif num >0 and num % 2 == 1:
    print("positive odd")
elif num<0 and num % 2 ==0:
    print("negative even")
elif num<0 and num% 2 ==1:
    print("negative odd")
else :
    print("num is zero")

#3
num1 = int(input("enter 1st num :"))
num2 = int(input("enter 2nd num :"))
if num1>num2 :
    print("num1 is greater")
elif num2>num1:
    print("num2 is greater")
else :
    print("both are equal")
#4
num1 = int(input("enter 1st num :"))
num2 = int(input("enter 2nd num :"))
num3 = int(input("enter 3rd num :"))
if num1<num2 and num1 < num3:
    print("num1 is the samallest")
elif num2<num1 and num2<num3:
    print("num2 is the smallest")
elif num3<num1 and num3<num2:
    print("num3 is the smallest")
else :
    print("all the numbers are equal")

#5
num1 = int(input("enter 1st num :"))
num2 = int(input("enter 2nd num :"))
num3 = int(input("enter 3rd num :"))
if num1>num2 and num1 > num3:
    print("num1 is the larger")
elif num2>num1 and num2>num3:
    print("num2 is the larger")
elif num3>num1 and num3>num2:
    print("num3 is the larger")
else :
    print("all the numbers are equal")

#6
num = int(input("enter a num :"))
if num % 5 == 0 and num % 11 == 0 :
    print("number is divisible by both")
elif num % 5==0 :
    print("number is only  divisible by 5 ")
elif num % 11 == 0:
    print("number is only divisible by 11")
else :
    print("num is not divisible by both 5 and 11")

#7
num = int(input("enter a num :"))
if num % 3 == 0 and num % 7 == 0 :
    print("number is divisible by both")
elif num % 3==0 :
    print("number is only  divisible by 3 ")
elif num % 7 == 0:
    print("number is only divisible by 7")
else :
    print("num is not divisible by both 3 and 7")

#8
marks = int(input("enter your marks :"))
if marks <100 and marks>= 40 :
    print("pass")
elif marks<= 40 and marks>0 :
    print("fail")
else:
    print("invalid")                                                                   

#9
marks = int(input("enter your  marks :"))
if marks<=100 and marks>=90:
    print("A")
elif marks<=89 and marks>80:
    print("B")
elif marks<=79 and marks>70:
    print("C")
elif marks<=69 and marks>60:
    print("D")
elif marks<=59 and marks>40:
    print("E")
elif marks<40 and marks>0:
    print("fail")
else:
    print("invalid marks ")


#11
year = int(input("enter year :"))
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print("leap year")
else:
    print("normal year")

# 12
v = input(" Take a character :")

if v>= 'A' and v<=  'Z':
    print("character is upper case")
elif v>= 'a' and v<= 'z':
    print("character is a lower case")
elif v>='0' and v<='9' :
    print("character is a digit")

else:
    print("character is  special")

#13
c = input("Enter a character: ")
c = c.lower()

if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
    print("Vowel")


elif (c == "b" or c == "c" or c == "d" or c == "f" or c == "g" or
      c == "h" or c == "j" or c == "k" or c == "l" or c == "m" or
      c == "n" or c == "p" or c == "q" or c == "r" or c == "s" or
      c == "t" or c == "v" or c == "w" or c == "x" or c == "y" or c == "z"):
    print("Consonant")

else:
    print("Invalid input")
    
#14
cost = int(input("enter cost price :"))
sell = int(input("enter selling price :"))
if cost < sell :
    print("profit")
elif cost>sell :
    print("loss")
else :
    print("no profit and no loss")

# 15
cost = int(input("enter cost price :"))
sell = int(input("enter selling price :"))
if cost<sell:
    profit = sell - cost
    profit_percentage = (profit/cost)*100
    print("profit_percentage =",profit_percentage)
elif sell<cost:
    loss = cost - sell 
    loss_percentage = (loss/cost)*100
    print("loss_percentage=",loss_percentage)
else :
    print("invalid price ")

# 16 
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Electricity bill =", bill)


#17
operation = int(input("enter the following operation u want to do : 1 for Addition , 2 for subtraction , 3 for multiplication , 4 for dividion  : "))
if operation==1 or operation == 2 or operation ==3 or operation==4:
    a=int(input("enter first number :"))
    b=int(input('enter second value :'))
    if operation==1:
        print(a+b)
    elif operation==2:
        print(a-b)
    elif operation==3:
        print(a*b)
    elif operation==4:
        print(a/b)
else :
    print("choose valid option")

#18
temp = int(input("enter temp :"))
if temp<0 :
    print("tempreture is freezing")
elif temp==0 and temp<=15:
    print("very cold")
elif temp>=16 and temp<=25 :
    print("cold")
elif temp>=26 and temp<=35:
    print("Normal")
else :
    print("hot") 


#19
num = int(input("enter num :"))
if num<0 :
    print("Negative")
elif num>=0 and num<=10:
    print("belongs between 0 to 10")
elif num>=11 and num<=50 :
    print("belongs between 11 to 50")
elif num>=51 and num<=100 :
    print("belongs between 51 to 100")
else :
    print("above 100")

# 20
s1 = int(input("enter first side lenght :"))
s2 = int(input("enter second side lenght :"))
s3 = int(input("enter third side lenght :"))
if (s1 + s2 > s3) and (s1 + s3 > s2) and  (s2 + s3 > s1):
    print("triangle is valid ")
else :
    print("traingle is invalid")


# 21
s1 = int(input("enter first side lenght :"))
s2 = int(input("enter second side lenght :"))
s3 = int(input("enter third side lenght :"))
if (s1 + s2 > s3) and (s1 + s3 > s2) and  (s2 + s3 > s1):
    print("triangle is valid ")
    if s1==s2==s3 :
      print("it is a equilateral traingle")
    elif ((s1==s2 and s2!=s3) or (s1==s3!=s2 and s2==s3!=s1)):
      print("traingle is isosceles")
    elif s1!=s2!=s3:
      print("traingle is scalene")
else :
    print("traingle is invalid")

#22
account_balance = int(input('enter balance :'))
withdrawl_ammount = int(input("enter withdrawl ammount :"))
if withdrawl_ammount<0 :
   print("invalid put correct withdrawl ammount")
elif withdrawl_ammount % 100 !=0 :
   print("invalid withdrwal_ammount is not divisible by 100 put correct value!!")
elif withdrawl_ammount > account_balance :
   print("invalid withdrawl_ammount cannot be greater than balance")
elif account_balance - withdrawl_ammount < 500:
    print("Invalid: At least ₹500 must remain after withdrawal.")
else:
   account_balance = account_balance - withdrawl_ammount
   print("Withdrawal successful")
   print("remaining balance:", account_balance)

#23
username = input("enter username :")
username = username.strip()
password = input("enter password :")
if username=="admin":
    print("login successful")
    if password == "python123":
        print("correct password")

    else :
        print(" wrong password ")

else :
    print("username not found")

#24
amount = int(input("Purchase: "))

if amount < 500:
    discount_percent = 0
elif amount < 1000:
    discount_percent = 5
elif amount < 2000:
    discount_percent = 10
elif amount < 5000:
    discount_percent = 15
else:
    discount_percent = 20

discount_amount = amount * discount_percent / 100
final_amount = amount - discount_amount

print(f"Original amount: {amount}")
print(f"Discount: {discount_percent}%")
print(f"Discount amount: {discount_amount}")
print(f"Final amount: {final_amount}")

#25
marks1 = int(input("enter first subject marks :"))
marks2 = int(input("enter second subject marks :"))
marks3 = int(input("enter third subject marks : "))
#for marks1
if marks1>= 0 and marks1<=100:
    print("correct values")
    if marks1>=35:
      print("pass in subject 1")
    elif marks1<35:
      print("fail in subject 1 ")
else:
   print("invalid values")
#for marks2
if marks2>= 0 and marks2<=100:
    print(" correct values")
    if marks2>=35:
      print("pass in subject 2")
    elif marks2<35:
      print("fail in subject 2 ")
else:
   print("invalid values")
# for marks3
if marks3>= 0 and marks3<=100:
    print(" correct values")
    if marks1>=35:
      print("pass in subject 3")
    elif marks1<35:
      print("fail in subject 3 ")
else:
   print("invalid values")
#for calculating average
average = (marks1 + marks2 + marks3)/3
if average>=75 and average<=100:
   print("Distinction")
elif average>=60 and average<=74:
   print("first class")
elif average>=50 and average<=59:
   print("second class")
elif average>=35 and average<=49:
   print("pass")
else:
   print("you are failed")


#26
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid")

elif day < 1:
    print("Invalid")

elif month == 2:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        if day <= 29:
            print("Valid")
        else:
            print("Invalid")
    else:
        if day <= 28:
            print("Valid")
        else:
            print("Invalid")

elif month == 4 or month == 6 or month == 9 or month == 11:
    if day <= 30:
        print("Valid")
    else:
        print("Invalid")

else:
    if day <= 31:
        print("Valid")
    else:
        print("Invalid")

# 27
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Valid time")
else:
    print("Invalid time")


# 28
person1 = int(input("enter 1st age :"))
person2 = int(input("enter 2nd age :"))
person3 = int(input("enter 3rd age :"))
if person1<person2 and person1 < person3:
    print("person1 is the samallest")
elif person2<person1 and person2<person3:
    print("person2 is the smallest")
elif person3<person1 and person3<person2:
    print("person3 is the smallest")
elif person1 == person2 == person3 :
    print("all persons are of same age")

else :
    if (person1 == person2) :
       print("person 1 and person2 are of same age")
    elif (person2 == person3):
      print("person2 and person3 are of same age")
    elif (person3 == person1):
        print("person3 and person1 are of same age")


#29
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
num3 = int(input("enter third number :"))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    print("num1 is middle one")

elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print("num2 is middle one")

elif (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):
    print("num3 is the middle one")

else:
    print("all the numbers are same")


#30
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))
attendance = int(input("Enter attendance percentage: "))

if 18 <= age <= 25 and marks >= 85 and attendance >= 75 and income <= 300000:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")


