# Task 1
your_name='Abhijit'
your_city="Berhampur"
your_favorite_programming_language="Python"
A_short_message="Hlo nice to meet you"

print(your_name,your_city,your_favorite_programming_language,A_short_message)

#task 2
x=""
print(x)
print(len(x))
print(type(x))

#task 3
z="Python Programming"
print(z)
print(len(z))
print(z[0])
print(z[17])
print(z[2])
print(z[16])

#task 4
c="Programming"
print(c[0])
print(c[1])
print(c[4])
print(c[10])

#task 5
q="Programming"
print(q[-10])
print(q[-9])
print(q[-8])
print(q[-1])

#task 6
a="Abhijit pathy"
print(a[0])
print(a[12])
print(a[-1])

#task 7
q="Python Programming"
print(q[0:6])
print(q[7:])
print(q[:])
print(q[:5])
print(q[-5:])

# task8
text = "ABCDEFGHIJKL"

print(text[::2])    
print(text[::3])     
print(text[1:9:2])   
print(text[::-1])    


#task 9
text = "Python Programming"

# Last 5 characters
print(text[-5:])

# Last 10 characters
print(text[-10:])

# Characters from the end using a negative step
print(text[::-1])

# task 10
text = "Programming"

print(text[:3])

print(text[-3:])

print(text[::2])

print(text[::-1])

print(text[1:-1])

#task 11
word = "Python"
sentence = "Python is easy"
sentence_spaces = "Python  is  easy"

print("Length of word:", len(word))
print("Length of sentence:", len(sentence))
print("Length of sentence with spaces:", len(sentence_spaces))

#task 12
text = "Python Programming"

last_index = len(text) - 1

print("Last valid index:", last_index)
print("Last character:", text[last_index])

#task 13
first_name = "Abhijit"
last_name = "Pathy"

full_name = first_name + " " + last_name

print(full_name)

#task 14
name = "Abhijit"
age = "18"
city = "Berhampur"
programming_language = "Python"

sentence = "My name is " + name + ". I am " + age + " years old and I live in " + city + ". I am learning " + programming_language + "."

print(sentence)

#task 15
t="whole"
u=2
# it shows type error when string add with a int
print(t+str(u))


#task 16
p="parrot"
print(p*3)
print(p*5)
print(p*10)

#task 17
m="matcha"
print(m*10)

# TASK 18
z="python programming language"
print(z.upper())
print(z.lower())
print(z.capitalize())
print(z.title())
print(z.swapcase())

#task 19
s="Python"
d="python"
print(s==d)
#false these two are not equal
print(s.lower()==d)
# now its true and both of them are equal

#task 20
q="Python is a programming language"
print("python" in  q)
print("programming" in q)
print("java" in q)
print("language" in q)

#task 21
o="Python is a programming language"
print(o.find("python"))
print(o.find("programming"))
print(o.find("language"))
print(o.find("java"))

# task 22
k="Python is a programming language"
print(k.index("Python"))
print(k.index("programming"))
print(k.index("language"))
 #print(k.index("java")) this one shows error and the name of error is type error 
# the difference in find() and index() is that in find we even if the character is not present its doesn't show error whereas in index() it shows value error.


# task 23
f="banana"
print(f.count("a"))
print(f.count("n"))
print(f.count("b"))

# task 24
v = "student_notes.pdf"
print(v.startswith("student"))
print(v.startswith("pdf"))
print(v.startswith("txt"))

#task 25
b="I am learning Java"
c=b.replace("java","python")
print(b)

#task 26
n="apple,apple,apple"
print(n.replace("apple","mango"))

#task 27
b="apple,apple,apple"
print(b.replace("apple","mango",1))

#task 28
text = "Python"
print(text.upper())

#task 29
text="    python programming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#task 30
input("enter your name :")
c="Abhi"
b=c.strip()
print(b)

#task 31
v="pyhton is easy to learn"
c=v.split()
print(c)

#task 32
m="apple,banana,mango,orange"
n=m.split()
print(n)

#task 33
words = ["Python", "is", "easy"]
k="".join(words)
print("k")

#task 34
m="Python-is-easy"
l="".join(m)
print(l)

#task 35
name = "Abhijit"
age = 18
city = "Berhampur"

sentence = f"My name is {name}, I am {age} years old, and I live in {city}."

print(sentence)

#task 36
a = 10
b = 20

print(f"The sum is {a + b}")

#task 37

text = "Python"
#print(text[20])
#IndexError: string index out of range
#"Python" has only 6 characters, with indexes 0 to 5. Index 20 does not exist.
#Corrected:

text = "Python"
print(text[2])

text = "Python"
#text[0] = "J"

#Error:

#TypeError: 'str' object does not support item assignment

#Strings in Python are immutable, meaning you cannot change an individual character directly.

#Corrected:

text = "Python"
text = "J" + text[1:]

print(text)
age = 20
#print("Age: " + age)

#Error:

#TypeError: can only concatenate str (not "int") to str
#"Age: " is a string, but age is an integer. Python cannot concatenate a string and an integer directly.

#Corrected using str():

age = 20
print("Age: " + str(age))
text = "Python"
#print(text.index("Java"))

#Error:

#ValueError: substring not found
#Why?
#"Java" does not exist inside "Python", so .index() cannot find its position.

#Corrected:

text = "Python"
print(text.index("th"))


#task   38
name = input("Enter your full name: ")
cleaned_name = name.strip()
print("Original input:", name)
print("Cleaned name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Length:", len(cleaned_name))
print("First character:", cleaned_name[0])
print("Last character:", cleaned_name[-1])
character = input("Enter a character to search: ")
print("Contains character:", character in cleaned_name)


#task 39
sentence = input("Enter a sentence: ")

print("Original sentence:", sentence)

print("Number of characters:", len(sentence))

print("Number of words:", len(sentence.split()))

print("First character:", sentence[0])

print("Last character:", sentence[-1])

print("Uppercase:", sentence.upper())

print("Lowercase:", sentence.lower())

print("Title case:", sentence.title())

print("Contains Python:", "Python" in sentence)

character = input("Enter a character to count: ")
print("Number of times it occurs:", sentence.count(character))

# Task 40

first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
city = input("Enter your city: ").strip()
course = input("Enter your course: ").strip()
age = int(input("Enter your age: "))


full_name = first_name + " " + last_name

print("Title Case:", full_name.title())

print("Uppercase:", full_name.upper())


print("Lowercase:", full_name.lower())

print("Length of full name:", len(full_name))


print("First character:", full_name[0])


print("Last character:", full_name[-1])

print("City:", city)
print("Course:", course)


print(f"Age: {age}")


print("Contains Python:", "Python" in course)

replaced_course = course.replace("Python", "Java")
print("Replaced course:", replaced_course)


word_count = len(course.split())
print("Number of words in course:", word_count)

