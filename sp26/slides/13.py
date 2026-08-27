######################### REPRESENTATIONS ######################

######### Functional Rep
#Constructor
# def rational(n, d):
#     """Construct rational number representing n/d."""

#     def top_or_bottom(choice):
#         if choice == 'n':
#             return n
#         elif choice == 'd':
#             return d
        
#     return top_or_bottom

# #Selectors
# def numer(x):
#     """Get numerator of rational x."""
#     return x('n')

# def denom(x):
#     """Get denominator of rational x."""
#     return x('d')



# ######### List Rep
#Constructor
def rational(n, d):
    return [n,d]

#Selectors
def numer(x):
    """Get numerator of rational x."""
    return x[0]

def denom(x):
    """Get denominator of rational x."""
    return x[1]




################ +++ === ABSTRACTION BARRIER === +++ ###########

############################ OPERATIONS ########################
def mul_rationals(x, y):
    "Multiply rationals x and y."
    xn, yn = numer(x), numer(y)
    xd, yd = denom(x), denom(y)

    return rational(xn*yn, xd*yd)

def add_rationals(x,y):
    pass

def equals_rationals(x,y):
    pass



