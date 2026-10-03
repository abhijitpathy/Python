s = input("Enter string: ")

up = lo = di = spc = sch = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        up += 1
    elif 'a' <= ch <= 'z':
        lo += 1
    elif '0' <= ch <= '9':
        di += 1
    elif ch == ' ':
        spc += 1
    else:
        sch += 1

print(up, lo, di, spc, sch)

m = up
if lo > m: m = lo
if di > m: m = di
if spc > m: m = spc
if sch > m: m = sch

if [up, lo, di, spc, sch].count(m) > 1:
    print("Tie")
else:
    print("Highest count:", m)