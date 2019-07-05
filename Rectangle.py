from colour import Color


class Rectangle:
    def __init__(self, colour = Color("green"), height = 1, width = 2):
        self.__height = height
        self.__colour = colour
        self.__width = width
    def __str__(self):
        return "Rectangle colour is " + str(self.__colour)\
               + ", width is " + str(self.__width)\
                + " and height is " + str(self.__height)


r = Rectangle("red", 3, 15)
print(r)