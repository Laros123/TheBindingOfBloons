from pathlib import Path
import numpy as np
import pygame
import os
pygame.init()

BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCE_DIR = BASE_DIR / 'resources'


UPDATE_1_60 = pygame.USEREVENT + 1
UPDATE_1_15 = pygame.USEREVENT + 2
UPDATE_1_1 = pygame.USEREVENT + 3
pygame.time.set_timer(UPDATE_1_60, int(1/60*1000))
pygame.time.set_timer(UPDATE_1_15, int(15/60*1000))
pygame.time.set_timer(UPDATE_1_1, int(60/60*1000))

DIRECTIONS: dict = {
    'up': np.array([0, -1], dtype=np.int8),
    'down': np.array([0, 1], dtype=np.int8),
    'left': np.array([0, -1], dtype=np.int8),
    'right': np.array([0, 1], dtype=np.int8)
}