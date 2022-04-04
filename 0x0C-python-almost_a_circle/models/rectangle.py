#!/usr/bin/python3
"""Model: rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializaton of object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ return standard print of class """
        msg = "[Rectangle] ({}) {}/{} - {}/{}"
        return msg.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter `height` private attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return rectangle area """
        return self.height * self.width

    def display(self):
        """Prints in stdout the Rectangle instance with the character #
        """
        print(("\n" * self.y), end="")
        """suggest to exchg `end=""` to [:-1]"""
        print((" " * self.x + (self.width * "#") + '\n') * self.height, end="")

    def update(self, *args, **keywords):
        """
        Updates instance of rectangle.
        Argument count funct, assigns an argument to each attribute
        """
        count = 0
        if args:
            while count < len(args):
                if count == 0:
                    self.id = args[count]
                if count == 1:
                    self.width = args[count]
                if count == 2:
                    self.height = args[count]
                if count == 3:
                    self.x = args[count]
                if count == 4:
                    self.y = args[count]
                count += 1
        else:
            for input_arg in keywords:
                setattr(self, input_arg, keywords.get(input_arg))

    def to_dictionary(self):
        """Returns dictionary object """
        return {
                'x': self.__x,
                'y': self.__y,
                'id': self.id,
                'height': self.__height,
                'width': self.__width
                }
