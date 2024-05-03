import xml.etree.ElementTree as xml_tree
from modules.consts import RESOURCE_DIR
from typing import Dict
from .utils import valid_attribute


class ControlsLoader:
    CONTROLSTREE = xml_tree.parse(RESOURCE_DIR / 'controls.xml').getroot()
    CONTROLS: Dict[str, int] = {}
    @classmethod
    def load(cls):
        for key in cls.CONTROLSTREE.findall('Key'):
            cls.CONTROLS[key.attrib['name']] = valid_attribute(key.attrib['key'])
