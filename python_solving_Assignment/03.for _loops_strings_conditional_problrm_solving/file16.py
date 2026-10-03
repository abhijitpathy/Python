p = input("Enter password: ")

u = l = d = s = 0

for ch in p:
    if 'A' <= ch <= 'Z':
        u += 1
    elif 'a' <= ch <= 'z':
        l += 1
    elif '0' <= ch <= '9':
        d += 1
    else:
        s += 1

t = len(p)

print("Uppercase:", u, u/t*100, "%")
print("Lowercase:", l, l/t*100, "%")
print("Digits:", d, d/t*100, "%")
print("Special:", s, s/t*100, "%")

if u >= l and u >= d and u >= s:
    print("Dominant: Uppercase")
elif l >= d and l >= s:
    print("Dominant: Lowercase")
elif d >= s:
    print("Dominant: Digits")
else:
    print("Dominant: Special")



