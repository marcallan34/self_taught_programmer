#Chapter 13 Challenges

#Challenge 1 'Create Rectangle and Square Classes with a method called
# calculate_perimeter that calculates the perimeter of the shapes they represent
# Create Rectangle and Square objects and call the method on both of them

class Shape():
    def what_am_i(self):
        print('I am a Shape.')

class Rectangle(Shape):
    def __init__(self, l, w):
        self.len = l
        self.width = w

    def calculate_perimeter(self):
        return (self.len*2) + (self.width*2)

class Square(Shape):
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len*4

    def change_size(self, n):
        self.len = self.len + n

rectangle1 = Rectangle(2, 4)
square1 = Square(4)

print(rectangle1.calculate_perimeter())
print(square1.calculate_perimeter())
square1.what_am_i()
rectangle1.what_am_i()

#Challenge 2: Define a method in your Square class called change_size that
#allows you to pass in a number that increases or decreases(if the number is
# negative) each side of a Square object by that number

#Challenge 3: Create a class called Shape. Define a method in it called
#what_am_i that prints "I am a shape" when called. Change your Square and
#Rectangle classes from the previous challenges to inherit from Shape,
#create Square and Rectangle objects, and call the new method on both of them.

#Challenge 4: Create a class called Horse and a class called Rider.
#Use composition to model a horse that has a rider.

class Horse():
    def __init__(self,name, color, rider):
        self.name = name
        self.color = color
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

johnny = Rider('johnny paycheck')
mr_ed = Horse('Mr. Ed', 'brown', johnny)

print(mr_ed.rider.name)







