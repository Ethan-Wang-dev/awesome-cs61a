SOURCE_FILE = __file__


def close(s: list[int], k: int) -> int:
    """Return how many elements of s are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close(t, 0)  # Only 3 is equal to its index
    1
    >>> close(t, 1)  # 2, 3, and 5 are within 1 of their index
    3
    >>> close(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    4
    >>> close(list(range(10)), 0)
    10
    """
    assert k >= 0
    count = 0
    for i in range(len(s)):  # Use a range to loop over indices
        "*** YOUR CODE HERE ***"
    return count


def close_list(s: list[int], k: int) -> list[int]:
    """Return a list of the elements of s that are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close_list(t, 0)  # Only 3 is equal to its index
    [3]
    >>> close_list(t, 1)  # 2, 3, and 5 are within 1 of their index
    [2, 3, 5]
    >>> close_list(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    [2, 4, 3, 5]
    """
    assert k >= 0
    return [___ for i in range(len(s)) if ___]


def double_eights(n: int) -> bool:
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> # ban iteration, in operator and str function 
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'double_eights', ['While', 'For', 'In', 'Str'])
    True
    """
    "*** YOUR CODE HERE ***"


def make_onion(f, g):
    """Return a function can_reach(x, y, limit) that returns
    whether some call expression containing only f, g, and x with
    up to limit calls will give the result y.

    >>> up = lambda x: x + 1
    >>> double = lambda y: y * 2
    >>> can_reach = make_onion(up, double)
    >>> can_reach(5, 25, 4)      # 25 = up(double(double(up(5))))
    True
    >>> can_reach(5, 25, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)     # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)   # Not possible
    False
    """
    def can_reach(x, y, limit):
        if limit < 0:
            return ____
        elif x == y:
            return ____
        else:
            return can_reach(____, ____, limit - 1) or can_reach(____, ____, limit - 1)
    return can_reach


def make_func_repeater(f, x):
    """
    >>> increment_repeater = make_func_repeater(lambda x: x + 1, 1)
    >>> increment_repeater(2) #same as f(f(x))
    3
    >>> increment_repeater(5)
    6
    """
    def repeat(____):
        if ____:
            return ____
        else:
            return ____
    return ____


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952) # 7+3, 8+2, and 8+2
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469) # 9+1, 6+4, 6+4, 4+6, 1+9, 4+6 
    6
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'ten_pairs', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"


def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5) # digit 5 appears 4 times in 55055
    4
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

