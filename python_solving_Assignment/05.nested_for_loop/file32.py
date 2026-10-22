str = input("Enter the text: ")
vowels = "AEIOUaeiou"

for i in range(len(str)):
  char1 = str[i]
  for j in range(len(str)):
    char2 = str[j]
    if char1 in vowels and char2 not in vowels:
      print(f"{char1}-{char2}")