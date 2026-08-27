def plus_minus(x):
    yield x
    yield -x

# I really hate this damn machine
# I wish that I could sell it.
# It never does quite what I want
# But only what I tell it.

def cycle(s):
    """Iterate over the elements of s repeatedly.
    """
    print("starting generator")
    while True:
        for x in s:
            print("before yield")
            yield x
            print("after yield")
        print("finished one loop")




for x in obj:
    print(x)


it = iter(obj)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(it)






### More Tree Practice

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

#          2
#         /  \
#       3      5
#      / \    / \
#     0   1  2   4
#    / \   \
#   6   2   4

def print_nodes(t) -> bool:
    "Print all labels of a tree."
    for branch in branches(t):
        print_nodes(branch)
    
    print(label(t))