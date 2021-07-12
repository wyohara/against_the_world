import json
import pygame

from bin.LoaderConfig import LoaderConfig


INITIAL_POSITION_SPRITE = (0, 0)


class LoaderSpritesheet:
    def __init__(self, file_spritesheet_image, file_spritesheet_json):
        """
        Get the json configure of the spritesheet and slice the spitesheet
        :param file_spritesheet_image: image containing spritesheet
        :param file_spritesheet_json: json containing spritesheet map
        """
        self.file_spritesheet = file_spritesheet_image
        self.file_spritesheet_images = pygame.image.load(file_spritesheet_image).convert()  # parse to pygame image

        with open(file_spritesheet_json) as f:  # parse the json file to load the postions
            self.sprite_coordinates_map = json.load(f)
        f.close()

    def __cut_spritesheet_image(self, axis_x, axis_y, width, height):
        """
        Slice the spritesheet using the coordinates in json file
        :param axis_x: axis x0
        :param axis_y:  axis y0
        :param width:  width to cut
        :param height: height to cut
        :return: the Tile image as Sprite
        """
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey(LoaderConfig().load_colors["transparent"])
        sprite.blit(self.file_spritesheet_images, INITIAL_POSITION_SPRITE, (axis_x, axis_y, width, height))
        return sprite

    def parse_sprite(self, name):
        """
        Return the Tile image
        :param name: name of the tile
        :return: the tile image as Sprite
        """
        sprite_map = self.sprite_coordinates_map['frames'][name]['frame']

        # load positions in spritesheet
        axis_x, axis_y, width, height = sprite_map["x"], sprite_map["y"], sprite_map["w"], sprite_map["h"]
        return self.__cut_spritesheet_image(axis_x, axis_y, width, height)
