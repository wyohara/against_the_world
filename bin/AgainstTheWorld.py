from abc import ABC
import os

from bin.LoaderConfig import LoaderConfig
from bin.configurations.GameConfigurations import GameConfigurations
from bin.configurations.player_control.PlayerControl import PlayerControl
from bin.configurations.tile_system.LoaderSpitesheet import LoaderSpritesheet
from bin.configurations.tile_system.TileMap import TileMap

PATH_SOURCES = os.path.join(os.getcwd(), "sources")


class AgainstTheWorld(GameConfigurations, ABC):
    def __init__(self):
        super().__init__()

    def _preloader(self):
        # load the sprites
        loader_spritesheet = LoaderSpritesheet(os.path.join(PATH_SOURCES, "spritesheet/spritesheet.png"),
                                               os.path.join(PATH_SOURCES, "spritesheet/spritesheet.json"))
        # load the position tilemap
        self.tile_map = TileMap(os.path.join(PATH_SOURCES, 'test_level.csv'), loader_spritesheet)

        # load the player sprite
        self.player_sprite = loader_spritesheet.parse_sprite('chick.png')
        self.player_control = PlayerControl(self.player_sprite, self.game_canvas,
                                            self.tile_map.player_start_x, self.tile_map.player_start_y)
        self.player_control.draw_and_move()

    def _on_start_tick(self):
        # update to remove updated frames
        self.game_canvas.fill(LoaderConfig().load_colors["sky"])
        self.tile_map.draw_canvas(self.game_canvas)

    def _add_events(self):
        self.player_control.handle_keys()

    def _on_end_tick(self):
        self.player_control.draw_and_move()
