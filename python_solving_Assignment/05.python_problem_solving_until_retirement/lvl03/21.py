digit_num = int(input("Enter a number: "))
digit_num = abs(digit_num)
digit_count = 0

while digit_num > 0:
    digit_num //= 10
    digit_count += 1

if digit_count == 0:
    digit_count = 1

print(digit_count)