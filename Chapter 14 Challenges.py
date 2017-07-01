#Chapter 14 Challenges

#Challenge 1
#Add a square_list class variable to a class called Square so that every time
#you create a new Square object, the new object gets added to the list.

class square():
    square_list = []

    def __init__(self, s):
        self.side_length = s
        self.square_list.append(self.side_length)
#Challenge 2
#Change the Square class so that when you print a Square object,
#a message prints telling you the len of each of the four sides of the shape.
#For example, if you create a square with Square( 29) and print it,
#Python should print 29 by 29 by 29 by 29.'''
    def __repr__(self):
        return'{} by {} by {} by {}'.format(self.side_length, self.side_length, self.side_length, self.side_length,)

#Challenge 3
#Write a function that takes two objects as parameters and returns True
#if they are the same object, and False if not.

def are_they_the_same(x,y):
    if x is y:
        print('these bjects are the same')
    else:
        print('these objects are not the same')

#alternatively:

def compare(x,y):
    return x is y
