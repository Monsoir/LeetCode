def islandPerimeter(grid):
    return solution1(grid)

def solution1(grid):
    rounds = len(grid)
    rowRounds = len(grid[0])
    length = 0
    for i in range(0, rounds):
        for j in range(0, rowRounds):
            if grid[i][j] == 1:
                if i == 0:
                    length += 1
                if j == 0:
                    length += 1
                if i == rounds-1:
                    length += 1
                if j == rowRounds - 1:
                    length += 1

                if i > 0 and grid[i-1][j] == 0:
                    length += 1
                if i < rounds - 1 and grid[i+1][j] == 0:
                    length += 1
                if j > 0 and grid[i][j-1] == 0:
                    length += 1
                if j < rowRounds - 1 and grid[i][j+1] == 0:
                    length += 1

    return length

if __name__ == '__main__':
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
    ]

    print(solution1(grid))
