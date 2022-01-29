from tkinter import *
from math import *

CANV_WIDTH = 750
CANV_HEIGHT = 250


def draw_axes(scale, tick_length):
    """Draws a horizontal line across the middle of the canvas, and a vertical
    line down the centre of the canvas using tkinter's default line thickness
    and colour.
    """

    # Draw the x axis
    width = w.winfo_width()
    w.create_line(get_x(-width // 2), get_y(0), get_x(width // 2), get_y(0))

    # Draw the y axis
    height = w.winfo_height()
    w.create_line(get_x(0), get_y(-height // 2), get_x(0), get_y(height // 2))

    # Draw ticks: start at 1 (-1) and keep going until the end of canvas in both directions

    x = 1
    while x * scale <= width//2:
        w.create_line(get_x(x * scale), get_y(0), get_x(x * scale), get_y(-tick_length))
        w.create_line(get_x(-x * scale), get_y(0), get_x(-x * scale), get_y(-tick_length))
        x += 1

    y = 1
    while y * scale <= height//2:
        w.create_line(get_x(0), get_y(y * scale), get_x(-tick_length), get_y(y * scale))
        w.create_line(get_x(0), get_y(-y * scale), get_x(-tick_length), get_y(-y * scale))
        y += 1


def get_x(x_val):
    """Maps a Cartesian-style x coordinate (where x is 0 at the window's
    horizontal centre) onto the tkinter canvas (where x is 0 is at the left
    edge). x_val is the Cartesian x coordinate. The units of measurerment
    are pixels.
    """
    return w.winfo_width() // 2 + x_val


def get_y(y_val):
    """Maps a Cartesian-style y coordinate (where y is 0 at the window's
    vertical centre, and in which y grows in value upwards) onto the tkinter
    canvas (where y is 0 is at the top edge, and y grows in value downwards).
    y_val is the Cartesian y coordinate. The returned value is the
    corresponding tkinter canvas x coordinate. The units of measurerment are
    pixels.
    """
    return w.winfo_height() // 2 - y_val


def plot_point(x, y, colour='black'):
    """Draws a single pixel "dot" at Cartesian coordinates (x,y).
    The optional colour parameter determines the colour of the dot.
    """
    w.create_oval(get_x(x), get_y(y), get_x(x), get_y(y), width=1,
                  fill=colour,
                  outline=colour)


def plot_fn(fn, start_x, end_x, scale=20, colour='black'):
    """Plots a function, y = fn(x), onto the canvas.

    Parameters:

    * fn is a function that takes a single number parameter and returns a
      number.

    * start_x is the left-most x value to be passed to fn.

    * end_x is the right-most x value to be passed to fn.

    * scale (optional) is used as a multiplier in both the x and y directions
      to "zoom in" on the plot. It is also used to increase the number of x
      coordinates "fed" to the fn function, to fill in all the horizontal gaps
      that would otherwise appear between the plotted points. scale is
      particularly useful for showing detail that would be otherwise be lost.

    * colour (optional) determines the colour of the plotted function.

    Note: nothing bad happens if start_x, end_x, or any y value computed from
    fn(x) is off the canvas. Those points simply will not be displayed.
    (Note to the student programmer: This happens automatically. You don't
    have to program it.)
    """
    x = start_x

    while x <= end_x:
        plot_point(x * scale, fn(x) * scale, colour)
        x += 1/scale

    # pass  # replace this line


def square(x):
    """Returns the square of x"""
    return x * x


def func_1(x):
    """A quadratic polynomial function (for testing)."""
    return -3 * square(x) + 2 * x + 1


def func_2(x):
    """A trigonometric function"""
    return x * sin(x)  # replace this line


def func_3(x):
    """Another trigonometric function"""
    return x / tan(x)  # replace this line


master = Tk()
master.title('Plot THIS!')
w = Canvas(master,
           width=CANV_WIDTH,
           height=CANV_HEIGHT)
w.pack(expand=YES, fill=BOTH)
w.update()  # makes w.winfo_width() and w.winfo_height() meaningful


def main():
    # draw the axes with ticks, and plot functions
    draw_axes(40, 4)
    plot_fn(sin, -20, 20, 40, 'green')  # sin() is defined in the math module
    plot_fn(cos, -20, 20, 40, 'blue')  # cos() is defined in the math module
    plot_fn(square, -20, 20, 40, 'red')
    plot_fn(func_1, -2, 3, 40, 'purple')
    plot_fn(func_2, -15, 15, 40, 'brown')
    plot_fn(func_3, -30, 30, 20, 'cyan')


main()

mainloop()
