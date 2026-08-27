# Nim

def play(strategy1, strategy2, n=10):
    """Play N-to-0-by-1-or-2 and return the index of the next player to play (here the loser).
    Here we'll allow a strategy to take 2 from 1 just to keep it simple.

    >>> play(two_strat, two_strat)
    2
    """
    who = 1  # Player 1 goes first
    while n > 0:
        if who == 1:
            n = n - strategy1(n)
        elif who == 2:
            n = n - strategy2(n)
        else:
            sys.exit("Error in play: who had a different value than 1 or 2")
        who = 3 - who # the easy way to switch players 1<->2
    return who  # The player whose turn it is

def two_strat(n):
    return 2

def one_strat(n):
    return 1

#print(play(two_strat, two_strat))

def noisy_strat(who, s):
    """A strategy that prints its choices.

    >>> play(noisy_strat(1, two_strat), noisy_strat(2, two_strat))
    Player 1 took 2 from 10 to reach 8
    Player 2 took 2 from 8 to reach 6
    Player 1 took 2 from 6 to reach 4
    Player 2 took 2 from 4 to reach 2
    Player 1 took 2 from 2 to reach 0
    2
    """
    def strat(n):
        choice = s(n)
        print('Player', who, 'took', choice, 'from', n, 'to reach', n-choice)
        return choice
    return strat

def interactive_strat(n):
    choice = 0
    while choice < 1 or choice > 2:
        print('How much will you take', n, '(1-2)?', end=' ')
        choice = int(input())
    return choice

print(play(noisy_strat(1, one_strat), noisy_strat(2, two_strat)))