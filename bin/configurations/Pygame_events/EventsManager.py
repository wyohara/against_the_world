import abc
import pygame.event


class EventsManager(metaclass=abc.ABCMeta):
    def __init__(self, event=pygame.event.Event):
        """
        Class control event in pygame
        :param event:
        """
        self._event = event
        self.event = event

    @property
    def key_pressed(self):
        """return the key pressed"""
        return pygame.key.get_pressed()

    @abc.abstractmethod
    def resolve(self):
        """
        Resolve the events inside the game when catched
        :return:
        """
        return
