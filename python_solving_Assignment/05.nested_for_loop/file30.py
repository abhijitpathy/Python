str = input("Enter the text: ")

for i in range(len(str)):
  for j in range(len(str)):
    if i != j:
      print(f"{str[i]} {str[j]}")