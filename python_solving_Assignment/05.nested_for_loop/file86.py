words = input("Enter words: ").split()
palindromes = ""

for word in words:
  if word == word[::-1]:
    if palindromes:
      palindromes += " and "
    palindromes += word

print(f"{palindromes} are palindromes.")