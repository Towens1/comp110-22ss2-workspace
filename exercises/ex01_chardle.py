"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730237027"

word = str(input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
ltr = str(input("Enter a single letter: "))
if len(ltr) != 1:
    print("Error: Character must be a single character.")
    exit()
i = 0
if word[0] == ltr:
    print(ltr + " found at index 0")
    i +=1
if word[1] == ltr:
     print(ltr + " found at index 1")
     i +=1
if word[2] == ltr:
     print(ltr + " found at index 2")
     i +=1
if word[3] == ltr:
     print(ltr + " found at index 3")
     i +=1
if word[4] == ltr:
     print(ltr + " found at index 4")
     i +=1
print(str(i) + " instances of " + ltr + " found in " + word)
