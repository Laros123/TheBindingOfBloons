from modules.consts import UPDATE_1_1, UPDATE_1_15, UPDATE_1_60
from modules.loader.controls_loader import ControlsLoader
from abc import ABC, abstractmethod
import pygame


class UpdateSystem(ABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.win = pygame.display.get_surface()
    
    def _logic_1_60(self) -> None:
        ...

    def _logic_1_15(self) -> None:
        ...

    def _logic_1_1(self) -> None:
        ...

    def _logic(self) -> None:
        ...

    @abstractmethod
    def quit(self) -> None:
        ...
    
    def _events(self, event) -> None:
        if event.type == pygame.QUIT:
            self.quit()
        if event.type == UPDATE_1_15:
            self._logic_1_15()
        if event.type == UPDATE_1_60:
            self._logic_1_60()
        if event.type == UPDATE_1_1:
            self._logic_1_1()
        if event.type == pygame.KEYDOWN:
            if event.key == ControlsLoader.CONTROLS['escape']:
                self.quit()
            if event.key == ControlsLoader.CONTROLS['fullscreen']:
                pygame.display.toggle_fullscreen()

    def _draw(self) -> None:
        ...

    def update(self) -> None:
        for event in pygame.event.get():
            self._events(event)
        self._logic()
        self._draw()
        pygame.display.flip()


class Screen(UpdateSystem):
    def __init__(self, screen_name: str, screen_manager: 'ScreenManager', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__screen_name = screen_name
        self.screen_manager = screen_manager

    def quit(self) -> None:
        self.screen_manager.stopped = True
    
    def get_screen_name(self) -> str:
        return self.__screen_name