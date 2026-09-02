#Task 17
age = input("Enter your age :" )
print(int(age) >= 18)

# Task 22
age = 25
print(age >= 18  and age <= 60)  # True 

# Task 23
age = 16
print(age < 18 or age > 60)  # True

# Task 24
age = 20
print(not age < 18) 
 # ans is True
# Beacause 20 < 18 is a false statement and not gives the opposite value . so the value is True


# Task 25
a = 21
c = a > 10 and a < 50
print(c)

# Task 26
a = 9
c = a < 10 or a > 100
print(c)


# Task 27
a = 9
c = a < 10 or a > 100
d = not(c)
print(d)

# Task 28 
# 0 is False
# 1 is True
# -5 is True
# "" is False
# "Python" is True
# False is False
# True is True
# None if False



# Task 29
c = bool(0)
print(c)

v= bool(10)
print(v)

e= bool("")
print(e)

l= bool("Hello")
print(e)

m = bool(None)
print(m)



# Task 30
w = 0
print(type(w),bool(0))

c = 1
print(type(c),bool(c))

b = ""
print(type(b),bool(b))

m = "Python"
print(type(m),bool(m))

o = False
print(type(o),bool(o))

k = None
print(type(k),bool(k))


