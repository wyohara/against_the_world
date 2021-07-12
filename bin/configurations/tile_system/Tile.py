import pygame


class Tile(pygame.sprite.Sprite):
    """
    Class to get a tile image and draw in another
    """
    def __init__(self, tile_image, x, y, spritesheet):
        """
        :param tile_image: tile image
        :param x: position in x coordinate screen view
        :param y: position in y coordinate screen view
        :param spritesheet: reference spritesheet used
        """

        # initiate the sprite
        pygame.sprite.Sprite.__init__(self)
        self.tile_image = spritesheet.parse_sprite(tile_image)
        self.rect = self.tile_image.get_rect()  # get the dimension of the image
        self.rect.x, self.rect.y = x, y

    def create_tile(self, canvas):
        canvas.blit(self.tile_image, (self.rect.x, self.rect.y))  # blit draw image in another
