matrix = int(input("enter no of rows"))
even = odd = positive = negative = zero = 0
largest = 0
for i in range(1,matrix+1):
    for j in range(1,matrix+1):
        n = int(input("Enter elements: "))

        if n % 2 == 0:
            even += 1
        else:
            odd += 1

        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            zero += 1

        if largest == 0 or n >largest:
            largest = n
print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
print("Largest:", largest)


