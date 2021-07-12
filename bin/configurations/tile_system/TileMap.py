import csv
import os

import pygame

from bin.configurations.tile_system.LoaderSpitesheet import LoaderSpritesheet
from bin.configurations.tile_system.Tile import Tile

TILE_SIZE = 16  # size of tile is 16px
BLACK = (0, 0, 0)


class TileMap:
    def __init__(self, filename_map_csv, loader_spritesheet=LoaderSpritesheet):
        """
        :param filename_map_csv:csv contain the coordinates
        :param loader_spritesheet: Class LoadSpritesheet to load the tiles
        """
        self.start_coord_x, self.start_coord_y = 0, 0
        self.loader_spritesheet = loader_spritesheet

        self.tilemap_loaded = self.__mount_tilemap(filename_map_csv)

        self.canvas = pygame.Surface((self.map_width, self.map_height))  # resize the window with the tilemap size
        self.canvas.set_colorkey(BLACK)
        self.__draw_tilemap()

    def draw_canvas(self, surface):
        """
        allow to blip tilemap in canvas (game window)
        :param surface:
        :return:
        """
        surface.blit(self.canvas, (0, 0))

    def __draw_tilemap(self):
        for tile in self.tilemap_loaded:
            tile.create_tile(self.canvas)

    def __read_csv_tilemap(self, csv_file):
        """
        Read the csv containing the tilemap positions
        :param csv_file: csv file containing the tilemap positions
        :return: position array
        """
        map = []
        with open(os.path.join(csv_file)) as csv_tile_map:
            csv_tile_map = csv.reader(csv_tile_map, delimiter=',')
            for row in csv_tile_map:
                map.append(list(row))
        return map

    def __mount_tilemap(self, filename_map_csv):
        """
        Create the tilemap containing the position in window and the tile value using csv file

        :param filename_map_csv: csv containing the position.
        :return: array containing the final tilemap
        """
        tilemap_parsed = []
        tile_axis_x, tile_axis_y = 0, 0
        for row in self.__read_csv_tilemap(filename_map_csv):
            tile_axis_x = 0
            for tile in row:
                if tile == '0':
                    self.start_x, self.start_y = tile_axis_x * TILE_SIZE, tile_axis_y * TILE_SIZE
                elif tile == '1':
                    tilemap_parsed.append(
                        Tile('grass.png', tile_axis_x * TILE_SIZE, tile_axis_y * TILE_SIZE, self.loader_spritesheet))
                elif tile == '2':
                    tilemap_parsed.append(
                        Tile('grass2.png', tile_axis_x * TILE_SIZE, tile_axis_y * TILE_SIZE, self.loader_spritesheet))

                tile_axis_x += 1  # Move to next tile in current x row
            tile_axis_y += 1  # Move to next tile to next y col

        # Store the final size of the tile map
        self.map_width, self.map_height = tile_axis_x * TILE_SIZE, tile_axis_y * TILE_SIZE
        return tilemap_parsed
