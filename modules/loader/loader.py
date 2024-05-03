from .gfx_loader import AnimationLoader, SpriteAtlasLoader
from .character_loader import CharacterLoader
from .controls_loader import ControlsLoader


def load():
    AnimationLoader.load()
    SpriteAtlasLoader.load()
    CharacterLoader.load()
    ControlsLoader.load()


