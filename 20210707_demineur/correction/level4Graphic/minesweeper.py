'''
Vikram Somu
Section A4
902829100
vs19@gatech.edu
'''

import turtle
import csv
import random
import math

class Sprite(object):
    def __init__(self, pixels):
        self.pixels = pixels

    def draw(self, turt, x, y):
          for col in range(len(self.pixels[0])):
            for row in range(len(self.pixels)):
                color = self.pixels[row][col]
                turtx = x + col
                turty = y - row
                if color:
                    self.plot_point(turt, turtx, turty, color)

    def plot_point(self, turt, x, y, color):
        turt.up()
        turt.pencolor(color)
        turt.setpos(x,y)
        turt.down()
        turt.forward(1)

class Mine(object):
    def __init__(self, sprite):
        self.drawn = False
        self.sprite = sprite

    def draw(self, turt, x, y):
        if self.drawn:
            return

        self.sprite.draw(turt, x, y)
        self.drawn = True

    def __str__(self):
        return "BOOM"

    def __repr__(self):
        return self.__str__()

class SafeSpot(object):
    total_spots = 0
    drawn_spots = 0

    def __init__(self, numAdjacent, sprite):
        self.sprite = sprite
        self.drawn = False
        self.numAdjacent = numAdjacent
        SafeSpot.total_spots += 1

    def draw(self, turt, x, y):
        if self.sprite:
            if self.drawn:
                return

            self.sprite.draw(turt, x, y)
        else:
            gray_rgb = (100, 100, 100)
            gray_sprite = Sprite([[gray_rgb]*25]*25)
            gray_sprite.draw(turt, x, y)

        SafeSpot.drawn_spots += 1
        self.drawn = True

    def __str__(self):
        if self.drawn:
            return '<{0}>'.format(self.numAdjacent)

        return str(self.numAdjacent)

    def __repr__(self):
        return self.__str__()

