# 1 sum of digits at even position
def sm_digits(n):
    if n<10:
        return 0
    return (n//10)%10+sm_digits(n//100)
print(sm_digits(583246))

# 2 Reverse a number without converting it to a string
def reverse_nm(n,back=0):
    if n==0:
        return back
    return reverse_nm(n//10,back*10+n%10)
print(reverse_nm(4827))
# 3 check wether is it a pallindrome
def is_pallindrome(string,i=0):
    if i >=len(string)//2:
        return True
    if string[i] != string[-1-i]:
        return False
    return is_pallindrome(string,i+1)
print(is_pallindrome("level")) 

# 4 count a character in a string
def ch_s(s, ch):
    if s == "":                          
        return 0
    if s[0] == ch:
        return 1 + ch_s(s[1:], ch) 
    else:
        return ch_s(s[1:], ch) 
print(ch_s("programming","m"))

# 5 gcd
def gcd(a,b):
    if b ==0:
        return a
    return gcd(b,a%b)
print(gcd(48,18))

# 6 check whether it is a prime number
def is_prime(n,i=2):
    if i*i>n:
        return True
    if n%i ==0:
        return False
    return is_prime(n,i+1)
print(is_prime(29))

# 7 Remove all occurence of a character
def remove_ch(s,ch):
    if s =="":
        return ""
    if s[0] == ch:
        return remove_ch(s[1:],ch)
    return s[0]+ remove_ch(s[1:],ch)
print(remove_ch("misisippi","s"))

#8 Convert a decimal number into binary
def binary(n):
    if n==0:
        return "0"
    if n==1:
        return "1"
    return binary(n//2)+ str(n%2)
print(binary(13))
   