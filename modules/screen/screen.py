from abc import ABC, abstractmethod
from modules.consts import UPDATE_1_1, UPDATE_1_15, UPDATE_1_60
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
    
    def _events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == UPDATE_1_15:
                self._logic_1_15()
            if event.type == UPDATE_1_60:
                self._logic_1_60()
            if event.type == UPDATE_1_1:
                self._logic_1_1()

    def _draw(self) -> None:
        ...

    def update(self) -> None:
        self._events()
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