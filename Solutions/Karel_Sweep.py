from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        paint_corner("yellow")
        while front_is_clear():
            move()
            paint_corner("red")
            put_beeper()
        if facing_east():
            if left_is_clear():
                move_to_next_row_in_east()
        else:
            if right_is_clear():
                move_to_next_row_in_west()

def move_to_next_row_in_east():
    turn_left()
    if front_is_clear():
        move()
    turn_left()

def move_to_next_row_in_west():
    turn_right()
    if front_is_clear():
        move()
    turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
