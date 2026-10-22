str = input("Enter the text: ")
counted = ""

for i in range(len(str)):
  char = str[i]

  if char not in counted:
    count = 0

    for j in range(len(str)):
      if str[j] == char:
        count += 1

    print(f"{char} = {count}")
    counted += char
