sum_num = int(input("Enter a number: "))
digit_sum = 0

while sum_num > 0:
    digit_sum += sum_num % 10
    sum_num //= 10

print(digit_sum)