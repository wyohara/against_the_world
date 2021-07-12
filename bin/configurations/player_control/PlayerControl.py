import pygame
from bin.LoaderConfig import LoaderConfig

MOVE_SPEED = LoaderConfig().load_configurations["default_move_speed"]


class PlayerControl:
    def __init__(self, player, game_canvas, axis_x, axis_y):
        self.__player = player
        self.__game_canvas = game_canvas
        self.position_x = axis_x
        self.position_y = axis_y

    def draw_and_move(self):
        """update the player position"""
        self.__game_canvas.blit(self.__player, (self.position_x, self.position_y))

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:  # down key
            self.position_y += MOVE_SPEED  # move down
        elif key[pygame.K_UP]:  # up key
            self.position_y -= MOVE_SPEED  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.position_x += MOVE_SPEED  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.position_x -= MOVE_SPEED  # move left
