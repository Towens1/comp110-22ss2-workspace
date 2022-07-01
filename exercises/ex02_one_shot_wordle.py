"""EX02 - One-Shot_Wordle - Loops!"""
__author__ = "730237027"
secretword = "python"

"""Code for user input"""
guess = input(f"What is your {len(secretword)}-letter guess? ")
while len(guess) != len(secretword):
    guess = input("That was not {len(secretword)}letters! Try again: ")

i = 0
result = ""
while i < len(secretword):
    """While loop checks guess letter by letter to identify 
    if it matches the secret word and prints green box for correctly placed letters"""
    if guess[i] == secretword[i]:
        result = result + "\U0001F7E9" 
    else:
        test = False
        n = 0
        while test is not True and n < len(secretword):
            """While loops determines whether letter in guess is in the secret word in any other 
            position and prints a yellow box if it is and a white box if it is not"""
            if guess[i] == secretword[n]:
                
                test = True
            n = n + 1
        if test is True:
            result = result + "\U0001F7E8"
        else:
            result = result + "\U00002B1C" 
    i = i + 1
print(result)
if guess == secretword:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")