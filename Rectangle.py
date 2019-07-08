from colour import Color


class Rectangle:
    def __init__(self, colour = Color("green"), height = 1, width = 2):
        self.__height = height
        self.__colour = colour
        self.__width = width


    def get_colour(self):
        return self.__colour


    def get_width(self):
        return self.__width


    def get_height(self):
        return self.__height


    def __add__(self, other):
        return Rectangle(self.__colour, \
                    max(float(self.__height),float(other.get_height())), \
                    max(float(self.__width), float(other.get_width())))
        self.__colour
    def __str__(self):
        return "Rectangle colour is " + str(self.__colour)\
               + ", width is " + str(self.__width)\
                + " and height is " + str(self.__height)


if __name__ == '__main__':
    r = Rectangle("red", 3, 15)
    r2 = Rectangle("Green", 5, 12)
    r3 = r +r2
    print(r)
    print(r2)
    print(r3)