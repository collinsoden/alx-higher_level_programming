#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
        try:
            self.__position = position
            if type(position) is not tuple:
                raise TypeError
            if len(position) != 2:
                raise TypeError
            if position[0] < 0 or position[1] < 0:
                raise TypeError
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """This method retrieves the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        try:
            self.__size = value
            if value < 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """This method retrieves the position of a square."""
        return self.__position

    @position.setter
    def position(self, value):
          try:
            self.__position = value
            if type(value) is not tuple:
                raise TypeError
            if len(value) != 2:
                raise TypeError
            if value[0] < 0 or value[1] < 0:
                raise TypeError
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """int: Return area of square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square"""
        s = self.__size
        pos = self.__position
        p1 = pos[0]
        p2 = pos[1]
        if s == 0:
            print()
        else:
            for ii in range(p2):
                    print()
            for i in range(s):
                for j in range(p1):
                    print(" ", end='')
                for j in range(s):
                    print("#", end='')
                print()
