import xml.etree.ElementTree as xml_tree
from modules.consts import RESOURCE_DIR
from typing import Dict
from .utils import valid_attributes, valid_attribute


class CharacterLoader:
    CHARACTERSTREE = xml_tree.parse(RESOURCE_DIR / 'characters.xml').getroot()
    CHARACTERS: Dict[str, dict] = {}
    @classmethod
    def load(cls):
        for character in cls.CHARACTERSTREE.findall('Character'):
            for characteristics in character.findall('Characteristics'):
                cls.CHARACTERS[character.attrib['name']] = valid_attributes(characteristics.attrib)


class Character:
    def __init__(self, name: str, characteristics: dict, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.speed = characteristics[name]['speed']
        self.damage = characteristics[name]['damage']
        self.range = characteristics[name]['range']
        self.shot_speed = characteristics[name]['shot_speed']
        self.health = characteristics[name]['health']
        self.luck = characteristics[name]['luck']