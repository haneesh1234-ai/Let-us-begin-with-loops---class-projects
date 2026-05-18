#cheracter occurence
word = str(input("enter a word : "))
character = str(input("enter the character to know the occurence : "))
count = 0
i = 0
while i <len(word) :
    if word[i] == character :
        count = count + 1
    i = i + 1
print("number of occurence = ",count )