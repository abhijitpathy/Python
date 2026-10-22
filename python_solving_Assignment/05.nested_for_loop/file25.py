s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = ""

for i in s1:
    for j in s2:
        if i == j:
            result += i

print(len(result))

