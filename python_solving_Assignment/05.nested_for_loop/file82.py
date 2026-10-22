str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

for char in str1:
  str2 = str2.replace(char, "", 1)

if len(str2) == 0:
  print("Anagram")
else:
  print("Not Anagram")