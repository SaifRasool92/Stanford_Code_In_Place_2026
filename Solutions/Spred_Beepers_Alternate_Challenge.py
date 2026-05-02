from karel.stanfordkarel import *

def main():
    spread_piles()
    return_home()

def spread_piles():
    """Spread out a pile of beepers to the right.

    Pre: Karel is on a corner to the left of a pile of beepers.
         Karel is facing east.
    Post: Karel is on an empty corner to the right of the
          last spread beeper.  Karel is facing east.
    """
    move()
    while beepers_present():
        move_pile()
        move()

def move_pile():
    """Move all but one beeper to the next column on the right.

    Pre: Karel is on a pile of beepers facing east.
    Post: Karel is on the same corner facing east.
    """
    while beepers_present():
        pick_beeper()
        if beepers_present():
            put_beeper_on_right()
    put_beeper()

def put_beeper_on_right():
    """Put a beeper in the next column on the right.

    Pre: Karel is on a pile of beepers facing east.
    Post: Karel is on the same corner facing east.
    """
    move()
    put_beeper()
    move_back()

def move_back():
    """Move backwards one corner.

    Karel remains facing in the same direction.
    """
    turn_around()
    move()
    turn_around()

def return_home():
    """Move Karel to the west corner.

    Pre: Karel is somewhere on the row facing east.
    Post: Karel is in the west corner facing east.
    """
    turn_around()
    move_to_wall()
    turn_around()

def move_to_wall():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
