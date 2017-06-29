#Chapter 12 Challenges
import math

#Challenge 1
class Apple():
    def __init__(self, s, c, o, a):
        self.size = s
        self.color = c
        self.organic = o
        self.age = a

#Challenge 2

class Circle():
    def __init__(self,r):
        self.radius = r

    def calculate_area(self):
        return self.radius** 2 *math.pi

circle1 = Circle(15)
print(circle1.calculate_area())

#Challenge 3

class Triangle():
    def __init__(self,l, w):
        self.len = l
        self.width = w

    def calculate_area(self):
        return (self.width*self.len)/2

triangle1 = Triangle(4, 8)
print(triangle1.calculate_area())

#Challenge 4

class Hexagon():
    def __init__(self, a):
        self.side_length = a

    def calculate_area(self):
        return self.side_length*6

hex1 = Hexagon(4)
print(hex1.calculate_area())




    
