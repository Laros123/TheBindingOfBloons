from .screen import Screen
from .game import GameScreen
from .menu import MenuScreen


class ScreenManager:
    def __init__(self) -> None:
        self.game: Screen = GameScreen('game', self)
        self.menu: Screen = MenuScreen('menu', self)
        self.__last_screen: Screen = self.menu
        self.__current_screen: Screen = self.game
        self.stopped: bool = False
    
    def change_current_screen(self, screen: Screen) -> None:
        self.__last_screen = self.get_current_screen()
        self.__current_screen = screen
    
    def get_current_screen(self) -> Screen:
        return self.__current_screen
    
    def get_last_screen(self) -> Screen:
        return self.__last_screen
    
    def run(self) -> None:
        while not self.stopped:
            self.get_current_screen().update()
