#import modules.loader.gfx_loader as gfx
from typing import List, Optional, Tuple
import numpy as np


class Object:
    def __init__(self, pos: Tuple[int, int] = (0, 0)) -> None:
        self.pos = np.array(pos, dtype=np.float16)


class AttachedObject(Object):
    """З'єднує об'єкти, по системі parent і child \n
        Можна з'єднувати тільки AttachedObject"""
    def __init__(self, parent: Optional['AttachedObject'] = None, *args, **kwargs) -> None:
        print(kwargs)
        super().__init__(*args, **kwargs)
        self.parent: Optional['AttachedObject'] = parent
        self.child_objects: List[Optional['AttachedObject']] = []

    @property
    def real_pos(self):
        if self.parent:
            return self.parent.real_pos - self.pos
        return self.pos
    
    def attach_child(self, child: 'AttachedObject'):
        self.child_objects.append(child)
