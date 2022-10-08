#!/bin/python3
import os


def gridChallenge(grid):
    grid = [''.join(sorted(row)) for row in grid]
    index_counter = 0
    while index_counter < len(grid[0]):
        last_val = 'a'
        for row in grid:
            if last_val > row[index_counter]:
                return 'NO'
            last_val = row[index_counter]
        index_counter += 1
    return 'YES'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
