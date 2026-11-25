# 1
def show(n):
    if n == 0:
        print("Stop")
        return

    print(n)
    show(n - 1)
    print(n)

show(2)
#  2 1 stop 1 2
# here the function calls 2 and the condition goes false so then it prints 2 and calls (2-1=1) and thwn it calls 1 and then stop after that the value returns to from where the function is called so it returns to show(1) and it prints 1 and then 2 just like that

# 2
def total(n):
    if n == 0:
        return 0

    return n + total(n - 1)
# in this function the base case is the if n ==0 return 0 it stops recursion beacuse if the condition beacomes true then it returns 0 to the function where it had been called and just like that it completes the recursion cycle
# 3

# def count(n):
#     if n == 0:
#         return

#     count(n + 1)

# in this case the recursive case is the bugged one where the count is keep on increasing instead of decreasing due to which the base case will never satisfy and also its beign called from 2 not from negative numbers

def count(n):
    if n == 0:
        return

    count(n - 1)
# 4
# def answer(n):
#     if n == 0:
#         return 0

#     n + answer(n - 1)

# print(answer(3))
# here it will show error beacuse the recursive case doest have a return in it so it will never go to where from it had called and if it got corect then the answer will be 6
def answer(n):
    if n == 0:
        return 0

    return n + answer(n - 1)

print(answer(3))

# 5
def show(n):
    if n ==0:
        print("Done!")
        return
    print(n)
    show(n-1)
show(3)

# 6
def show(n):
    if n ==4:
        print(4)
        return
    print(n)
    show(n+1)
show(1)
# 7
def sum_to(n):
    if n == 0:
        return 0

    return n + sum_to(n - 1)

print(sum_to(4))
# 8
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(4))

# 9
def digit_sum(n):
    if n <10:
        return n 
    return n % 10 + digit_sum(n//10)
print(digit_sum(583))
print(digit_sum(7))
print(digit_sum(0))

# 10
def power(a, n):
    if n == 0:
        return 1

    return a * power(a, n - 1)

print(power(2, 5))
print(power(9,0 ))
print(power(3,1))
#
# 11
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
print(count_digits(5382))  
print(count_digits(6))     
print(count_digits(0))     
# 12
def reverse_text(text):
    if text == "":
        return ""
    return text[-1] + reverse_text(text[:-1])
print(reverse_text("cat"))
print(reverse_text("a"))   
print(reverse_text(""))     
# 13
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
print(fibonacci(0))  
print(fibonacci(1))  

# 14
def max_digit(n):
    if n < 10:
        return n

    last = n % 10
    remaining = max_digit(n // 10)

    if last > remaining:
        return last
    else:
        return remaining
print(max_digit(4729))  
print(max_digit(555))  
print(max_digit(0))     

# 15
def mystery(n):
    if n <= 1:
        return n

    return mystery(n - 1) + mystery(n - 2)
print(mystery(0)) #0
print(mystery(1)) #1
print(mystery(2)) #1

# 16
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 17
def stop_at_zero(n):
    if n == 0:
        return
    stop_at_zero(n - 1)

# 