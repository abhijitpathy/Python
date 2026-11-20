# #05 Python Practice: Strings, for Loops, and while Loops

# #1
# n = input("enter number")
# target = "420"
# found = False
# for i in range(len(n) - len(target) + 1):
#     if n[i:i + len(target)] == target:
#         found = True
#         break

# if found:
#     print("Caught")
# else:
#     print("Escaped")

# #2 Decompress
# n = input("enter text")

# for i in range(0, len(n), 2):
#     ch = n[i]
#     count = int(n[i + 1])

#     for j in range(count):
#         print(ch, end="")
# print()

# #3


# def palindrome(a):
#     n = len(a)

#     if n % 2 == 0:
#         first = a[:n // 2]

#         second = a[n // 2:]
#     else:
#         first = a[:n // 2]

#         second = a[n // 2 + 1:]
        

#     return first == first[::-1] and second == second[::-1]

# print(palindrome("abaccbc"))
# 4
# def whole_pallindrome(s,a):
#      count = 0
#      for i in s:
#         if i == a:
#           count += 1
#      print(count)

# whole_pallindrome("banana","a")
     
     
# # 5
# def reverse_string(s):
#     reverse = ""
#     i = len(s) - 1

#     while i >= 0:
#           reverse += s[i]
#           i -= 1
#     print(reverse)

# reverse_string("abhijit")
# # 6
# def whole_pallindrome(str):
#      str2=""
#      lenght = len(str)
#      for element in range(lenght-1,-1,-1):
#           str2= str2 + str[element]
#      if str2 == str:
#           print("it is pallindrome")
#      else :
#           print("its not pallindrome")
# whole_pallindrome("racecar")

# # # 7
# str = input("enter a string").lower()
# def vowel_count(s):

#      vowel = "aeiou"
#      count =0
#      for i in s:
#          if i in vowel:
#                count +=1
#      print(count)

# vowel_count("hello")


# #8
# string = input("enter a string with alphabets and digits").lower()
# digits = "0123456789"
# count = 0

# for ch in string:
#     for d in digits:
#         if ch == d:
#             count += 1
#             break

# print(count)

# #9
# String= input("enter word")
# character = input("enter your choosen character")

# index = 0

# while string != "":
#     if String[0] == character:
#         print(index)
#         break
#     String = String[1:]
#     index += 1
# else:
#     print(-1)

#10
string = input("enter word")
character = input("enter your choosen character")

result = ""

while string != "":
    if string[0] != character:
        result += string[0]
    string = string[1:]

print(result)


