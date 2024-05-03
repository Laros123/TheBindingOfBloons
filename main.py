import pygame
import numpy as np
from modules.screen.screen_manager import ScreenManager
import modules.loader.loader as loader
from modules.window import Window

pygame.init()


if __name__ == '__main__':
    loader.load()
    win = Window()
    screen_manager = ScreenManager()
    screen_manager.run()