text = input("Enter string with digits: ")

# Extract digits
digits = ""
for ch in text:
  if ch >= "0" and ch <= "9":
    digits += ch

print(f"Extracted digits: {digits}")
print("Digit Pair Classifications:")

# Nested loops to generate and classify every ordered pair
for i in range(len(digits)):
  for j in range(i + 1, len(digits)):
    d1 = digits[i]
    d2 = digits[j]
    
    # Classification logic based on values
    if d1 == d2:
      status = "Equal"
    elif d1 < d2:
      status = "Ascending (Smaller first)"
    else:
      status = "Descending (Larger first)"
      
    print(f"({d1}, {d2}) -> {status}")