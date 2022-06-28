"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730237027"

word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
ltr = input("Enter a single character: ")
if len(ltr) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + ltr + " in " + word)
i = 0
if word[0] == ltr:
    print(ltr + " found at index 0")
    i += 1
if word[1] == ltr:
    print(ltr + " found at index 1")
    i += 1
if word[2] == ltr:
    print(ltr + " found at index 2")
    i += 1
if word[3] == ltr:
    print(ltr + " found at index 3")
    i += 1
if word[4] == ltr:
    print(ltr + " found at index 4")
    i += 1
if i == 0:
    print("No instances of " + ltr + " found in " + word)
if i == 1:
    print("1 instance of " + ltr + " found in " + word)
else:
    print(str(i) + " instances of " + ltr + " found in " + word)
