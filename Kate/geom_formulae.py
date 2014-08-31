__author__ = 'catherine'

from numbers import Number
from math import *
import math


def rectangle_perimeter(length: Number, breadth: Number) -> Number:
    """
    calculate perimeter of a rectangle from length and breath
    :param length:the length
    :param breadth:the breadth
    :return:the perimeter(same unit as length and breath )
    >>>rectangle_perimeter(1,3)
    8
    """
    return length * 2 + 2 * breadth

print(rectangle_perimeter(1, 3))


def rectangle_area(length, breadth):
    """
    calculate area of a rectangle from length and breadth
    :param length: the length
    :param breadth: the breadth
    :return:the area(unit^2 from length and breadth)
    >>>rectangle_area(2,3)
    6
    """
    return length * breadth

print(rectangle_area(3, 8))


def equilateral_triangle_area(base, height):
    """
    calculate area of an equilateral triangle from base and height
    :param base: the base
    :param height: the height
    :return:the area(unit^2 from base and height)
    >>>equilateral_triangle_area(6,5)
    15
    """
    return 0.5 * base * height


def equilateral_triangle_area_alternate(side: Number) -> Number:
    """
    calculate the area of equilateral triangle
    :param side: the side length
    :return: the area(unit^2 from side)
    >>> equilateral_triangle_area_alternate(6)
    """
    return (math.sqrt(3)/4) * side * side * side


def equilateral_triangle_perimeter(side: Number) -> Number:
    """
    calculate perimeter of an equilateral triangle
    :param side: the side length
    :return:the perimeter(same unit as side)
    >>>equilateral_triangle_perimeter(6)
    18
    """
    return 3*side


def parallelogram_perimeter(base, height: Number) -> Number:
    """
    calculate the perimeter of a parallelogram
    :param base: the base
    :param height: the height
    :return: the perimeter(same unit as base and height)
    >>>parallelogram_perimeter(3,4)
    14
    """
    return 2*base + 2*height


def parallelogram_area(base, height: Number) -> Number:
    """
    calculate the area of a parallelogram
    :param base: the base
    :param height: the height
    :return: the area(unit^2 from base and height)
    >>> parallelogram_area(3,4)
    12
    """

    return base*height


def circle_perimeter(radius: Number) -> Number:
    """
    calculates the perimeter of a circle
    :param radius: the radius
    :return:the perimeter(same unit as radius)
    >>>circle_perimeter(3)
    28.274333882308138
    """
    return pi * radius * radius

print(circle_perimeter(3))


def circle_area(radius: Number) -> Number:
    """
    calculate the area of a circle
    :param radius: the radius
    :return: tne area(unit^2 from radius)
    >>>circle_area (3)
    18.84955592153876
    """
    return 2 * pi * radius

print(circle_area(3))


def rhombus_area(diagonal_length_1, diagonal_length_2: Number) -> Number:
    """
    calculate the area of a rhombus
    :param diagonal_length_1: the first diagonal length
    :param diagonal_length_2: the other diagonal length
    :return: the area(unit^2 from diagonal length)
    >>>rhombus_area(3,4)
    6
    """
    return 0.5 * diagonal_length_1 * diagonal_length_2

print(rhombus_area(3, 4))


def rhombus_area_alternative(base, height: Number) -> Number:
    """
    calculate the area of a rhombus
    :param base: the base length
    :param height: the height length
    :return: the area(unit^2 from base and height)
     >>>rhombus_area_alternative(7,9)
     63
    """
    return base * height

print(rhombus_area_alternative(7, 9))


def ellipse_area(radius_1, radius_2: Number) -> Number:
    """
    calculate the area of an ellipse
    :param radius_1: the horizontal radius
    :param radius_2: the vertical radius
    :return:the area(unit^2 from radius)
    >>>ellipse_area(3,4)
    37.69911184307752
    """
    return pi * radius_1 * radius_2

print(ellipse_area(3, 4))


def sphere_volume(radius: Number) -> Number:
    """
    calculate the volume of a sphere
    :param radius: the radius of the sphere
    :return: the volume(unit^3 from radius)
    >>>sphere_volume(3)
    113.09733552923254
    """
    return (4.0/3.0) * pi * radius * radius * radius

print(sphere_volume(3))


def cuboid_volume(length, breadth, height: Number) -> Number:
    """
    calculate the volume of a cuboid
    :param length: the length
    :param breadth: the breadth
    :param height: he height
    :return: the volume(unit^3 from length)
    >>>cuboid_volume(3,4,5)
    60
    """
    return length * breadth * height

print(cuboid_volume(3, 4, 5))


def cube_volume(side: Number) -> Number:
    """
    calculate the volume of a cube
    :param side: the side length
    :return: the volume(unit^3 from side)
    >>>cube_volume(3)
    27
    """
    return side ** 3

print(cube_volume(3))


def pyramid_volume(base, height):
    """
    calculate the volume of a pyramid
    :param base: the base
    :param height: the perpendicular height
    :return: the volume (unit^3 from base)
    >>>pyramid_volume(3,4)
    4
    """
    return 1.0/3.0 * base * height

print(pyramid_volume(3, 4))


def cylinder_volume(radius, height):
    """
    calculate the volume of a cylinder
    :param radius: the radius
    :param height: the height
    :return: the volume (unit^3 from radius)
    >>>cylinder_volume(3,5)
    141.3716694115407
    """
    return pi * radius ** 2 * height

print(cylinder_volume(3, 5))


def cone_volume(radius, height):
    """
    calculate the volume of a cone
    :param radius: the radius of the base
    :param height: the height
    :return: the volume (unit^3 from radius)
    >>>cone_volume(3,5)
    47.1238898038469
    """
    return (pi * radius ** 2 * height)/3

print(cone_volume(3, 5))


def regular_hexagon_perimeter(side):
    """
    calculate the perimeter of a regular hexagon
    :param side: the side
    :return: the perimeter (same unit as the side)
    >>>regular_hexagon_perimeter(5)
    30
    """
    return 6 * side

print(regular_hexagon_perimeter(5))


def regular_hexagon_area(side):
    """
    calculate the area of a regular hexagon
    :param side:  the side
    :return: the area(unit^2 from side)
    >>>regular_hexagon_area(5)
    64.9519052838329
    """
    return (3 * math.sqrt(3) * side ** 2) / 2

print(regular_hexagon_area(5))
