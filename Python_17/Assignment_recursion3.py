#1 print a message N times
def msg_Print(n):
    if n==3:
        return "hello"
    print("hello")
    return msg_Print(n+1)
print(msg_Print(1))

# 2 print even numbers from 2 to N
def even_numb(n):
    if n<2:
        return
    even_numb(n-1)
    if n%2 ==0:
        print(n)
(even_numb(10))

# 3 sum of odd numbers from 1 ro N
def sum_odd(n):
    if n <=0:
        return 0
    if n%2!=0:
        return n+ sum_odd(n-1)
    return sum_odd(n-1)
print(sum_odd(7))

# 4 count how many times a digit appear
def count_number(number,target):
    if number <10:
        if number == target:
            return 1
        return 0
    last_digit = number %10
    if last_digit == target :
        return 1 + count_number(number//10,target)
    return count_number(number//10,target )
print(count_number(52525,5))
# 5 find the product of digits
def product_digits(n):
    if n <10:
        return n
    return n%10 * product_digits(n//10)
print(product_digits(234))
# 6 find the first digit of a number
def first_digit(n):
    if n<10:
        return n
    return first_digit(n//10)
print(first_digit(5837))
# 7  check wether a number or a digit
def contains_digits(number,target):
    if number %10 == target:
        return True
    if number<10:
        return False
    return contains_digits(number//10,target)
print(contains_digits(4826,8))
# 8 calculate lenght of a string
def string_lenght(s,count=0,n=""):
    if n ==s:
        return count
    return string_lenght(s,count+1,n+s[count])
print(string_lenght("coding"))
# 9 count vowels in a string
def count_vowels(s, i=0):
    if i == len(s):
        return 0
    return (1 if s[i] in "aeiou" else 0) + count_vowels(s, i + 1)

print(count_vowels("education"))  
# 10 check whether a string is a pallindrome
def is_pallindrome(string,i=0):
        if i >=len(string)//2:
            return True
        if string[i] != string[-1-i]:
            return False
        return is_pallindrome(string,i+1)
print(is_pallindrome("level"))

        
    


