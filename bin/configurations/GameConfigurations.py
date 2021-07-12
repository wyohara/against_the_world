import abc
import pygame
from bin.configurations.Pygame_events.SystemEvents import SystemEvents


class GameConfigurations(metaclass=abc.ABCMeta):
    """
    Main structure of the game.

    Set the window, events and window surface
    """

    def __init__(self):
        pygame.init()

        # set the size window
        self.__canvas_height = 500
        self.__canvas_width = 500
        self._event = None

        # create window
        self.game_canvas = pygame.display.set_mode((self.__canvas_width, self.__canvas_height), pygame.RESIZABLE)

        self.__clock = pygame.time.Clock()  # define the clock to limit fps
        pygame.display.set_caption("Against the world")

        self._preloader()

    @abc.abstractmethod
    def _preloader(self):
        """
        Event aplied when the game start
        :return:
        """
        return

    @abc.abstractmethod
    def _on_start_tick(self):
        """
        Event applied when start loop tick
        :return:
        """
        return

    @abc.abstractmethod
    def _on_end_tick(self):
        """
        Event applied when end loop tick
        :return:
        """
        return

    @abc.abstractmethod
    def _add_events(self):
        """
        Events added when the game catch events
        :return:
        """
        return

    def start_game(self):
        self.__clock.tick(60)  # set 60 frames per second

        # init the game
        while True:
            self._on_start_tick()  # applying the configurations
            for self._event in pygame.event.get():  # capture the events
                SystemEvents(self._event, self.__canvas_width, self.__canvas_height).resolve()

                self._add_events()

            self._on_end_tick()
            pygame.display.update()  # draw the window changes
