from graphics import Canvas
import random

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 400
BALL = 12

def main():
    
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0,0, CANVAS_WIDTH, CANVAS_HEIGHT, "black")

    start_x = 80
    start_y = 150
    gap = 70

    draw_H(canvas, start_x, start_y)
    draw_E(canvas, start_x + gap, start_y)
    draw_L(canvas, start_x + gap*2, start_y)
    draw_L(canvas, start_x + gap*3, start_y)

    draw_O(canvas, start_x + gap*4, start_y)
    draw_O(canvas, start_x + gap*5, start_y)
    draw_O(canvas, start_x + gap*6, start_y)
    draw_O(canvas, start_x + gap*7, start_y)

    draw_exclamation(canvas, start_x + gap*8, start_y)

    draw_gradient_text(
    canvas,
    "Welcome to Section",
    200,
    start_y + 140
    )

def gradient_color(step, total_steps):
    """
    Creates gradient from blue → pink
    """
    start = (0, 180, 255)     # blue
    end = (255, 80, 180)      # pink

    r = int(start[0] + (end[0] - start[0]) * step / total_steps)
    g = int(start[1] + (end[1] - start[1]) * step / total_steps)
    b = int(start[2] + (end[2] - start[2]) * step / total_steps)

    return f"#{r:02x}{g:02x}{b:02x}"

def draw_gradient_ball(canvas, x, y, color):
    canvas.create_oval(
        x, y,
        x + BALL, y + BALL,
        color
    )

def draw_gradient_text(canvas, text, start_x, start_y):
    small_ball = 8       # smaller than main BALL
    spacing = small_ball + 2
    total = len(text)

    x = start_x

    for i, ch in enumerate(text):
        color = gradient_color(i, total)

        if ch != " ":
            canvas.create_oval(
                x, start_y,
                x + small_ball,
                start_y + small_ball,
                color
            )

        x += spacing

def draw_ball(canvas, x, y):
    canvas.create_oval(
        x, y,
        x + BALL, y + BALL,
        random_color()
    )


def vertical_line(canvas, x, y):
    for i in range(8):
        draw_ball(canvas, x, y + i*BALL)


def horizontal_line(canvas, x, y):
    for i in range(5):
        draw_ball(canvas, x + i*BALL, y)


# LETTERS

def draw_H(canvas, x, y):
    vertical_line(canvas, x, y)
    vertical_line(canvas, x+4*BALL, y)
    horizontal_line(canvas, x, y+4*BALL)


def draw_E(canvas, x, y):
    vertical_line(canvas, x, y)
    horizontal_line(canvas, x, y)
    horizontal_line(canvas, x, y+4*BALL)
    horizontal_line(canvas, x, y+7*BALL)


def draw_L(canvas, x, y):
    vertical_line(canvas, x, y)
    horizontal_line(canvas, x, y+7*BALL)


def draw_O(canvas, x, y):
    horizontal_line(canvas, x, y)
    horizontal_line(canvas, x, y+7*BALL)
    vertical_line(canvas, x, y)
    vertical_line(canvas, x+4*BALL, y)


def draw_exclamation(canvas, x, y):
    for i in range(6):
        draw_ball(canvas, x, y + i*BALL)
    draw_ball(canvas, x, y + 7*BALL)


def random_color():
    colors = [
    # Bright basic colors
    'lime', 'aqua', 'fuchsia', 'yellow',
    'gold', 'coral', 'turquoise', 'skyblue',

    # Bright pastel colors
    'lightgreen', 'lightcoral',
    'lightpink', 'lightskyblue',

    # Fresh nature colors
    'springgreen', 'mediumseagreen', 'mediumorchid',

    # Warm bright colors
    'tomato', 'deeppink', 'hotpink', 'orangered',

    # Cool bright colors
    'deepskyblue', 'dodgerblue', 'royalblue',

    # Strong vibrant colors
    'blue', 'salmon', 'cyan',
    'orange', 'green', 'red', 'magenta'
]
    return random.choice(colors)


if __name__ == "__main__":
    main()
