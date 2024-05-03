import pygame
import pygame._sdl2 as sdl2

class Window:
    def __init__(self) -> None:
        self.win = pygame.display.set_mode((468, 312), pygame.SCALED|pygame.HWSURFACE|pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.RESIZABLE, vsync=1)
        self.win_sdl2 = sdl2.Window.from_display_module()
        self.renderer = sdl2.Renderer.from_window(self.win_sdl2)
        self.renderer.draw_color = pygame.Color((18, 24, 16))
        pygame.display.set_caption('The Binding of Bloons')
