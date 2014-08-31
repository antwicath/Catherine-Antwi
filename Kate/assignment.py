__author__ = 'catherine'

from numbers import Number


def square_perimeter(side: Number) -> Number:
    """
    Calculate perimeter of a square from side length.
    @param side: the side length
    @return: the perimeter (same units as side length)
    >>> square_perimeter(4)
    16
    """
    return 4*side

print(square_perimeter(4))


def square_area(side):
    """
calculates area of a square from side length
    :param side: the side length
    return: the area(unit^2 from side)
    square_area(4)
    16
    """
    return side*side

print(square_area(7) )



if __name__ == "__main__":
    sampleSide = 4
    print("area:",
        square_area(sampleSide),
        "perimeter:",
        square_perimeter(sampleSide))

    from numbers import Number


def rectangle_perimeter(length : Number, breadth: Number) -> Number:
    """
    calculate perimeter of a rectangle from length and breath
    :param length:the length
    :param breadth:the breadth
    :return:the perimeter(same unit as length and breath )
    >>>rectangle_perimeter(2,3)
    10
    """
    return length *2 + 2 * breadth
print(rectangle_perimeter(1,3))


def rectangle_area(length: Number, breadth: Number) -> Number:
    """
    calculate area of a rectangle from length and breadth
    :param length: the length
    :param breadth: the breadth
    :return:the area(unit^2 from length and breadth)
    >>>rectangle_area(2,3)
    6
    """
    return length * breadth
print(rectangle_area(3,8))