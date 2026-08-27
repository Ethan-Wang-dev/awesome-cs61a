########### Warm-Up ############
# >>> r = Rational(1, 2)
# >>> r
# What will be shown on the terminal?

# Would eval(repr(r)) be the same thing as r?
# Hint: Use documentation for the parts of this question
# you don't know about. 
class Rational:
    # Constructor/Initializer
    def __init__(self, n, d):
        # Selectors
        self.numer = n
        self.denom = d

    # Operations/Methods
    def __mul__(self, r):
        return Rational(self.numer *r.numer, self.denom * r.denom)
    def __str__(self):
        return f"{self.numer}/{self.denom}"
    def __repr__(self):
        return f"Rational({self.numer}, {self.denom})"
    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom


class Transaction:
    """ A transaction describes a change in an account.

    >>> t = Transaction(3, 20, 10)
    >>> print(t)
    3: decreased 20->10

    >>> t0 = Transaction(0, 20, 10)
    >>> t1 = Transaction(1, 20, 20)
    >>> t0 == t1
    False
    >>> t0.__eq__(t1)
    False
    >>> bool(t0)
    True
    >>> t0.__bool__()
    True
    """
    def __init__(self, id: int, before: int, after: int):
        self.id = id
        self.before = before
        self.after = after

    def changed(self) -> bool:
        """Return whether the transaction resulted in a changed balance."""
        return self.before != self.after

    def report(self) -> str:
        """Return a string describing the transaction.

        >>> Transaction(3, 20, 10).report()
        '3: decreased 20->10'
        >>> Transaction(4, 20, 50).report()
        '4: increased 20->50'
        >>> Transaction(5, 50, 50).report()
        '5: no change'
        """
        msg: str = 'no change'
        if self.changed():
            if self.before < self.after:
                msg = f'increased {self.before}->{self.after}'
            else:
                msg = f'decreased {self.before}->{self.after}' 
        return str(self.id) + ': ' + msg
    
    def __str__(self):
        """Returns the report string of a Transaction."""
        return self.report()

    def __repr__(self):
        return f"Transaction({self.id}, {self.before}, {self.after})"

    def __eq__(self, other):
        return self.id == other.id and self.before == other.before and self.after == other.after
    def __bool__(self):
        return self.changed()
    

class Letter:
    """
    >>> hi = Letter('Hello, World!')
    >>> hi.send()
    Letter('Hello, World!') has been sent.
    Letter('HELLO, WORLD!')
    >>> hi.send()
    Letter('Hello, World!') was already sent.
    >>> Letter('Hey').send().send()
    Letter('Hey') has been sent.
    Letter('HEY') has been sent.
    Letter('HEY')
    """
    def __init__(self, contents: str):
        self.contents = contents
        self.sent = False

    def send(self):
        if self.sent:
            print(self, 'was already sent.')
        else:
            print(self, 'has been sent.')
            self.sent = True
            return Letter(self.contents.upper())

    def __repr__(self):
        return f'Letter({repr(self.contents)})'
