#!/usr/bin/python3


def pascal_triangle(n):
    """
returns a list of lists of integers representing the Pascal’s triangle
"""

    if n <= 0:
        return []

    """ initialise the triangle with the first row"""
    triangle = [[1]]

    for i in range(1, n):
        """ start each row with 1"""
        row = [1]
        for j in range(1, i):
            """ each element is the sum of 2 numbers above it"""
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        """ end each row with 1"""
        row.append(1)
        triangle.append(row)

    return triangle
