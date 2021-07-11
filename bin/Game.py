import time

import pygame, sys
from pygame.locals import *

# set up direction variables
DOWN_LEFT = 1
DOWN_RIGHT = 3
UP_LEFT = 7
UP_RIGHT = 9
CELL_MOVE = 4

# set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Game(object):
    """
    Main structure of the game.

    Set the window, events and window surface
    """
    def __init__(self):
        # initialize the pygame
        pygame.init()

        # set the size window
        self.window_height = 500
        self.window_width = 500
        # set up the block data structure
        b1 = {"rect": pygame.Rect(300, 80, 50, 100), "color": RED, "dir": UP_RIGHT}
        b2 = {"rect": pygame.Rect(200, 200, 20, 20), "color": GREEN, "dir": UP_LEFT}
        b3 = {"rect": pygame.Rect(100, 150, 60, 60), "color": BLUE, "dir": DOWN_LEFT}
        self.__blocks = [b1, b2, b3]

        # create window
        self.window_surface = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        pygame.display.set_caption("Dungeon Legend")

    def __movements(self):
        for b in self.__blocks:
            # move the block data structure
            if b["dir"] == DOWN_LEFT:
                b["rect"].left -= CELL_MOVE
                b["rect"].top += CELL_MOVE
            if b["dir"] == DOWN_RIGHT:
                b["rect"].left += CELL_MOVE
                b["rect"].top += CELL_MOVE
            if b["dir"] == UP_LEFT:
                b["rect"].left -= CELL_MOVE
                b["rect"].top -= CELL_MOVE
            if b["dir"] == UP_RIGHT:
                b["rect"].left += CELL_MOVE
                b["rect"].top -= CELL_MOVE

            # check if the block has move out of the window
            if b["rect"].top < 0:
                # block has moved past the top
                if b["dir"] == UP_LEFT:
                    b["dir"] = DOWN_LEFT
                if b["dir"] == UP_RIGHT:
                    b["dir"] = DOWN_RIGHT
            if b["rect"].bottom > self.window_height:
                # block has moved past the bottom
                if b["dir"] == DOWN_LEFT:
                    b["dir"] = UP_LEFT
                if b["dir"] == DOWN_RIGHT:
                    b["dir"] = UP_RIGHT
            if b["rect"].left < 0:
                # block has moved past the left side
                if b["dir"] == DOWN_LEFT:
                    b["dir"] = DOWN_RIGHT
                if b["dir"] == UP_LEFT:
                    b["dir"] = UP_RIGHT
            if b["rect"].right > self.window_width:
                # block has moved past the right side
                if b["dir"] == DOWN_RIGHT:
                    b["dir"] = DOWN_LEFT
                if b["dir"] == UP_RIGHT:
                    b["dir"] = UP_LEFT

            # draw the block onto the surface
            pygame.draw.rect(self.window_surface, b["color"], b["rect"])

    def run(self):
        # init the game
        while True:

            self.window_surface.fill(BLACK)
            # capture the events
            for event in pygame.event.get():
                # quit game if press alt+F4 or exit
                if event.type == QUIT or (
                        event.type == KEYDOWN and event.key == (K_F4 and K_LALT)):
                    pygame.quit()
                    sys.exit()

                if event.type == VIDEORESIZE:  # resize the window
                    self.window_width = event.w
                    self.window_height = event.h

            self.__movements()  # apply the animation

            # draw the window changes
            pygame.display.update()
            time.sleep(0.02)
