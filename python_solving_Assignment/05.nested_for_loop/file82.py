str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

for char in str1:
  str2 = str2.replace(char, "", 1)

if len(str2) == 0:
  print("Anagram")
else:
  print("Not Anagram")



str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


len1 = 0
for char in str1:
    len1 += 1


len2 = 0
for char in str2:
    len2 += 1


if len1 != len2:
    is_anagram = False
else:
    is_anagram = True

    
    for char1 in str1:
        found = False
        new_str2 = "" 
        
        
        already_skipped = False 

        
        for char2 in str2:
            if char2 == char1 and not already_skipped:
                found = True
                already_skipped = True  
                
            else:
                new_str2 += char2  

        
        str2 = new_str2

        
        if not found:
            is_anagram = False
            break


if is_anagram:
    print("Anagram")
else:
    print("Not an Anagram")

