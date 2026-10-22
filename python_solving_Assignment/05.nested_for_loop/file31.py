str = input("Enter the text: ")
for i in range(len(str)):
  for j in range(len(str)):
    char1 = str[i]
    char2 = str[j]
    
    if char1 == char2:
      status = "Same"
    else:
      status = "Different"
      
    print(f"{char1} {char2} is {status}")