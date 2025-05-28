
import functools
import math


class Point:

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __add__(self, other: "Point, int"):
        if isinstance(other, Point):
            # Point
            new_point = Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            # int
            new_point = Point(self.x + other, self.y + other)
        elif isinstance(other, tuple):
            # tuple
            new_point = Point(self.x + other[0], self.y + other[1])
        else:
            raise TypeError(f'Point class does not support add for type {type(other)}')
        return new_point

    def __sub__(self, other: "Point, int"):
        if isinstance(other, Point):
            # Point
            new_point = Point(self.x - other.x, self.y - other.y)
            # new_point = self + (other.x *  -1, other.y * -1)
        elif isinstance(other, (int, float)):
            # int
            new_point = Point(self.x - other, self.y - other)
        elif isinstance(other, tuple):
            # tuple
            new_point = Point(self.x - other[0], self.y - other[1])
        else:
            raise TypeError(f'Point class does not support add for type {type(other)}')
        return new_point

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_point = Point(self.x * other, self.y * other)
        else:
            raise TypeError(f'Point class does not support add for type {type(other)}')
        return new_point

    # p1 == p2
    # self == other
    # p1 == (3,3)
    # p1 == 4 like (4,4)
    def __eq__(self, other):
        print('__eq__')
        # * eq requires hash
        # * when 2 objects are equal their hash value needs to be also equals
        # * p1 == p2 ? True -> the hash value should be the same
        if isinstance(other, Point):
            # Point
            return self.x == other.x and self.y == other.y
        elif isinstance(other, (int, float)):
            # int, float
            return self.x == other and self.y == other
        elif isinstance(other, tuple):
            # tuple
            return self.x == other[0] and self.y == other[1]
        else:
            raise TypeError(f'Point class does not support == for type {type(other)}')

    def __ne__(self, other):
        if not isinstance(other, Point) and not isinstance(other, (int, float)) and not isinstance(other, tuple):
            raise TypeError(f'Point class does not support != for type {type(other)}')
        return not self == other

    # >
    def __gt__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f'Point class does not support > for type {type(other)}')
        dist_self = math.sqrt(self.x ** 2 + self.y ** 2)
        dist_other = math.sqrt(other.x ** 2 + other.y ** 2)
        return dist_self > dist_other

    # >=
    def __ge__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f'Point class does not support >= for type {type(other)}')
        return self > other or self == other

    # <
    def __lt__(self, other):
        pass

    # <=
    def __le__(self, other):
        pass


    def __repr__(self):
        return f"Point ({self.x:.2f}, {self.y:.2f})"

    def __str__(self):
        return f"Point ({self.x:.2f}, {self.y:.2f})"

    # __del__




p1 = Point(2.0, 4.7)
p2 = Point(1.9, 5.5)

p3 = p1 + p2
print(p3)
print(p1 + p2)  # print(2+3)

# p3 = p1 + p2
# print(p3)
# print(p3 := p1 + p2)  # p3 = p1 + p2, print(p3)

p1 = p1 + 1  # Point(3.0, 5.7)
print(p1)
print(p1 + (2, 9))  # (5.0, 14.7)
print(p1 - (3.4, 3.4))
print("p1 - p2 = ", p1 - p2)
print("p1 * 2 =", p1 * 2)
p1 = Point(3.5, 4.7)
p2 = Point(3.5, 4.7)
print("p1:", p1)
print("p2:", p2)
# print(f"p1 == p2? {p1 == p2}")
# print(f"p1 == (3.5, 4.7)? {p1 == (3.5, 4.7)}")
# print(f"p1 == 4? {p1 == 4}")
# p3 = Point(3.5, 4.7)
print('p3 == p1?', p3 == p1)  # True

# print('p3 != p1?', p3 != "a")  # Error
print('p3 != p1?', p3 != p1)  # False
# option 1- do not implement __ne__ -- python will return not __equal__
# option 1- implement __ne__ manually

print('p1 > p2', p1 > p2)
print('p1 >= p2', p1 >= p2)