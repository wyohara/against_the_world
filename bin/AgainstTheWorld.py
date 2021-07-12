from abc import ABC

from bin.configurations.GameConfigurations import GameConfigurations
from bin.configurations.tile_system.LoaderSpitesheet import LoaderSpritesheet
from bin.configurations.tile_system.TileMap import TileMap

BLACK = (0, 0, 0)
COLOR_SKY = (0, 180, 240)


class AgainstTheWorld(GameConfigurations, ABC):
    def __init__(self):
        super().__init__()

    def _preloader(self):
        loader_spritesheet = LoaderSpritesheet("sources/spritesheet/spritesheet.png",
                                               "sources/spritesheet/spritesheet.json")
        self.tile_map = TileMap('sources/test_level.csv', loader_spritesheet)

        # load the player sprite
        self.player_img = loader_spritesheet.parse_sprite('chick.png')

    def _running(self):

        player_pos = self.player_img.get_rect()
        player_pos.x, player_pos.y = self.tile_map.start_x, self.tile_map.start_y

        self.canvas.fill(COLOR_SKY)  # fill the canvas with blue sky
        self.tile_map.draw_canvas(self.canvas)
        self.canvas.blit(self.player_img, player_pos)
        pass
