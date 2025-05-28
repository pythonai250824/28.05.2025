
class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

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

    def __sub__(self, other):
        pass

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

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