import random

def placeRandomBombe(nbBombs, nbColumns, nbLines):
    for i in range(nbBombs):
        x = random.randint(0,nbColumns-1)
        y = random.randint(0,nbLines-1)
        grid[y][x] = 'X'

def gridGenerator(nbColumns, nbLines):
    array = [[0 for row in range(nbColumns)] for column in range(nbLines)]
    return array

def displayGrid():
    for row in grid:
        print(" ".join(str(cell) for cell in row))
        print("")

if __name__ == "__main__":
    nbColumns = 10
    nbLines = 5
    grid = gridGenerator(nbColumns, nbLines)
    placeRandomBombe(2, nbColumns, nbLines)
    displayGrid()
