# region Cup of join

def cup_of_join(*args, sep='-'):
    """Accepts an unlimited number of lists.
    and parameter sep between any two lists, if not provided, the character "-" 
    returns a list consisting of lists
    """
    result = []
    if len(args) == 0:
        return None
    for arg in args:
        result.extend(arg)
        result.append(sep)
    result.pop()  # remove last separator
    return result


# endregion

if __name__ == '__main__':
    
    cup_of_join([1, 2], [8], [9, 5, 6], sep='@')
    cup_of_join([1, 2], [8], [9, 5, 6])
    cup_of_join([1])
    cup_of_join()
