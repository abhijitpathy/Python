str = input("Enter the text: ")
vowels = "Aeiouaeiou"

for i in range(len(str)):
  char = str[i]
  is_vowel = False
  for j in range(len(vowels)):
    if char == vowels[j]:
      is_vowel = True
      break  
  if is_vowel:
    print(f"{char} = Vowel")
  else:
    print(f"{char} = Consonant")