"""Challenge Question 1"""
__author__ = "730237027"

choice: int = int(input("Enter a number: "))
if choice < 25:
    print("A")
if choice > 75:
    print("C")
if choice > 50:
    print("B")
else:
    print("D")
