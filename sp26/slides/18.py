# Constructor for functional representation of rational
def func_rational(n, d):
    return lambda choice: n if choice == 'n' else d
# Selectors
def numer(r):
    return r('n')
def denom(r):
    return r('d')
#Operation
def mul_rationals(r, q):
    return func_rational(numer(r)*numer(q), denom(r)*denom(q))

##########################################################

# Constructor for list representation of rational
def list_rational(n, d):
    return [n,d]
# Selectors
def numer(r):
    return r[0]
def denom(r):
    return r[1]

############### ABSTRACTION BARRIER #################

#Operation
def mul_rationals(r, q):
    return list_rational(numer(r)*numer(q), denom(r)*denom(q))

def add_rationals(r,q):
    pass

########### Warm-Up ############
# What is the *first* line that
# goes wrong when running this
# code?

# f1 = func_rational(2,3)
# f2 = func_rational(1,5)
# numer(f1)
# denom(f2)

# l1 = list_rational(2,3)
# l2 = list_rational(1,5)
# numer(l2)
# numer(f1)

# r = mul_rationals(l1, l2)
# print(r)

# q = mul_rationals(f1, f2)
# print(q)








class Rational:
    # Constructor/Initializer
    def __init__(self, n, d):
        # Selectors
        self.numer = n
        self.denom = d
        self.greeting = "hello"
        self.secret = "super secret passphrase"

    # Operations/Methods
    def __mul__(self, r):
        return Rational(self.numer *r.numer, self.denom * r.denom)
    def say_hello(self):
        print(self.greeting)
    def __repr__(self):
        return f"{self.numer}/{self.denom}"
    
