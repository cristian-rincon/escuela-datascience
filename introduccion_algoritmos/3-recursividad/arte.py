import turtle

my_turtle = turtle.Turtle()
my_window = turtle.Screen()


def draw(my_turtle, length):

    if length > 0:
        my_turtle.forward(length)
        my_turtle.left(80)
        draw(my_turtle, length - 5)


if __name__ == "__main__":
    draw(my_turtle, 200)
    my_window.exitonclick()
