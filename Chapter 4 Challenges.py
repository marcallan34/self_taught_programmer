#Chapter 4 challenges

#Challenge 1

def squared(x):
    """
    Returns variable x squared.
    :param x: int, or float.
    :return: int of x squared.
    """
    return x**x

print(squared(3))

#Challenge 2
def print_string(s):
    """
    Prints string s.
    :param s: string.
    :prints string s.
    """
    print(s)

print_string('Testing')

#Challenge 3
def parameter_functions(x,y,z, a=2, b=4):
    """
    Prints ((x+y)-(z+a)*b) with the option to change parameters a and b. Other they will be 2 and 4 respectively
    :param x: int or float.
    :param y: int or float.
    :param z: int or float.
    :param a: int or float.
    :param b: int or float.
    return: ((x+y)-(z+a)*b)
    """
    print((x+y)-(z+a)*b)

parameter_functions(2,3,1)

#challenge 4
def times_two(x):
    """
    Returns x*2
    :param x :int or float
    :return
    :return product of x and the int 2
    """

def times_four(y):
    """
    Returns y*4
    :param y: int or float
    :return: int or float product of y and 4
    """
    return y*4

first_test = times_two(2)

print(times_four(first_test))

#challenge 5
def to_float(string):
    try:
        return float(string)
    except ValueError:
        print('not a number')

print(to_float('5'))

#challenge 6

#wrote docstrings for all functions in this chapter








