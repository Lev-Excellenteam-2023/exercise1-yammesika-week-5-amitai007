from itertools import cycle, islice


def round_robin(*iterables):
    """
    Take any number of iterables and return their elements in a round-robin fashion.
    Args:
    *iterables: any number of iterables (e.g. lists, tuples, etc.)
    Yields:
    The next value from each iterable in a round-robin fashion.
    Example:
    round_robin('ABC', 'D', 'EF') -> A D E B F C
    """
    num_active = len(iterables)

    # create a cycle object that iterates over the __next__ method of each iterable
    nexts = cycle(iter(iterable).__next__ for iterable in iterables)

    # loop until there are no more active iterables
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # if an iterable raises StopIteration, remove it from the cycle
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))


def main():
    # example
    for item in round_robin('ABC', 'D', 'EF'):
        print(item)


if __name__ == '__main__':
    main()
