"""
mandelbrot.py
Define a mapping from (x, y) pixel locations to (R,G,B) colour values by
applying the Mandelbrot algorithm and counting iterations.
"""

from config import MAX_X, MAX_Y, MAX_ITERATION, X1, X2, Y1, Y2
from utils import progress, scaled


def color(it):
    """
    Arbitrarily maps the number of iterations to an RGB colour.
    :param it:The number of iterations for this value.
    :return:A tuple (R, G, B) of color values to paint this pixel.
    """
    # TODO: Figure out a linear colour-map that looks half-decent.
    return (it+160) % 256, (it+80) % 256, it % 256


@progress(iterations=MAX_X * MAX_Y)
def basic_mandelbrot(x, y):
    """
    Calculate and return the RGB colour for a given (x, y) pixel.
    :param x: The X coordinate of the pixel.
    :param y: The Y coordinate of the pixel.
    :return: A tuple (R,G,B) of values 0-255.
    """
    # Scale X and Y to the viewport bounded by (X1, Y1) and (X2, Y2).
    x = scaled(x, 0, MAX_Y, X1, X2)
    y = scaled(y, 0, MAX_Y, Y1, Y2)

    # Set the initial value z0 and the constant c.
    z = complex(0, 0)
    c = complex(x, y)

    # Count the number of iterations to escape an arbitrary "bound".
    for i in range(MAX_ITERATION):
        z = z*z + c
        if abs(z) > 4:
            break
    else:
        # We haven't escaped in time - return a default colour of black.
        return 0, 0, 0

    # Return a color based on this escape time.
    return color(i)


if __name__ == "__main__":
    from renderer import display
    display(basic_mandelbrot)
