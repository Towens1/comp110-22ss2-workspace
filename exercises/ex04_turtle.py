"""EX04 - Turtle - Creates an image of a house and the sun/"""
__author__ = "730237027"

from turtle import Turtle, colormode, done
lola: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene.

    Function prints the following in order by calling other functions:
    2 house windows, door, body of house, roof, and then the sun.
    """
    lola.pencolor("blue")
    print(square(lola, -200, -50.0, 100.0))
    print(square(lola, 0, -50.0, 100.0))

    lola.pencolor("black")
    print(square(lola, -100, -200, 100))

    lola.pencolor("green")
    print(rectangle(lola, -250.0, -10.0, 200.0))
    
    lola.begin_fill()
    print(triangle(lola, -250.0, -10.0, 200.0))
    lola.end_fill()

    
    print(spiral(lola, 250.0, 250.0, 30.0))
  
    
    


def square(lola: Turtle, x: float, y: float, width: float) -> None:
    """ Function draws a square of the given width those top-left corner is located at x, y."""
    lola.penup()
    lola.goto(x, y)
    lola.setheading(0.0)
    lola.pendown()

    i: int = 0
   
    while i < 4:
        
        lola.forward(width)
        lola.right(90)
        i += 1
   
    


def rectangle(lola: Turtle, x: float, y: float, width: float) -> None:
    """Function draws a rectange of the given width those top-left corner is located at x, y."""
    lola.penup()
    lola.goto(x, y)
    lola.setheading(0.0)
    lola.pendown()
    lola.pencolor("green")
    i: int = 0
    
    while i < 2:
        lola.forward(width * 2)
        lola.right(90)
        lola.forward(width * 1.5)
        lola.right(90)
        i += 1


def triangle(lola: Turtle, x: float, y: float, width: float) -> None:
    """ Function draws a triangle of the given width those top-left corner is located at x, y."""
    lola.penup()
    lola.goto(x,y)
    lola.setheading(0.0)
    lola.pendown()
    lola.color("gray")

    i: int = 0
    while i <  3:
        lola.forward(width * 2)
        lola.left(120)
        i += 1
    


def spiral(lola: Turtle, x: float, y: float, width: float) -> None:
    """Draw a circle of the given width those top-left corner is located at x, y."""
    lola.penup()
    lola.goto(x, y)
    lola.setheading(0.0)
    lola.pendown()
    
    lola.pencolor("yellow")
    i: int = width
    
    while i < 125:
        lola.forward(width)
        lola.right(24)
        i += 5

    

if __name__ == "__main__":
    main()
    done()