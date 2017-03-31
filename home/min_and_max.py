#!/usr/bin/env python3


def min(*args, **kwargs):
    key = kwargs.get("key", None)

    if key is None:
        return find_min_without_key(args)
    else:
        return find_min_with_key(args, key)

def max(*args, **kwargs):
    key = kwargs.get("key", None)

    if key is None:
        return find_max_without_key(args)
    else:
        return find_max_with_key(args, key)

def find_min_without_key(data):
    result = next(iter(data))
    for arg in data:
        if hasattr(arg, "__iter__"):
            if len(data) > 1:
                if find_min_in_iterable(arg) < find_min_in_iterable(result):
                    result = arg
            else:
                result = next(iter(arg))
                for item in arg:
                    if item < result:
                        result = item
                return result
        else:
            if arg < result:
                result = arg
    return result

def find_min_with_key(data, key):
    if len(data) > 1:
        result = next(iter(data))
        for arg in data:
            if key.__call__(arg) < key.__call__(result):
                result = arg
    else:
        result = next(iter(data[0]))
        for arg in data[0]:
            if key.__call__(arg) < key.__call__(result):
                result = arg
    return result

def find_min_in_iterable(iter_object):
    local_min = iter_object[0]

    for item in iter_object:
        if item < local_min:
            local_min = item
    return local_min

def find_max_without_key(data):
    result = next(iter(data))
    for arg in data:
        if hasattr(arg, "__iter__"):
            if len(data) > 1:
                if find_max_in_iterable(arg) > find_max_in_iterable(result):
                    result = arg
            else:
                result = next(iter(arg))
                for item in arg:
                    if item > result:
                        result = item
                return result
        else:
            if arg > result:
                result = arg
    return result

def find_max_with_key(data, key):
    if len(data) > 1:
        result = next(iter(data))
        for arg in data:
            if key.__call__(arg) > key.__call__(result):
                result = arg
    else:
        result = next(iter(data[0]))
        for arg in data[0]:
            if key.__call__(arg) > key.__call__(result):
                result = arg
    return result

def find_max_in_iterable(iter_object):
    local_max = iter_object[0]

    for item in iter_object:
        if item < local_max:
            local_max = item
    return local_max


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert max(range(6)) == 5
    assert max(filter(str.isalpha, "@v$e56r5CY{C")) == "v"
    assert max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]) == [7]