class MineSweeper(object):

    def __init__(self, width, height, prob, pixelCSV):
        self.width = width
        self.height = height

        self.spriteSetup(pixelCSV)
        self.gridSetup(prob)
        self.screenSetup()
        self.marked_mines = [[False for i in range(self.width)] for j in range(self.height)]

    def spriteSetup(self, pixelCSV_fn):
        self.spriteDict = {'0': None}
        blackbox_pix = [[(0,0,0) for i in range(23)] for j in range(24)]
        whitebox_pix = [[(255,255,255) for i in range(23)] for j in range(24)]

        reader = csv.reader(open(pixelCSV_fn, 'r'))

        sprite_idx = 0
        cur_sprite = []
        for rowi, row in enumerate(reader):
            if rowi != 0 and rowi % 25 == 0:
                if sprite_idx == 0:
                    self.spriteDict['mine'] = Sprite(cur_sprite)
                else:
                    self.spriteDict[str(sprite_idx)] = Sprite(cur_sprite)
                sprite_idx += 1
                cur_sprite = []
            cur_sprite.append(row)

        self.spriteDict['blackbox'] = Sprite(blackbox_pix)
        self.spriteDict['whitebox'] = Sprite(whitebox_pix)

    def gridSetup(self, prob):
        self.grid = [[None for i in range(self.width)] for j in range(self.height)]

        for rowi, row in enumerate(self.grid):
            for coli, col in enumerate(row):
                rand_test = random.random()

                if rand_test < prob:
                    self.grid[rowi][coli] = Mine(self.spriteDict['mine'])

        for rowi, row in enumerate(self.grid):
            for coli, col in enumerate(row):
                if not col:
                    adjacent_mines = self.find_adj_mines(coli, rowi)
                    self.grid[rowi][coli] = SafeSpot(
                        adjacent_mines,
                        self.spriteDict[str(adjacent_mines)]
                    )

    def find_adj_mines(self, x, y):
        adjacent_mines = 0

        for col in range(x-1, x+2):
            for row in range(y-1, y+2):
                if not (col == x and row == y) and self.gridloc_inbounds(col, row):
                    elem = self.grid[row][col]

                    if isinstance(elem, Mine):
                        adjacent_mines += 1

        return adjacent_mines

    def gridloc_inbounds(self, x, y):
        if x < 0 or y < 0 or y >= self.height or x >= self.width:
            return False

        return True

    def screenSetup(self):
        self.screen = turtle.Screen()
        self.drawer = turtle.Turtle()
        self.drawer.ht() #hide the turtle
        self.screen.colormode(255)

        self.screen.setup (
            width=self.width*25,
            height=self.height*25
        )

        self.screen.tracer(0)

        self.draw_grid(
            turtle.window_width(),
            turtle.window_height(),
            self.drawer
        )

        self.screen.setup (
            width=self.width*25 + 100,
            height=self.height*25 + 100
        )

        self.startX = 0
        self.startY = 0

        self.drawer.up()

        self.screen.onclick(self.clicked)
        self.screen.onclick(self.right_clicked, btn=2)
        self.screen.listen()

    def draw_grid(self, w, h, t):
        if not (hasattr(self, 'halfh') and hasattr(self, 'halfw')):
            self.halfh = int( h / 2 )
            self.halfw = int( w / 2 )

        woff = 1
        neghoff = 0

        if self.width % 2 != 0:
            woff += 1

        if self.height % 2 != 0:
            neghoff += 1

        for row in range(-1*self.halfh-neghoff, self.halfh+1):
            for col in range(-1*self.halfw, self.halfw+woff):
                rowi = self.halfh - row
                coli = col - (-1*self.halfw)
                if rowi % 25 == 0 or coli % 25 == 0:
                    t.up()
                    t.setpos(col, row)
                    t.down()
                    t.forward(1)

    def right_clicked(self, x, y):
        if not self.screenloc_inbounds(x,y):
            return
        # print(x,y)
        self.toggle_box_color(x,y)

    # Input any coord from the screen
    def toggle_box_color(self, x, y):
        topx, topy = self.get_box_topleft_coords(x, y)
        r, c = self.translate_cartesianxy_to_gridrc(topx, topy)

        if self.grid[r][c].drawn:
            return

        if self.marked_mines[r][c]:
            self.spriteDict['whitebox'].draw(self.drawer, topx+1, topy-1)
            self.marked_mines[r][c] = False
        else:
            self.spriteDict['blackbox'].draw(self.drawer, topx+1, topy-1)
            self.marked_mines[r][c] = True

    def clicked(self, x, y):
        if not self.screenloc_inbounds(x,y):
            return
        # set topx and topy now equal to the top left x,y coords of the clicked box
        topx, topy = self.get_box_topleft_coords(x, y)
        grid_row, grid_col = self.translate_cartesianxy_to_gridrc(topx, topy)
        itm = self.grid[grid_row][grid_col]
        # print(topx, topy)
        # print(grid_row, grid_col)
        # print(itm)
        # print(self.grid)

        # disable clicking marked spots
        if self.marked_mines[grid_row][grid_col]:
            return

        if not itm.drawn and isinstance(itm, Mine):
            self.handle_mine(itm, topx, topy)

        if not itm.drawn and isinstance(itm, SafeSpot):
            self.handle_safespot(itm, topx, topy)

    def screenloc_inbounds(self, x, y):
        if x < -1 * self.halfw or y < -1 * self.halfh:
            return False

        if x > self.halfw or y > self.halfh:
            return False

        return True

    def handle_safespot(self, itm, x, y):
        itm.draw(self.drawer, x, y)

        if itm.numAdjacent == 0:
            r, c = self.translate_cartesianxy_to_gridrc(x, y)
            self.zeroClicked(r, c)

        # win condition
        # print(SafeSpot.total_spots, SafeSpot.drawn_spots)
        if SafeSpot.total_spots == SafeSpot.drawn_spots:
            for r, row in enumerate(self.grid):
                for c, col in enumerate(row):
                    if isinstance(col, Mine):
                        topx, topy = self.translate_gridrc_to_cartesianxy(r, c)
                        if self.marked_mines[r][c]:
                            self.toggle_box_color(topx,topy) # clear box to white
                        col.draw(self.drawer, topx, topy) # drawn mine

            self.display_topleft_message("YOU WIN! :)")
            self.screen.exitonclick()

    # lose condition
    def handle_mine(self, itm, x, y):
        red_rgb = (255, 0, 0)
        red_sprite = Sprite([[red_rgb]*25]*25)
        red_sprite.draw(self.drawer, x, y)
        itm.draw(self.drawer, x, y)
        self.display_topleft_message("YOU LOSE :(")
        self.screen.exitonclick()

    def display_topleft_message(self, msg):
        self.drawer.up()
        self.drawer.setpos(-1*self.halfw, self.halfh)
        self.drawer.write(msg, font=('Calibri', 20, 'normal'))

    def translate_cartesianxy_to_gridrc(self, x, y):
        grid_row = math.floor( (self.halfh - y) / 25 )
        grid_col = math.floor( (x + self.halfw) / 25 )
        # print('translated r,c', grid_row,grid_col, self.halfh, self.halfw)
        return (grid_row, grid_col)

    def translate_gridrc_to_cartesianxy(self, r, c):
        topx = c*25 - self.halfw
        topy = self.halfh - r*25
        return (topx, topy)

    def get_box_topleft_coords(self, x, y):
        while ( x - (-1*self.halfw) ) % 25 != 0:
            x -= 1

        while (self.halfh - y) % 25 != 0:
            y += 1

        return (x, y)

    def zeroClicked(self, r, c):
        def zero_helper(self, r, c):
            elem = self.grid[r][c]
            # print('considering ', row, col, elem.drawn)
            if not elem.drawn and isinstance(elem, SafeSpot):
                # print('visiting ', row, col)
                x, y = self.translate_gridrc_to_cartesianxy(r, c)
                elem.draw(self.drawer, x, y)

                if elem.numAdjacent == 0:
                    self.zeroClicked(r, c)


        self.iterate_neighbors(r, c, zero_helper)

    def iterate_neighbors(self, r, c, cb):
        for col in range(c-1, c+2):
            for row in range(r-1, r+2):
                if not (col == c and row == r) and self.gridloc_inbounds(col, row):
                    cb(self, row, col)

def main():
    #Boxes
    GRID_WIDTH = 15
    GRID_HEIGHT = 15

    MineSweeper(GRID_WIDTH, GRID_HEIGHT, 0.15, "sprites.csv")
    turtle.done()

if __name__ == '__main__':
    main()
