import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


with open('/usr/share/dict/words') as f:
    dict_words = f.read().splitlines()



################# Warm-Up #################
# Both functions take in a list of words and
# a length and return a list of the original
# words filtered to be shorter than the given
# length.

# Which implementation will typically run
# faster? Why?
@timer
def remove_long_words(words, length):
    new_words = words[:]

    for word in words:
        if len(word) >= length:
            new_words.remove(word)

    return new_words
@timer
def add_short_words(words, length):
    new_words = []

    for word in words:
        if len(word) < length:
            new_words.append(word)
    
    return new_words




alternate = ['hi', 'hello']*25000

# words = add_short_words(alternate, 4)
# words = remove_long_words(alternate, 4)

# words = remove_long_words(dict_words, 5)
# words = add_short_words(dict_words, 5)




class Link:
    """A linked list.

    >>> Link(1, Link(4, Link(1)))
    Link(1, Link(4, Link(1)))
    >>> Link(1, Link(4, Link(1, Link.empty)))
    Link(1, Link(4, Link(1)))
    >>> Link(1, Link(4, Link(1, 5)))
    Traceback (most recent call last):
        ...
    AssertionError
    >>> Link(1, Link(4, Link(1, Link(5))))
    Link(1, Link(4, Link(1, Link(5))))
    >>> s = Link(1, Link(4, Link(1, Link(5))))
    >>> t = s
    >>> Link(3, s)
    Link(3, Link(1, Link(4, Link(1, Link(5)))))
    >>> s
    Link(1, Link(4, Link(1, Link(5))))
    >>> s = Link(3, s)
    >>> s
    Link(3, Link(1, Link(4, Link(1, Link(5)))))
    >>> t
    Link(1, Link(4, Link(1, Link(5))))
    >>> s.rest is t
    True
    >>> s.append(2)
    Traceback (most recent call last):
        ...
    AttributeError: 'Link' object has no attribute 'append'
    >>> s
    Link(3, Link(1, Link(4, Link(1, Link(5)))))
    >>> s.rest
    Link(1, Link(4, Link(1, Link(5))))
    >>> s.rest.rest
    Link(4, Link(1, Link(5)))
    >>> s.rest.rest.rest
    Link(1, Link(5))
    >>> s.rest.rest.rest.rest
    Link(5)
    >>> s.rest.rest.rest.rest.rest
    ()
    >>> s.rest.rest.rest.rest.rest = Link(2)
    >>> s
    Link(3, Link(1, Link(4, Link(1, Link(5, Link(2))))))
    >>> t
    Link(1, Link(4, Link(1, Link(5, Link(2)))))
    >>> print(s)
    (3 1 4 1 5 2)
    >>> (3, (1, (4, (1, (5, 2)))))
    (3, (1, (4, (1, (5, 2)))))
    >>> type(s) == Link
    True
    >>> type(s) == tuple
    False
    >>> print(t)
    (1 4 1 5 2)
    >>> print(s.rest)
    (1 4 1 5 2)

    >>> from fractions import Fraction
    >>> u = Link(1, Link('hello', Link(None, Link(Fraction(1, 3)))))
    >>> print(u)
    (1 hello None 1/3)
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '('
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + ')'


def double(s, v):
    """Insert another v after each v in s.

    >>> s = [2, 7, 1, 8, 2, 8]
    >>> double(s, 8)
    >>> s
    [2, 7, 1, 8, 8, 2, 8, 8]
    """
    i = 0
    while i < len(s):
        if s[i] == v:
            s.insert(i+1, v)
            i += 2
        else:
            i += 1

def double_link(s, v):
    """Insert another v after each v in s.

    >>> s = Link(2, Link(7, Link(1, Link(8, Link(2, Link(8))))))
    >>> double_link(s, 8)
    >>> print(s)
    (2 7 1 8 8 2 8 8)
    """
    while s is not Link.empty:
        if s.first == v:
            s.rest = Link(v, s.rest)
            s = s.rest.rest
        else:
            s = s.rest
