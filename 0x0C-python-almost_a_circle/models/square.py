#!/usr/bin/python3
"""Model: Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
            self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


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
        """ Returns dictionary object """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
