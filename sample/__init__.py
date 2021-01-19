import doctest


def sample(value):
    """Return value * 2.

    >>> sample(0)
    0
    >>> sample(1)
    2
    >>> sample(2)
    4
    >>> sample(3)
    6

    """
    return value * 2


if __name__ == "__main__":
    doctest.testmod()
