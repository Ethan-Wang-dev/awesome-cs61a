"""Typing test implementation"""

from utils import (
    lower,
    split,
    remove_punctuation,
    lines_from_file,
    count,
    deep_convert_to_tuple,
)
from ucb import main, interact, trace
from datetime import datetime
import random


###########
# Phase 1 #
###########


def pick(paragraphs: list[str], select, k: int) -> str:
    """Return the Kth paragraph from PARAGRAPHS for which the SELECT function returns True.
    If there are fewer than K such paragraphs, return an empty string.

    Arguments:
        paragraphs: a list of strings representing paragraphs
        select: a function that returns True for paragraphs that meet its criteria
        k: an integer representing which paragraph to return

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    res_paras = [p for p in paragraphs if select(p)]
    if k <= len(res_paras) - 1:
        return res_paras[k]
    else:
        return ''
    # END PROBLEM 1


def about(keywords: list[str]):
    """Return a function that takes in a paragraph and returns whether
    that paragraph contains one of the words in keywords.

    Arguments:
        keywords: a list of keywords

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in keywords]), "keywords should be lowercase."

    # BEGIN PROBLEM 2
    def func(para_source: str):
        paras = split(remove_punctuation(para_source).lower())
        for k in keywords:
            if k in paras:
                return True
        return False
    return func
    # END PROBLEM 2


def accuracy(entered: str, source: str) -> float:
    """Return the accuracy (percentage of words entered correctly) of ENTERED
    compared to the corresponding words in SOURCE.

    Arguments:
        entered: a string that may contain typos
        source: a model string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    entered_words = split(entered)
    source_words = split(source)
    # BEGIN PROBLEM 3
    right = 0
    length = len(entered_words)
    if entered_words == [] and source_words == []:
        return 100.0
    elif entered_words == [] and source_words != []:
        return 0.0
    elif entered_words != [] and source_words == []:
        return 0.0
    for i in range(0, min(length, len(source_words))):
        if entered_words[i] == source_words[i]:
            right += 1
    return right / length * 100
    # END PROBLEM 3


def wpm(entered: str, elapsed: int) -> float:
    """Return the words-per-minute (WPM) of the ENTERED string.

    Arguments:
        entered: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, "Elapsed time must be positive"
    # BEGIN PROBLEM 4
    return len(entered) / 5 / (elapsed / 60)
    # END PROBLEM 4


################
# Phase 4 (EC) #
################


def memo(f):
    """A general memoization decorator."""
    cache = {}

    def memoized(*args):
        immutable_args = deep_convert_to_tuple(args)  # convert *args into a tuple representation
        if immutable_args not in cache:
            result = f(*immutable_args)
            cache[immutable_args] = result
            return result
        return cache[immutable_args]

    return memoized


def memo_diff(diff_function):
    """A memoization function."""
    cache = {}

    def memoized(entered, source, limit):
        # BEGIN PROBLEM EC
        key = (entered, source, limit)
        if key not in cache:
            cache[key] = diff_function(entered, source, limit)
        return cache[key]
        # END PROBLEM EC

    return memoized


###########
# Phase 2 #
###########


def autocorrect(entered_word: str, word_list: list[str], diff_function, limit: int) -> str:
    """Returns the element of WORD_LIST that has the smallest difference
    from ENTERED_WORD based on DIFF_FUNCTION. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    lowest difference is greater than LIMIT, return ENTERED_WORD instead.

    Arguments:
        entered_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    def get_min_diff(diff_lst: list[tuple]) -> tuple:
        assert diff_lst != [], "diff_lst 必然不为空"
        min_diff = diff_lst[0]
        for t in diff_lst:
            if t[2] < min_diff[2]:
                min_diff = t
        return min_diff
    # 若 entered_word 已经完整包含在 word_list 中了，返回 entered_word
    if entered_word in word_list:
        return entered_word
    # 若不包含 → 利用 diff_function 判断不同的程度
    diff_lst = []
    i = 0
    for w in word_list:
        diff_n =  diff_function(entered_word, w, limit)
        if diff_n <= limit:
            diff_lst.append((w, i, diff_n))
        i += 1
    # 若最低的不同程度的 word 高于 limit，则返回 entered_word 本身
    if diff_lst == []:
        return entered_word
    # 若存在多个 差异程度 相等的，返回 index 最靠前的 word
    return get_min_diff(diff_lst)[0]
    # END PROBLEM 5


def furry_fixes(entered: str, source: str, limit: int) -> int:
    """A diff function for autocorrect that determines how many letters
    in ENTERED need to be substituted to create SOURCE, then adds the difference in
    their lengths to this value and returns the result.

    Arguments:
        entered: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> furry_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> furry_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> furry_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> furry_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> furry_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    def count_diff(entered, source, now):
        if entered == '' or source == '':
            return abs(len(entered) - len(source))
        if now > limit:
            return 0
        if entered[0] != source[0]:
            return 1 + count_diff(entered[1:], source[1:], now+1)
        else:
            return count_diff(entered[1:], source[1:], now)
    return count_diff(entered, source, 0)
    # END PROBLEM 6


