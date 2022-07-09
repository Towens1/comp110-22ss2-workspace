,

import random
player: str = ""
points: int = 0
petName: str = ""
icon: str = "\U0001F973"
dog: str = "\U0001F415"
cat: str = "\U0001F408"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    global player 
    greet()
    player = input("Enter your name: ")
    
    print(f"Hi, {player}! Please select your pet")
    petChoice = input("Enter 1 to adopt a pet dog, Enter 2 to adopt a pet cat, and enter 3 to adopt on another day. ")

    global points
    global petName
    if petChoice == "3":
        print(f" {player}, you finished with {points} points! Come play again tomorrow!")
        exit()
    else:
        if petChoice == "1":
            print(f"Here is your new pet: {dog}")
            points += 10
            print(f"You won {points} points!")
        if petChoice == "2":
            print(f"Here is your new pet: {cat}")
            points += 10
            print(f"You won {points} points!")
    petName = input("Enter your pet's name: ")
    print(f"For welcoming {petName} into your home, you earn 5 more points!")
    points += 5
    print(f"You now have {points} points!") 
    cond: bool = False
    while cond is False:
        print("Would you like to complete another task or do you wish to exit the game? ")
        game = input("Enter 1 to continue or 2 to exit. ")
        if game == "1":
            tasks(points)
        if game == "2":
            cond is True
            print(f" {player}, you finished with {points} points! Come play again tomorrow!")
            exit()
    print(f"{player}, you are a great pet owner! You have {points} points!")


def greet() -> None:
    """Function prints a welcome message and asks player their name."""
    print("Welcome to Pet Play! This game helps you learn the responsibilities of being a pet owner. Would you like to play? What is your name? ")


def tasks(points: int) -> int:
    """Function randomly selects a pet condition and prompts user to select the correct response to their pet."""
    global petName
    global player
    list = [f"{petName} is crying", f"{petName} is sitting by the door", f"{petName} is panting", f"{petName} is barking"]
    n = random.randint(0, 3)
    choice = list[n]
    print(choice)
    response = input(f"{player}, what should you do to help {petName}? Enter 1 to feed them. Enter 2 to give them water. Enter 3 to play with them. Enter 4 to take them outside. ") 
    
    if choice == list[0] and response == "1":
        points += 5
        print(f"Great choice! {icon} You have made {petName} happy! You now have {points} points!")
        return points
    if choice == list[1] and response == "4":
        points += 5
        print(f"Great choice! {icon} You have made {petName} happy! You now have {points} points!")
        return points
    if choice == list[2] and response == "2":
        points += 5
        print(f"Great choice! {icon} You have made {petName} happy! You now have {points} points!")
        return points
    if choice == list[3] and response == "3":
        points += 5
        print(f"Great choice! {icon} You have made {petName} happy! You now have {points} points!")
        return points
    else:
        points -= 5
        print(f"Oops. That was not the right choice. {petName} is not happy. You now have {points} points.")
        return points


if __name__ == "__main__":
    main()