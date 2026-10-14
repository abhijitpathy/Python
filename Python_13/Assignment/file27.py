str = "apple"
count=0
for i in str:
    if i == "p" :
        count+=1
        if count>1:
            print("repeated character")
            break
else:
    print("not repeated")



word = input("Enter a word: ").lower().strip()

for i in range(len(word)):
    for j in range(i + 1, len(word)):
        if word[i] == word[j]:
            print("Repeated character")
            break
else:
    print("No repeated character")


s = input("Enter a string: ").lower().strip()


for i in range(len(s)):
    ch = s[i]
    if s.count(ch) >= 2:
        print("Repeated Character is: ",ch)
        break
else:
    print("No repeated character")