def minimum_mewtations(entered: str, source: str, limit: int) -> int:
    """A diff function for autocorrect that computes the edit distance from ENTERED to SOURCE.
    This function takes in a string ENTERED, a string SOURCE, and a number LIMIT.

    Arguments:
        entered: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if entered == source:
        return 0
    if limit < 0: # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        return limit + 1
        # END
    # Recursive cases should go below here
    if entered == '' or source == '':
        return abs(len(entered) - len(source))
    if entered[0] == source[0]: # Feel free to remove or add additional cases
        # BEGIN
        return 0 + minimum_mewtations(entered[1:], source[1:], limit)
        # END
    else:
        add = 1 + minimum_mewtations(
            entered, source[1:], limit - 1
        )
        remove = 1 + minimum_mewtations(
            entered[1:], source, limit - 1
        )
        substitute = 1 + minimum_mewtations(
            entered[1:], source[1:], limit - 1
        )
        # BEGIN
        return min(add, remove, substitute)
        # END


# Ignore the line below
minimum_mewtations = count(minimum_mewtations)


def final_diff(entered: str, source: str, limit: int) -> int:
    """A diff function that takes in a string ENTERED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, "Remove this line to use your final_diff function."


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(entered: list[str], source: list[str], user_id: int, upload) -> float:
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        entered: a list of the words entered so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> entered = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(entered, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    full_len = len(source)
    r = 0
    for e in entered:
        if e == source[r]:
            r += 1
        else:
            break
    ratio = r / full_len
    upload({'id': user_id, 'progress': ratio})
    return ratio
    # END PROBLEM 8


def time_per_word(words: list[str], timestamps_per_player: list[list[int]]) -> dict:
    """Return a dictionary {'words': words, 'times': times} where times
    is a list of lists that stores the durations it took each player to type
    each word in words.

    Arguments:
        words: a list of words, in the order they are entered.
        timestamps_per_player: A list of lists of timestamps including the time
                          each player started typing, followed by the time each
                          player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> result = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> result['words']
    ['collar', 'plush', 'blush', 'repute']
    >>> result['times']
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    ts_by_player = timestamps_per_player  # A shorter name (for convenience)
    # BEGIN PROBLEM 9
    times = []  # You may remove this line
    word_n = len(words)
    for per_player in ts_by_player: # [1, 3, 5] ; [2, 5, 6]
        time = []
        for i in range(0, word_n):
            time.append(per_player[i + 1] - per_player[i])
        times.append(time)
    # END PROBLEM 9
    return {'words': words, 'times': times}


def fastest_words(words_and_times: dict) -> list[list[str]]:
    """Return a list of lists indicating which words each player entered fastest.
    In case of a tie, the player with the lower index is considered to be the one who entered it the fastest.

    Arguments:
        words_and_times: a dictionary {'words': words, 'times': times} where
        words is a list of the words entered and times is a list of lists of times
        spent by each player typing each word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words({'words': ['Just', 'have', 'fun'], 'times': [p0, p1]})
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    check_words_and_times(words_and_times)  # verify that the input is properly formed
    words, times = words_and_times['words'], words_and_times['times']
    # assert len(words) == len(times[0]), "The length of words and times should be same"
    w_idxs = range(len(words))
    pl_idxs = range(len(times))
    # BEGIN PROBLEM 10
    res = [[] for _ in pl_idxs] # [['have', 'fun'], ['Just']] ; p0's fastest words, p1's fastest words
    flgs = [] # e.g. [0, 2, 1, 0] means that for word 0, p1 is fastest ...
    for i in w_idxs:
        idx_of_fastest = 0
        for j in pl_idxs:
            if times[j][i] < times[idx_of_fastest][i]:
                idx_of_fastest = j
        flgs.append(idx_of_fastest)
    for i in w_idxs:
        res[flgs[i]].append(words[i])
    return res
    # END PROBLEM 10


def check_words_and_times(words_and_times):
    """Check that words_and_times is a {'words': words, 'times': times} dictionary
    in which each element of times is a list of numbers the same length as words.
    """
    assert 'words' in words_and_times and 'times' in words_and_times and len(words_and_times) == 2
    words, times = words_and_times['words'], words_and_times['times']
    assert all([type(w) == str for w in words]), "words should be a list of strings"
    assert all([type(t) == list for t in times]), "times should be a list of lists"
    assert all([isinstance(i, (int, float)) for t in times for i in t]), "times lists should contain numbers"
    assert all([len(t) == len(words) for t in times]), "There should be one word per time."


def get_time(times, player_num, word_index):
    """Return the time it took player_num to type the word at word_index,
    given a list of lists of times returned by time_per_word."""
    num_players = len(times)
    num_words = len(times[0])
    assert word_index < len(times[0]), f"word_index {word_index} outside of 0 to {num_words-1}"
    assert player_num < len(times), f"player_num {player_num} outside of 0 to {num_players-1}"
    return times[player_num][word_index]


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file("data/sample_paragraphs.txt")
    random.shuffle(paragraphs)
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print("No more paragraphs about", topics, "are available.")
            return
        print("Type the following paragraph and then press enter/return.")
        print("If you only type part of it, you will be scored only on that part.\n")
        print(source)
        print()

        start = datetime.now()
        entered = input()
        if not entered:
            print("Goodbye.")
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print("Words per minute:", wpm(entered, elapsed))
        print("Accuracy:        ", accuracy(entered, source))

        print("\nPress enter/return for the next paragraph or type q to quit.")
        if input().strip() == "q":
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument("topic", help="Topic word", nargs="*")
    parser.add_argument("-t", help="Run typing test", action="store_true")

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)