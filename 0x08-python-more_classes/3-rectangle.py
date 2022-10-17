#!/usr/bin/python3
"""
    Module contains of a single class
"""


class Rectangle:
    """Defines a reactangle"""

    def __init__(self, width=0, height=0):
        """Initializing instance data"""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def __str__(self):
        """Prints rectangle with `#` character"""
        string = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                string.append("#")
            if i < (self.__height - 1):
                string.append("\n")
        return "".join(string)

    @property
    def width(self):
        """Retrieves of `width` value """
        return self.__width

    @property
    def height(self):
        """Retrieves `height` value"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the value of atribute `width` to a new value"""
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets atribute `height` to a new value"""
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a reactangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of a reactangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)