import turtle
import argparse
import math


# Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
# Програма має візуалізувати фрактал “дерево Піфагора”,
# і користувач повинен мати можливість вказати рівень рекурсії.
def draw_square(t: turtle.Turtle, side: float, is_right: bool) -> None:
    """Draw a square with side s starting from current position/heading."""

    if is_right:
        t.color("green")
    else:
        t.color("red")
    for _ in range(4):
        t.forward(side)
        t.left(90)


def classic_pythagoras_tree(t: turtle.Turtle, side: float, depth: int, is_right: bool) -> None:
    """
    Classic Pythagoras tree:
    1) draw a square of side s
    2) go to its top-left corner
    3) draw left child square on the left leg (rotation +theta)
    4) move to attachment point for right child square and draw it (rotation -(90-theta))
    theta is in radians.
    """
    if depth == 0 or side < 2:
        return

    # Draw current square (base)
    draw_square(t, side, is_right)

    # Move to top-left corner of current square
    t.penup()
    t.left(90)
    t.forward(side)
    t.right(90)

    if is_right:  # For the right square, move to one side further
        t.forward(side)
        t.right(90)
    t.pendown()

    top_left = t.position()
    top_left_heading = t.heading()

    # Compute child side lengths
    next_side = side * math.sqrt(2) / 2

    # ---- Left child square ----
    t.penup()
    t.setposition(top_left)
    t.setheading(top_left_heading)
    t.left(45)
    t.pendown()

    classic_pythagoras_tree(t, next_side, depth - 1, is_right=False)

    # ---- Right child square ----

    # Start again at top-left, move along the top edge by s_left to the triangle's apex attachment
    t.penup()
    t.setposition(top_left)
    t.setheading(top_left_heading)
    t.forward(side)
    t.left(45)
    t.pendown()

    classic_pythagoras_tree(t, next_side, depth - 1, is_right=True)


def main(recursion_level):
    screen = turtle.Screen()
    screen.title("Classic Pythagoras Tree from squares with 45° branches")

    t = turtle.Turtle()
    t.speed(0)  # set to 1..3 for slower
    t.pensize(2)

    base_side = 120

    # Place base square
    t.penup()
    t.goto(-base_side / 2, -250)
    t.setheading(0)  # face east
    t.pendown()

    # we draw left square for the start
    classic_pythagoras_tree(t, base_side, recursion_level, is_right=False)

    screen.mainloop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw a Classic Pythagoras Tree Fractal")
    parser.add_argument("level", type=int, help="Recursion level for the fractal")
    args = parser.parse_args()

    if args.level < 0:
        print("Level must be a non-negative integer.")
    else:
        main(args.level)


# Example usage:
# python pythagoras_tree.py 5
