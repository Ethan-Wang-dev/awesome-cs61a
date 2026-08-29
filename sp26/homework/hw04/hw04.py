def shuffle(s):
    """Return a shuffled list that interleaves the two halves of s.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> shuffle(letters)
    ['a', 'e', 'b', 'f', 'c', 'g', 'd', 'h']
    >>> shuffle(shuffle(letters))
    ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
    >>> letters  # Original list should not be modified
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    assert len(s) % 2 == 0, 'len(seq) must be even'
    ss = list(s)
    if ss == []:
        return []
    s0 = ss[:len(ss)//2]
    s1 = ss[len(ss)//2:]
    res = []
    while s0 != [] and s1 != []:
        if len(s0) == len(s1):
            res.append(s0[0])
            s0 = s0[1:]
        else:
            res.append(s1[0])
            s1 = s1[1:]
    res.append(s1[0])
    return res


def deep_map(f, s):
    """Replace all non-list elements x with f(x) in the nested list s.

    >>> six = [1, 2, [3, [4], 5], 6]
    >>> deep_map(lambda x: x * x, six)
    >>> six
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    # if type(s[0]) == list:
    #     if len(s[0]) > 1: # [3, ...]
    #         return [deep_map(f, s[0][0]), deep_map(f, s[0][1:])]
    #     else: # [4]
    #         return [f(s[0])]
    # elif type(s[0]) != list: # number 1
    #     if len(s) > 1:
    #         return [f(s[0])].append(deep_map(f, s[1:]))
    #     else:
    #         return f(s[0])
    for i in range(len(s)):
        if type(s[i]) == list:
            deep_map(f, s[i])
        else:
            s[i] = f(s[i])
    ### A recursive version
    # def walk(i):
    #     if i == len(s):
    #         return
    #     if type(s[i]) == list:
    #         deep_map(f, s[i])
    #     else:
    #         s[i] = f(s[i])
    #     walk(i + 1)
    # walk(0)


SOURCE_FILE = __file__


def planet(mass):
    """Construct a planet of some mass."""
    assert mass > 0
    return ['planet', mass]

def mass(p):
    """Select the mass of a planet."""
    assert is_planet(p), 'must call mass on a planet'
    return p[1]

def is_planet(p):
    """Whether p is a planet."""
    return type(p) == list and len(p) == 2 and p[0] == 'planet'

def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return t, u, v

def total_mass(m):
    """Return the total mass of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_mass(t)
    3
    >>> total_mass(u)
    6
    >>> total_mass(v)
    9
    """
    if is_planet(m):
        return mass(m)
    else:
        assert is_mobile(m), "must get total mass of a mobile or a planet"
        return total_mass(end(left(m))) + total_mass(end(right(m)))

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> p = mobile(arm(3, t), arm(2, u))
    >>> balanced(p)
    False
    >>> balanced(mobile(arm(1, v), arm(1, p)))
    False
    >>> balanced(mobile(arm(1, p), arm(1, v)))
    False
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(SOURCE_FILE, 'balanced', ['Index'])
    True
    """
    # if is_planet(m):
    #     return True
    # if is_mobile(m):
    #     l = end(left(m))
    #     r = end(right(m))
    #     l_len = length(left(m))
    #     r_len = length(right(m))
    #     # 两臂上都是planet
    #     if is_planet(l) and is_planet(r):
    #         l_mass = mass(l)
    #         r_mass = mass(r)
    #         return l_mass * l_len == r_mass * r_len
    #     # 两臂都是mobile
    #     if is_mobile(l) and is_mobile(r):
    #         return (total_mass(l) * l_len == total_mass(r) * r_len) and balanced(l) and balanced(r)
    #     # 一臂planet，一臂mobile
    #     is_m = l if is_mobile(l) else r
    #     is_p = l if is_planet(l) else r
    #     m_len = length(is_m)
    #     p_len = length(is_p)
    #     return (total_mass(is_m) * m_len == mass(is_p) * p_len) and balanced(is_m) and balanced(is_p)
    if is_planet(m):
        return True
    if is_mobile(m):
        l = end(left(m))
        r = end(right(m))
        l_m = total_mass(l)
        r_m = total_mass(r)
        l_l = length(left(m))
        r_l = length(right(m))
        return balanced(l) and balanced(r) and (l_m * l_l == r_m * r_l)



def prune_leaves(t, vals):
    """Return a version of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    if is_leaf(t):
        if label(t) in vals:
            return None
        else:
            return t
    if is_tree(t):
        purned_bs = []
        for b in branches(t):
            purned_b = prune_leaves(b, vals)
            if purned_b is not None:
                purned_bs.append(purned_b)
        return tree(label(t), purned_bs)


SOURCE_FILE = __file__


def max_path_sum(t):
    """Return the maximum root-to-leaf path sum of a tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t) # 1, 10
    11
    >>> t2 = tree(5, [tree(4, [tree(1), tree(3)]), tree(2, [tree(10), tree(3)])])
    >>> max_path_sum(t2) # 5, 2, 10
    17
    """
    if is_leaf(t):
        return label(t)
    # t is tree
    label_bs = []
    for b in branches(t):
        label_bs.append(max_path_sum(b))
    return max(label_bs) + label(t)


def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be an arm"
    assert is_arm(right), "right must be an arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    """Construct an arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is an arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of an arm."""
    assert is_arm(s), "must call length on an arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of an arm."""
    assert is_arm(s), "must call end on an arm"
    return s[2]



# Tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

