import random

def placeRandomBombe(k, n, m):
    for i in range(k):
        x = random.randint(0,n-1)
        y = random.randint(0,m-1)
        grid[y][x] = 'X'

def grid(n, m):
    array = [[0 for row in range(n)] for column in range(m)]
    return array

def displayGrid():
    for row in grid:
        print(" ".join(str(cell) for cell in row))
        print("")

if __name__ == "__main__":
    columns = 10
    lines = 5
    grid = grid(columns, lines)
    placeRandomBombe(2, columns, lines)
    displayGrid()
