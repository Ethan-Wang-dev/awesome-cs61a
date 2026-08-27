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

########### Warm-Up ############
# Assume we use our list representation for the
# following tree
# What order will the labels be printed in?
#          2
#         /  \
#       3      5
#      / \    / \
#     0   1  4   2
#    / \   \
#   6   2   4

def print_nodes(t):
    "Print all labels of a tree."
    for branch in branches(t):
        print_nodes(branch)
    
    print(label(t))

class Tree:
    #Constructor
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches

    def __iter__(self):
        for branch in self.branches:
            #yield from branch
            #     ||
            for label in iter(branch):
                yield label
        
        yield self.label

    

t = Tree(2, 
            [Tree(3, 
                [Tree(0, [
                        Tree(6),
                        Tree(2)
                ]),
                 Tree(1, [
                        Tree(4)
                 ])]), 
             Tree(5, [
                    Tree(4),
                    Tree(2)
             ])])

def print_nodes(t):
    "Print all labels of a tree."
    print(t.label)
    for branch in t.branches:
        print_nodes(branch)
    