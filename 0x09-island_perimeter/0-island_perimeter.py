#!/usr/bin/python3
""" island perimeter"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in the grid
    """

    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                """ start with 4 edges"""
                perimeter += 4

                """check above for edge sharing"""
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                """ check left for edge sharing"""
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
