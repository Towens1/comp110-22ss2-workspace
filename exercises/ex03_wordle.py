"""EX02 - Wordle - The Complete Game!"""
__author__ = "730237027"

secretword = "codes"


def contains_char(secretword: str, ltr: str) -> bool:
    """Function determines whether given letter in guess is in the secret word."""
    assert len(ltr) == 1
    i: int = 0
    check: bool = False
    while check is not True and i < len(secretword):
        if ltr == secretword[i]:
            check = True
        i = i + 1
    return check


def emojified(guess: str, secretword: str) -> str:
    """Function prints certain colored box depending on whether a letter in guess is in the secret word.
    
    If the letter is in the same position in both words, the box is green. 
    If the letter is not in the same position but in both words, the box is yellow. 
    If the letter is not in the secret word, then the box is white. 
    The string of the colored-boxes is returned.
    """
    assert len(guess) == len(secretword)
    i: int = 0
    result = ""
    while i < len(secretword):
        if guess[i] == secretword[i]:
            result = result + "\U0001F7E9" 
        else:
            check = contains_char(secretword, guess[i])
            if check is True:
                result = result + "\U0001F7E8"
            else:
                result = result + "\U00002B1C" 
        i = i + 1
    return result


def input_guess(length: int) -> str:
    """Function prompts user to input guess.
    
    If guess does not match set length, the user will be prompted to enter another guess.
    Guess is returned.
    """
    guess = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That was not {length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    while turns < 7:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secretword))
        result = emojified(guess, secretword)
        print(result)
        if guess == secretword:
            print(f"You won in {turns}/6 turns!")
            return None
        else:
            turns = turns + 1
    print("X/6 - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main()