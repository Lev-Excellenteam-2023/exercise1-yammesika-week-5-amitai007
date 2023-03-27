# import the cycle and islice functions from the itertools module
from itertools import cycle, islice


# define a function called round_robin that accepts any number of iterables
def round_robin(*iterables):
    """round_robin('ABC', 'D', 'EF') --> A D E B F C"""
    # get the number of iterables passed in
    num_active = len(iterables)

    # create a cycle object that iterates over the __next__ method of each iterable
    nexts = cycle(iter(it).__next__ for it in iterables)

    # loop until there are no more active iterables
    while num_active:
        try:
            # iterate over the next method of each iterable in the cycle
            for next in nexts:
                # yield the next value from the iterable
                yield next()
        except StopIteration:
            # if an iterable raises StopIteration, remove it from the cycle
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))