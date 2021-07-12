import time, abc

import pygame, sys
from pygame.locals import *

# set up the colors
BLACK = (0, 0, 0)


class GameConfigurations(metaclass=abc.ABCMeta):
    """
    Main structure of the game.

    Set the window, events and window surface
    """

    def __init__(self):
        # initialize the pygame
        pygame.init()

        # set the size window
        self.__canvas_height = 500
        self.__canvas_width = 500

        # create window
        self.canvas = pygame.display.set_mode((self.__canvas_width, self.__canvas_height), pygame.RESIZABLE)
        self.__clock = pygame.time.Clock()
        self.__game_running = True
        pygame.display.set_caption("Against the world")

        self._preloader()

    @abc.abstractmethod
    def _preloader(self):
        return

    @abc.abstractmethod
    def _running(self):
        return

    def run(self):
        self.__clock.tick(60)  # set 60 frames per second

        # init the game
        while self.__game_running:
            self.canvas.fill(BLACK)

            # capture the events
            for event in pygame.event.get():
                # quit game if press alt+F4 or exit
                if event.type == QUIT or (
                        event.type == KEYDOWN and event.key == (K_F4 and K_LALT)):
                    self.__game_running = False

                if event.type == VIDEORESIZE:  # resize the window
                    self.__canvas_width = event.w
                    self.__canvas_height = event.h

            self._running()  # applying the configurations

            pygame.display.update()  # draw the window changes
