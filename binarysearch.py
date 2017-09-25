"""Using a binary search, find val in a range of 1-100. Return # of guesses.

Construct a list of 1-100 (inclusive). Write a binary search that searches
for val in that list (val will always be a number between 1 and 100).

Return the number of searches it took to find val. For a proper binary search
of 1-100, this should never be more than 7.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
"""


def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    # initialize number of guesses
    num_guesses = 0

    # set binary parameters ("left" and "right" values)
    higher_than = 0
    lower_than = 101

    guess = None

    # initiate binary search
    while guess != val:
        num_guesses += 1

        # find halfway point to compare val to
        # since int, number truncates. ex. 50.5 --> 50.
        guess = (lower_than - higher_than) / 2 + higher_than

        # binary search traversal (initiates cutting possibilities by half)
        if val > guess:
            higher_than = guess

        elif val < guess:
            lower_than = guess

    # while loop now exited (= val found)
    return num_guesses


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n"
