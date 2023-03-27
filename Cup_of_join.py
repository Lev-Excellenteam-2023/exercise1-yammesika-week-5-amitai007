# region Cup of join

def Cup_of_join(*args, sep='-'):
    result = []
    if len(args) == 0:
        return None
    for arg in args:
        result.extend(arg)
        result.append(sep)
    result.pop()  # remove last separator
    return result


# endregion
