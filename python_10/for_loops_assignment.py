# #1Q printing hello
for i in range(5):
    print("Hello")

# #2Q printing no upto 9
for i in range(0,10):
    print(i)

# #3Q printing no from 0 to 10
for i in range(1,11):
    print(i)

# #4Q printing in reverse
for i in range(10,0,-1):
    print(i)

#5Q the numbers from 5 to 50, increasing by 5.
for i in range(5,55,5):
    print(i,end=" ")

#6Q  even numbers from 2 to 20 using range().
for i in range(1,21):
    if i % 2 ==0:
        print(f"{i} is even,",end=" ")

#7Q all odd numbers from 1 to 19 using range()
for i in range(1,20):
    if i % 2 ==1:
        print(f"{i} is odd,",end=" ")

#8Q 3 6 9 12 15 18 using range()
for i in range(3,20,3):
    print(i,end=" ")

#9Q the numbers from 20 down to 2, decreasing by 
for i in range(20,0,-2):
    print(i,end=" ")

#10Q a positive integer n from the user and print all numbers from 1 to n.
n = int(input("enter  number :"))
for i in range(1,n+1):
    print(i,end=" ")

#11Q  Take n from the user and print only the even numbers from 1 to n.
n = int(input("enter  number :"))
for i in range(1,n+1):
    if i %2 ==0:
        print(f"{i} is even,",end=" ")

#12Q  Take n from the user and print only the odd numbers from 1 to n.
n = int(input("enter  number :"))
for i in range(1,n+1):
    if i %2 ==1:
        print(f"{i} is odd,",end=" ")

 #13Q Take n from the user and print all numbers from 1 to n that are divisible by 3.
n = int(input("enter  number :"))
for i in range(1,n+1):
    if i % 3 ==0:
        print(f"{i} is divisible by 3,",end=" ")

#14Q Take n from the user and print all numbers from 1 to n that are divisible by both 2 and 3
n = int(input("enter  number :"))
for i in range(1,n+1):
    if i %2 ==0 and i % 3 == 0:
        print(f"{i} is divisible by both 2 & 3,",end=" ")

# #15Q Take n from the user and count how many numbers from 1 to n are even
n = int(input("enter number :"))
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1

print("Number of even numbers:", count)

# # 16q 1 + 2 + 3 + ... + n
 #using a for loop.
n = int(input("Enter n: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum =", sum)

# #17q take n from the user and calculate the sum of all even numbers from 1 to n
n = int(input("Enter num: "))
sum_even = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers =", sum_even)

# #18q Take n from the user and calculate the sum of all odd numbers from 1 to n
n = int(input("Enter num: "))
sum_odd = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        sum_odd += i

print("Sum of odd numbers =", sum_odd)

#19q Take a number from the user and print its multiplication table from 1 to 10
n = int(input("enter number:"))
for i in range(1,11):
    print(n*i,end=" ")

#20q 1 × 2 × 3 × ... × n
 # using a for loop.
n = int(input("Enter n: "))
multiply = 1

for i in range(1, n + 1):
    multiply *= i

print("Product =", multiply)

# #21Q take a string from the user and print each character on a separate line
l = input("enter characters :")
for character in l:
    print(character)

# #22Q Take a string from the user and print all its characters on the same line using end=""
l = input("enter characters :")
for character in l:
    print(character,end=" ")

# #23Q Take a string from the user and count the number of characters in it using a for loop
word = input("enter characters:")
count = 0
for character in word:
    count = count + 1

print("Characters:", count)

# #24Q Take a string from the user and count how many times the character "a" appears
word = input("enter characters :")
count = 0
for character in word:
    if character == "a":
        count = count + 1

print("Count:", count)

# #25Q Take a string from the user and count how many characters are uppercase letter
text = input("Enter a string: ")
count = 0
for character in text:
    if character.isupper():
        count += 1

print("Number of uppercase letters =", count)

# #26 
# Use nested loops to print:

# ****
# ****
# ****
for row in range(3):
    for column in range(4):
        print("*", end="")
    print()

# #27Q 
# Use nested loops to print:

# *****
# *****
# *****
# *****
for row in range(4):
    for coloumn in range(4):
        print("*",end="")
    print()

# #28Q
28.
# Print the following pattern:

# *
# **
# ***
# ****
# *****
for row in range(1,6):
    for column in range(1,row+1):
        print("*",end="")
    print()

# #29Q 
# Print the following pattern:

# 1
# 12
# 123
# 1234
# 12345
for row in range(1,6):
    for column in range(1,row+1):
        print(column,end="")
    print()


# #30Q Create a multiplication-table grid using nested for loops.
#For example, for numbers 1 to 5, produce rows showing their multiplication results.
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()


# #final one 
# Take a number n from the user and print:

# 1
# 12
# 123
# 1234
# ...
# until the last row contains n numbers.
n = int(input("enter number :"))
for row in range(1,n):
    for column in range(1,row+1):
        print(column,end="")
    print()