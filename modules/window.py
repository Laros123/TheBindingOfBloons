import pygame
import pygame._sdl2 as sdl2

class Window:
    def __init__(self) -> None:
        self.win = pygame.display.set_mode((468, 312), pygame.SCALED|pygame.HWSURFACE|pygame.FULLSCREEN|pygame.DOUBLEBUF, vsync=1)
        self.win_sdl2 = sdl2.Window.from_display_module()
        renderer = sdl2.Renderer.from_window(self.win_sdl2)
        renderer.draw_color = pygame.Color((13, 23, 12))
        pygame.display.set_caption('The Binding of Bloons')
