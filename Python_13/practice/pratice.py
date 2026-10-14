#secA
#1
for i in range(1, 5):
    if i == 1:
        break
    print(i)

print("End")
#  End
#2
for i in range(1, 7):
    print(i)
    if i == 4:
        break
print("Finished")
#  1234 finished 
#3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#  1245
#4
for i in range(1, 5):
    if i == 2:
        pass
    print(i)
#  1234
#5 
for i in range(3):
    print("Python")
else:
    print("Done")
# python python python done

#SECb

#6
for i in range(1, 5):
    print("A", i)
    if i == 3:
        break
    print("B", i)
#  A1B1 A2 B1B2 A3
#7 
for i in range(1, 5):
    if i == 2:
        continue
    print("Value:", i)
    print("Next line")
# value:1 Next line value:3 Next line value:4 Next line 
#8 
for i in range(1, 4):
    if i == 2:
        pass
        print("Inside if")
    print("Outside if", i)
#  Outside if 1
# Inside if
# Outside if 2
# Outside if 3
#9 
for i in range(2, 8, 2):
    print(i)
    if i == 4:
        break
    print("Hello")

print("After loop")
# 2 hello 4 After loop
#10 
for i in range(1, 5):
    print("Start", i)
    if i == 3:
        continue
    print("End", i)
# start 1 end 1 start 2 end 2 start 3 start 4 end 4

# sec 3


#11
for i in range(2, 5):
    print(i)
else:
    print("Loop completed")
#  234 loop completed
#12 
for i in range(1, 6):
    if i == 4:
        break
    print(i)
else:
    print("Completed")
print("Program end")
# 123 program end
#13 
for i in range(1, 5):
    if i % 2 == 0:
        continue
    print(i)
else:
    print("Completed")
# 13 completed
#14
for i in range(5, 5):
    print(i)
else:
    print("Else executed")
#  else executed
#15
for letter in "CODE":
    print(letter)
    if letter == "D":
        break
else:
    print("All letters checked")
#  coD
#16 
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
else:
    print("Finished normally")
# 123 finished normally
#17
word = "banana"

for ch in word:
    if ch == "n":
        print("Found")
        break
else:
    print("Not found")
#  found
#18
word = "apple"

for ch in word:
    if ch == "z":
        print("Found")
        break
else:
    print("Not found")
#  Not found


#Sec D


#19 
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")
print()
# dctn
#20 
for ch in "programming":
    if ch == "g":
        break
    print(ch, end="-")
# pro
#21
for ch in "computer":
    if ch == "o":
        continue
    if ch == "t":
        break
    print(ch, end="")
#  cmpu
#22
for ch in "cat":
    if ch == "a":
        pass
    print(ch.upper(), end=" ")
#  CAT

#SEC E


#23
n = 1

while n <= 5:
    print(n)
    if n == 3:
        break
    n += 1

print("Stopped")
#  123 stopped
#24 
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)
# 1245
#25
n = 1

while n <= 5:
    if n == 2:
        n += 1
        continue
    print(n)
    n += 1
#  1345
#26 
n = 1

while n <= 4:
    if n == 3:
        break
    print(n)
    n += 1

print(n)
# 12
#27 
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)
#  1,1  1,2 2,1  2,2  3,1  3,2 
#28 
for row in range(1, 3):
    for col in range(1, 4):
        if col == 2:
            continue
        print(row, col)
#  1,1  1,3  2,1  2,3  
#29
for i in range(1, 4):
    print("Outer", i)
    for j in range(1, 4):
        if j == 2:
            break
        print("Inner", j)
#  outer 1 , inner 1 
# outer 2 , inner 1
# outer 3 ,  inner 1

#30 
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)
    else:
        print("Inner else", i)
# 1,1 2,1 3,1 1,3 
#31 
for i in range(1, 3):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)
    else:
        print("Inner loop complete")
# 1,1  2,1 2,3 inner loop completed

#32 
for i in range(1, 7):
    if i == 2:
        continue
    if i == 5:
        break
    print(i)
else:
    print("Loop else")
print("End")
# 134 End

#33 
for i in range(1, 5):
    if i == 3:
        pass
    else:
        print("Else block", i)
    print("Number", i)
# else block 1 , number 1 ,   else block , 2 ,   number,2   number, 3  else block 4   number,4

#34
for i in range(1, 5):
    print("X", end="")
    if i == 2:
        continue
    print("Y", end="")
print("Z")
#  x y
#x
# xy
# xy z

# 35 
for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")
#   1 2 outside



