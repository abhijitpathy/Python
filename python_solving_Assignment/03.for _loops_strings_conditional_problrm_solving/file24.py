sentence = input("Enter sentence: ")
word = input("Enter secret word: ")

count = 0
position = 0

for i in range(len(sentence)):
    if sentence[i:i+len(word)] == word:
        count = count + 1

        if position == 0:
            position = i

if count > 0:
    print("Starting position:", position)
    print("Occurrences:", count)
else:
    print("Secret word not found")