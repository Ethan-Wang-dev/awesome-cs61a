#################### WARM-UP ##################
# Here is a function that takes in a list and prints each of its elements.
def print_elts(x):
    for elt in x:
        print(elt)

# What would you need to change about this code to make it work for tuples
# instead of lists?

# What would you need to change for it to take in a string and print each
# of its letters?





# s = [[1, 2], 3, 4, 5]
# next(s)

# t = iter(s)
# next(t)
# # [1, 2]
# next(t)
# # 3
# u = iter(s)
# next(u)
# # [1, 2]

# list(t)
# [4, 5]

# >>> a = [1, 2, 3]
# >>> b = [a, 4]
# >>> c = iter(a)
# >>> d = c
# >>> print(next(c))
# 1
# >>> print(next(d))
# 2
# >>> b
# [[1, 2, 3], 4]















def list_mutation_demos():
    s = [2, [3, 4], 5]
    s.append([6, 7])
    s.extend([8, 9])
    t = []
    t.extend(s)
    u = list(s)

    
def tuple_demos():
    (3, 4, 5, 6)
    3, 4, 5, 6
    ()
    tuple()
    tuple([1, 2, 3])
    # tuple(2)
    (2,)
    (3, 4) + (5, 6)
    (3, 4, 5) * 2
    5 in (3, 4, 5)

    # {[1]: 2}
    {1: [2]}
    {(1, 2): 3}
    # {([1], 2): 3}
    {tuple([1, 2]): 3}

def iterator_demos():
    """Using iterators

    >>> s = [[1, 2], 3, 4, 5]
    >>> next(s)
    Traceback (most recent call last):
        ...
    TypeError: 'list' object is not an iterator
    >>> t = iter(s)
    >>> next(t)
    [1, 2]
    >>> next(t)
    3
    >>> u = iter(s)
    >>> next(u)
    [1, 2]
    >>> list(t)
    [4, 5]

    >>> a = [1, 2, 3]
    >>> b = [a, 4]
    >>> c = iter(a)
    >>> d = c
    >>> print(next(c))
    1
    >>> print(next(d))
    2
    >>> b
    [[1, 2, 3], 4]
    """

def average(s):
    """Return the average of values in a list.

    >>> average([3, 4, 5, 6])
    4.5
    >>> average(map(lambda x: x * x, [3, 4, 5, 6]))
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return sum(s) / len(list(s))

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

def map_demo():
    """Using built-in sequence functions.

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> caps = map(lambda x: x.upper(), bcd)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    >>> all(map(double, range(-3, 3)))
    *** -3 => -6 ***
    *** -2 => -4 ***
    *** -1 => -2 ***
    *** 0 => 0 ***
    False
    """