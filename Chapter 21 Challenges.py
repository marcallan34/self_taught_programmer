#Chapter 21 Challenges

#Challenge 1: reverse the string 'yesterday' using a stack

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

stack = Stack()

for c in 'yesterday':
    stack.push(c)

reversed_string = ''

for i in range(len(stack.items)):
    reversed_string += stack.pop()

print(reversed_string)

#Challenge 2: use a stack to make a new list that reverses the list [1, 2, 3, 4, 5]

list1 = [1, 2, 3, 4, 5]
list2 = []

stack2 = Stack()

for item in list1:
    stack.push(item)

for j in range(len(stack.items)):
    list2.append(stack.pop())

print(list2)



