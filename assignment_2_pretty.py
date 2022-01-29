from tkinter import *
import math

CANV_WIDTH = 1440
CANV_HEIGHT = 900


def draw_axes(scale, tick_length):
    """Draws a horizontal line across the middle of the canvas, and a vertical
    line down the centre of the canvas using tkinter's default line thickness
    and colour.
    """

    # Draw the x axis
    width = w.winfo_width()
    w.create_line(get_x(-width // 2), get_y(0), get_x(width // 2), get_y(0), fill = '#687078')

    # Draw the y axis
    height = w.winfo_height()
    w.create_line(get_x(0), get_y(-height // 2), get_x(0), get_y(height // 2), fill = '#687078')

    x = 1
    while x * scale <= width//2:
        w.create_line(get_x(x * scale), get_y(0), get_x(x * scale), get_y(-tick_length), fill = '#687078')
        w.create_line(get_x(-x * scale), get_y(0), get_x(-x * scale), get_y(-tick_length), fill = '#687078')
        x += 1

    y = 1
    while y * scale <= height//2:
        w.create_line(get_x(0), get_y(y * scale), get_x(-tick_length), get_y(y * scale), fill = '#687078')
        w.create_line(get_x(0), get_y(-y * scale), get_x(-tick_length), get_y(-y * scale), fill = '#687078')
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


def plot_line(x1, y1, x2, y2, colour='black', width = 1):
    """Draws a single pixel "dot" at Cartesian coordinates (x,y).
    The optional colour parameter determines the colour of the dot.
    """
    w.create_line(get_x(x1), get_y(y1), get_x(x2), get_y(y2), fill=colour, width=width)


def plot_point(x, fn, scale, colour, size=3):
    w.create_oval(get_x(x * scale) - size, get_y(fn(x) * scale) - size, get_x(x * scale) + size, get_y(fn(x) * scale) + size,
                  fill=colour,
                  outline=colour)
    w.create_text(get_x(x * scale) + 40, get_y(fn(x) * scale) - 15,
                  text='(' + str('%.2f' % x) + ', ' + str('%.2f' % fn(x)) + ')',
                  font="Didot 14 bold",
                  justify='right')


def plot_fn(fn, start_x, end_x, scale=20, colour='black', detail = 2, width = 1):
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

    # increase detail value to have more detail

    x = start_x
    increment = 1/(scale * detail)

    while x <= end_x:
        plot_line(x * scale, fn(x) * scale, (x + increment) * scale, fn(x + increment) * scale, colour, width)
        x += increment

    # pass  # replace this line


def square(x):
    """Returns the square of x"""
    return x * x


def sin(x):
    """Returns sine of x"""
    return math.sin(x)


def cos(x):
    """Returns cosine of x"""
    return math.cos(x)


def func_1(x):
    """A quadratic polynomial function (for testing)."""
    return -3 * square(x) + 2 * x + 1


def func_2(x):
    """Your choice of a function"""
    return x * math.sin(x)  # replace this line


def func_3(x):
    """Your choice of a function"""
    if not x == 0:
        return math.sin(60 / x)  # replace this line
    else:
        return 0


def func_4(x):
    return math.sin(6 * x * x)


master = Tk()
master.title('Plot')
w = Canvas(master,
           width=CANV_WIDTH,
           height=CANV_HEIGHT)
w.pack(expand=YES, fill=BOTH)
w.configure(bg="#F0F2F5")
w.update()  # makes w.winfo_width() and w.winfo_height() meaningful


def main():
    global_scale = 80

    # plot functions
    plot_fn(sin, -20, 20, global_scale, 'green', 2)  # sin() is defined in the math module
    plot_fn(cos, -20, 20, global_scale, '#4CC7BB', 2, 2)  # cos() is defined in the math module
    plot_fn(square, -20, 20, global_scale, '#E85454', 2)
    plot_fn(func_1, -2, 3, global_scale, '#9645CC',  2)
    plot_fn(func_2, -20, 20, global_scale, '#EDD172', 2)
    # plot_fn(func_3, -30, 30, global_scale, '#72ABED', 10)
    # plot_fn(func_4, -30, 30, global_scale, '#72ABED', 2, 1)
    draw_axes(global_scale, 4)

    # plot points
    plot_point(7, sin, global_scale, 'maroon')
    plot_point(2, square, global_scale, 'blue')
    plot_point(math.pi / 2, sin, global_scale, 'black')


main()

mainloop()
