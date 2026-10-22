str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Common characters include", end="")

for i in range(len(str1)):
  char = str1[i]

  for j in range(len(str2)):
    if str1[i] == str2[j]:
      print(f" {char}", end="")
      break  