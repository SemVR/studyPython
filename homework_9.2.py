#The difference between the numbers

def difference(*args):
    if not args:
        return 0

    result = max(args) - min(args)
    return round(result, 2)