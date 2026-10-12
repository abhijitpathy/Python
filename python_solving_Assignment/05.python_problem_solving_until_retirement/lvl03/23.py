product_num = int(input("Enter a number: "))
digit_product = 1

while product_num > 0:
    digit_product *= product_num % 10
    product_num //= 10

if product_num == 0 and digit_product == 1:
    digit_product = 0

print(digit_product)