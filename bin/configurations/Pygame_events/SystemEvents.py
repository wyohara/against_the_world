import abc, pygame
from pygame.locals import *
import sys

from bin.configurations.Pygame_events.EventsManager import EventsManager


class SystemEvents(EventsManager, abc.ABC):
    def __init__(self, event, canvas_width, canvas_height):
        """
        Class to control global system events
        :param event: pygame Event
        :param canvas_width: canvas width
        :param canvas_height: canvas height
        """
        super().__init__(event)
        self.__canvas_height = canvas_height
        self.__canvas_width = canvas_width

    def resolve(self):

        if self.event.type == QUIT or (  # quit game if press exit
                self.key_pressed[K_F4] and self.key_pressed[K_LALT]):  # quit game if press alt + F4
            pygame.quit()
            sys.exit()

        if self.event.type == VIDEORESIZE:  # resize the window
            self.__canvas_width = self.event.w
            self.__canvas_height = self.event.h
