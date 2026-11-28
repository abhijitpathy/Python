# 1
add = lambda a,b:a+b
print(add(10,20))

# 2
square = lambda e : e**2
print(square(6))
# 3
cube = lambda q:q**3
print(cube(3))
# 4
odd_even = lambda x:"even" if x%2 ==0 else"odd"
print(odd_even(7))
# 5
greater = lambda a,b: a if a>b else b
print(greater(45,32))
# 6
to_farhneit = lambda c: (c*9/5)+32
print(to_farhneit(25))
# 7
lenght = lambda s:len(s)
print(lenght("python"))
# 8
capital = lambda u : u.upper()
print(capital("hello")) 
# 9
last_ch = lambda s:s[-1]
print(last_ch("coding"))
# 10
final_price = lambda price,discount:price - (price*discount/100)
final_price(1000,10)