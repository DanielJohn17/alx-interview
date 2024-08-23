#!/usr/bin/python3
'''Module for minOperations method.'''


def minOperations(n: int) -> int:
    '''
        Method that calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
    '''
    file = "H"
    temp = ""
    operations = 0

    if not isinstance(n, int):
        return 0

    while len(file) < n:
        if n % len(file) == 0:
            temp = file
            operations += 2
        else:
            operations += 1

        file += temp

    return operations
