#!/usr/bin/python3
'''Generate the minimum operations
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    num_ops = 0
    copy = 0
    paste = 1
    while paste < n:
        if copy == 0:
            copy = paste
            paste += copy
            num_ops += 2
        elif n - paste > 0 and (n - paste) % paste == 0:
            copy = paste
            paste += copy
            num_ops += 2
        elif copy > 0:
            paste += copy
            num_ops += 1
    return num_ops
