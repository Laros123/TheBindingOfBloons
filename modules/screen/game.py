from .screen import Screen
from modules.loader.gfx_loader import Sprite
import pygame


class GameScreen(Screen):
    def _draw(self) -> None:
        self.win.fill((13, 23, 12))
        self.win.blit(Sprite.SPRITES['leaves_background'][0].image, (0, 0))