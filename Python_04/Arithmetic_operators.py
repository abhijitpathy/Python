#Task 1
a=5
b=3
print(a+b)
print(a-b)
print(a//b)
print(a/b)
print(a**b)
print(a*b)
print(a%b)

#Task 2
r=2
t=2.3
print(r+t) # 4.3 type=int
print(r-t) # -0.299 type= float
print(r*t) # 4.6 type= float
print(r**t) # 4.9 type=float
print(r%t) # 2.o type=float
print(r/t) # 0.8 type=float
print(r//t)# 0.0 type=float

#Task 3 
physics = 84
math = 88
chem = 90
 # Total marks = Addition of all subjects (262)
print(physics+math+chem)
# tottal marks = 262 out of 300
print((math+physics+chem)/3)
# Average marks = Addition of all subject / total no of subject  (87.33)

#Task 4
product_price = 120
quantity = 30
print(product_price*quantity)
# Total price of all the quantities (3600)

#Task 5
n=4
print(n%2)
# if reminder = 0 then it is a even number
m=3
print(n%2)
# if reminder = 1 then it is a odd number

# task 6
m=13
e=3
print(m/e)
print(m//e)
# division = 4.3333
# floor division = 4
print(-m/e)
print(-m//e)
# division = -4.333
# floor division = -5

# task 7
j=-13
k=-69
print(j+k)
print(j-k)
print(j/k)
print(j*k)
print(j//k)
print(j**k)
print(j%k)

# task 8
m=12
b=4
print(m//b)
print(-m//b)
print(m//-b)
print(-m//-b)
# The negative results are different from simply removing the decimal part becuase in floor division the round up move towards negative infinity from positive infinity

# task 9
c=12
n=19
print(n-c)
print(c-(-n))
print((c)-n)
print((-c)-(-n))


# task 10
z=6
x=9
print(x%z)
print((-x)-z)
print(x%(-z))
print((-x)%(-z))

# task 11
print(10+5*2) # 20
print(20-4/2) #18
print(10+20/5*2) #18
print(2+3*4**2) #50
print(100-20//5) #96
# as the for the sequence python evaluated exponents first then multiplication,division,floor division and then addition subtracts.
# it also starts evaluating from left to right 


#  task 12
print(10+5*2) #20
print((10+5)*2) #30
# here the first solved was the parentheses which chamged the result and we have solve what inside parenthese first
print(20-10/2) # 15
print((20-10)-2) # 8
# here the first solved was the parentheses which chamged the result and we have solve what inside parenthese first
print(2+3*4) #14
print((2+3)*4) # 20
# here the first solved was the parentheses which chamged the result and we have solve what inside parenthese first

 #task 13
r=True
t=False
print(r+t)
print(r-t)
print(r*t)
#print(r/t)
#print(r//t)
#print(r%t)
#print(r**t)
# only addition, subtraction and multiplication works in boolean and all others are errors

# task 14
y=True
u=False
i=5
o=10
print(y+i)
print(u+i)
print(y*o)
print(u*o)
print(y-i)
print(u-i)

# As we know that both True and False have bibary values 1 and 0 respectively

# task 15
m="moon"
l="light"
print(m+l)
# moonlight

# task 16
p="jack"
print(p*4)
# it shows jack written 4 times
 #print(p*4.1)
# it shows type error



# task 17
h="jack"
j="reacher"
print(h+j)
#print(h-j)
print(h*3)
#print(h/j)
# both addition and multiplication are working but subtraction

# task 18
n=None
#print(n+1)
#print(n-2)
#print(n/2)
#print(n//2)
#print(n%2)
#print(n**2)

#task 19
n=10
i=0
# print(10/i) causes zero division error 
o="6"
y="8"
#print(o-y) here  it shows invalid string arithmetic

m=None
l=9
# print(m-l)  it shows type error

# task 20
a=12
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
# addition: 18
# subtraction: 6
# multiplication: 72
# division: 2.0
# floor division: 2
# modulus: 0
# exponential: 2985984

#  task 21

a=10
b=-3
c= 2.5
print(a+b+c) #9.5
print(a-b-c) #10.5
print(a*b*c) #-75.0
print(a/b/c) # -1.3
print(a//b//c) # -2.0
print(a%b%c) # 0.5
print(a**b-c) #-2.499
print((a+b)*c-b) #20.5
print((-a)*(-b)+(-c)) # -32.5
print((a)*(-(b))+c) #32.5

text = "Python"

print(text[::2])
print(text[1::2])
print(text[::-1])
text = "Hello World"

print(len(text))
print(text[5])
print(text[-1])
