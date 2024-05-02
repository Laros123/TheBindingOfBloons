import pygame
import xml.etree.ElementTree as xml_tree
from modules.consts import RESOURCE_DIR
from typing import List
from .utils import valid_attributes, valid_attribute


class Sprite:
    """Має зображення і списки зображень"""
    SPRITES: dict = {}
    def __init__(self, image: pygame.Surface, name: str, id: int = -1) -> None:
        self.image: pygame.Surface = image
        # Перевіряється що зображення не з атласу
        if id >= 0:
            # Перевіряється що зображення немає у спрайтів
            if not isinstance(Sprite.SPRITES.get(name), list):
                Sprite.SPRITES[name] = []
            Sprite.SPRITES[name].append(self)
            return
        Sprite.SPRITES[name] = self


class SpriteLoader:
    ...


class SpriteAtlas:
    """Має зображення атласу, організує всі спрайти"""
    def __init__(self, name: str, path: str, sprite_atlas: xml_tree.Element) -> None:
        self.name: str = name
        self.image: pygame.Surface = pygame.image.load(path)
        self.current_id: int = 0
        self.load_sprites(sprite_atlas)
    
    def add_image(self, sprite_rect: dict):
        Sprite(self.image.subsurface(*sprite_rect.values()), self.name, self.current_id)
        self.current_id += 1

    def load_sprites(self, sprite_atlas: xml_tree.Element):
        # for має декілька ітерацій
        for for_sprite in sprite_atlas.findall('for'):
            for_attributes: dict = valid_attributes(for_sprite.attrib) # Має width і iter

            for i in range(for_attributes['iter']):
                for sprite in for_sprite.findall('Sprite'):
                    sprite_rect: dict = valid_attributes(sprite.attrib)
                    sprite_rect['x'] += i * for_attributes['width']

                    self.add_image(sprite_rect)

        for sprite in sprite_atlas.findall('Sprite'):
            sprite_rect: dict = valid_attributes(sprite.attrib)

            self.add_image(sprite_rect)
            

class SpriteAtlasLoader:
    SPRITEATLASSTREE = xml_tree.parse(RESOURCE_DIR / 'gfx' / 'sprite_sheets.xml').getroot()
    @classmethod
    def load(cls):
        for sprite_atlas in cls.SPRITEATLASSTREE:
            SpriteAtlas(sprite_atlas.attrib['name'], sprite_atlas.attrib['path'], sprite_atlas)


class Animation:
    ANIMATIONS = {}
    def __init__(self, name: str, ids: int, fps: int, loop: bool) -> None:
        self.name = name
        self.loop = loop
        self.sprites = ids
        self.fps = fps
        Animation.ANIMATIONS[self.name] = self.sprites


class AnimationLoader:
    ANIMATIONSTREE = xml_tree.parse(RESOURCE_DIR / 'gfx' / 'animations.xml').getroot()
    @classmethod
    def load(cls):
        for animations_object in cls.ANIMATIONSTREE.findall('AnimatedActor'):
            fps = valid_attribute(animations_object.attrib['fps'])
            for animation in animations_object.findall('Animation'):
                name = animation.attrib['name']
                loop = valid_attribute(animation.attrib['loop'])
                sprites: List[int] = []
                for sprite in animation.findall('Sprite'):
                    sprites.append(valid_attribute(sprite.attrib['id']))
                Animation(name, sprites, fps, loop)
