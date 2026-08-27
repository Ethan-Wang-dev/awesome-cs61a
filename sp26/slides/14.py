
######################### REPRESENTATIONS ######################
#Constructor
def tree(label, branches=[]):
    "Return a tree"
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

#Selectors
def label(tree):
    "Return the root label"
    return tree[0]

def branches(tree):
    "Return a list of branches"
    return tree[1:]

def is_tree(tree):
    "Return true if the argument tree is a correctly formed tree"
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    "Return true if the given tree has no branches"
    return not branches(tree)


#          #### +++ === ABSTRACTION BARRIER === +++ ####        #


############################ OPERATIONS ########################


def print_leaves(t):
    """Print the leaves of a tree."""
    # Use label(t) and branches(t) to fill out the rest
    
    if is_leaf(t):
        print(label(t))
    else:
        for branch in branches(t):
            print_leaves(branch)











t = tree(1, 
         [tree(9, [
             tree(2, [
                 tree(5, [
                     tree(6), 
                     tree(7)]), 
                 tree(8), 
                 tree(3)]), 
             tree(4)])])

#          1
#          |
#          |
#          9
#        /   \
#       2     4
#      /|\
#     5 8 3
#    / \
#    6  7

# the number 4
label(branches(branches(t)[0])[1])

# Examples

def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def largest_label(t):
    """Return the largest label in tree t.

    >>> t = tree(3, [tree(-1), tree(2, [tree(4, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> print_tree(t) 
    3
      -1
      2
        4
          1
        3
      1
        -1
    >>> largest_label(t)
    4
    """
    if is_leaf(t):
        return label(t)
    else:
        return max([label(t)] + [largest_label(b) for b in branches(t)])

def above_root(t):
    """Print all the labels of t that are larger than the root label.

    >>> t = tree(3, [tree(-1), tree(2, [tree(4, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> print_tree(t) 
    3
      -1
      2
        4
          1
        3
      1
        -1
    >>> above_root(t)
    4
    >>> above_root(branches(t)[1])
    4
    3
    """
    def process(u):
        if label(u) > label(t):
            print(label(u))
        for b in branches(u):
            process(b)
    process(t)





