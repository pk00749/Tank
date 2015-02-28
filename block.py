#-*-coding=utf-8-*-

# Variable = nADJ
# Function = v_n
# Class = Name
# self = self.n

import os
import time
import pygame as pg
from pygame.locals import *
from pygame.font import *

UNIT = 32


def load_image(picName):
    current_dir = os.path.split(os.path.abspath(__file__))[0]
    path = os.path.join(current_dir, 'Resources', picName)
    return pg.image.load(path).convert()

def get_image():
    mapping = []
    wall = load_image('wall.jpg')
    grass = load_image('grass.jpg')
    eagle = load_image('eagle.jpg')
    steel = load_image('steel.jpg')
    water = load_image('water.jpg')
    mapping.append(eagle)
    mapping.append(wall)
    mapping.append(grass)
    mapping.append(steel)
    mapping.append(water)
    return mapping


class Block(pg.sprite.Sprite):
    """docstring for wall"""
    def __init__(self, landform, location, images, screen):
        pg.sprite.Sprite.__init__(self)
        self.mapping = images
        self.rect = location
        self.surface = screen
        self.obstacles = self.dict_block(landform)
        self.set_image()

    def set_image(self):
        self.surface.blit(self.obstacles, self.rect)

    def dict_block(self, landform):
        block = {'e': self.mapping[0],
                 'w': self.mapping[1],
                 'g': self.mapping[2],
                 's': self.mapping[3],
                 't': self.mapping[4]}
        return block[landform]


def build_battle(self, image, screen):
    battle_1 = ((' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '),
                ('g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'),
                ('g', 'w', 'w', 'w', 'w', 'g', 'w', 'w', 'w', 'w', 'g', 'w', 'w', 'w', 'w', 'g', 'w', 'w', 'w', 'g', 'g'),
                ('g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g'),
                ('g', 'w', 'g', 'g', 'g', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g'),
                ('g', 'w', 'g', 'w', 'w', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g'),
                ('g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g'),
                ('g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g', 'w', 'g', 'g', 'w', 'g'),
                ('g', 'w', 'w', 'w', 'w', 'g', 'w', 'w', 'w', 'w', 'g', 'w', 'w', 'w', 'w', 'g', 'w', 'w', 'w', 'g', 'g'),
                ('g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'),
                ('g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'),
                ('g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'),
                ('g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'),
                ('t', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't'),
                ('g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'),
                ('g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'),
                ('g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'),
                ('g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'),
                (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', 's', 's', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '),
                (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', 'e', 's', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '))
    obstacles = Block('e', (10*UNIT, 19*UNIT), image, screen)
    for y in range(0, 20):
        for x in range(0, 21):
            if battle_1[y][x] != ' ':
                obstacles.append = Block(battle_1[y][x], (x*UNIT, y*UNIT), image, screen)
            else:
                pass
    return pg.sprite.Group(obstacles)
