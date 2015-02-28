#-*-coding=utf-8-*-

# Variable = nADJ
# Function = v_n
# Class = Name
# self = self.n

import os
import sys
import time
import pygame as pg
from pygame.locals import *
from pygame.font import *

UNIT = 32


def load_image(picName):
    current_dir = os.path.split(os.path.abspath(__file__))[0]
    path = os.path.join(current_dir, 'Resources', picName)
    return pg.image.load(path).convert()


def show_text(surfaceHandle, pos, text, color, fontBold=False, fontSize=20, fontIitalc=False):
    font = pg.font.SysFont('arial', fontSize)
    font.set_bold(fontBold)
    font.set_italic(fontIitalc)
    content = font.render(text, True, color)
    surfaceHandle.blit(content, pos)


def normal_text():
    author_info = "Designer: YorkLi"
    show_text(screen, (20, 18*UNIT), author_info, (0, 255, 0), False, 30, False)
    text_time = "Time: %s" % time.strftime("%H:%M:%S", time.gmtime())
    show_text(screen, (20, 19*UNIT), text_time, (0, 255, 0), False, 30, False)


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
    print '1'
    return mapping


class Block(pg.sprite.Sprite):
    """docstring for wall"""
    def __init__(self, landform, location, images):
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


class Control(object):
    """docstring for Control"""
    def __init__(self):
        self.keys = pg.key.get_pressed()
        self.obstacles = pg.sprite.Group()
        self.image = get_image()

    def build_battle(self):
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
        obstacles = Block('e', (10*UNIT, 19*UNIT), self.image)
        for y in range(0, 20):
            for x in range(0, 21):
                if battle_1[y][x] != ' ':
                    obstacles.append = Block(battle_1[y][x], (x*UNIT, y*UNIT), self.image)
                else:
                    pass
        return pg.sprite.Group(obstacles)

    def event_loop(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == QUIT or self.keys[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()

    def main_loop(self):
        while True:
            self.event_loop()
            screen.fill(color)
            self.build_battle()
            normal_text()
            pg.display.flip()

if __name__ == '__main__':
    pg.init()
    windowSize = (width, height) = (672, 640)
    color = (0, 0, 0)
    screen = pg.display.set_mode(windowSize)
    run = Control()
    run.main_loop()
