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
import block

CAPTION = 'Tanks'
DIRECT_DICT = {pg.K_w: (0, -1),
               pg.K_s: (0, 1),
               pg.K_a: (-1, 0),
               pg.K_d: (1, 0)}
COLOR_KEY = (0, 0, 0)
UNIT = 32

def load_image(picName):
    current_dir = os.path.split(os.path.abspath(__file__))[0]#获取当前脚本文件所在目录的绝对路径
    path = os.path.join(current_dir, 'Resources', picName)#指定图片目录
    return pg.image.load(path).convert()#加载图片

def show_text(surfaceHandle, pos, text, color, fontBold=False, fontSize=20, fontIitalc=False):
    font = pg.font.SysFont('arial', fontSize) #获取系统字体，并设置文字大小
    font.set_bold(fontBold) #设置是否加粗属性
    font.set_italic(fontIitalc) #设置是否斜体属性
    content = font.render(text, True, color) #设置文字内容
    surfaceHandle.blit(content, pos) #绘制文字

def rolling_text(posX, posY):
    rollingText = "Testing"
    show_text(screen, (posX, posY), rollingText, (0, 0, 255), False, 40, False)

def normal_text():
    authorInfo = "Designer: York Li"
    show_text(screen, (20, 390), authorInfo, (0, 255, 0), False, 30, False)
    textTime = "Time: %s" % time.strftime("%H:%M:%S", time.gmtime())
    show_text(screen, (20, 420), textTime, (0, 255, 0), False, 30, False)

class Bullets(pg.sprite.Sprite):
    """docstring for Bullets"""
    def __init__(self, tankRect, direction, speed):
        pg.sprite.Sprite.__init__(self)
        self.originalBullet = bullet.subsurface((0, 0, 32, 32))
        self.image = self.originalBullet
        self.speed = speed
        self.rect = tankRect
        self.distance = [self.rect.x, self.rect.y]
        self.direction = direction

    def update(self, screenRect):
        vector = DIRECT_DICT[self.direction]
        self.distance[0] += self.speed * vector[0]
        self.distance[1] += self.speed * vector[1]
        self.rect.topleft = self.distance
        self.remove(screenRect)

    def remove(self, screenRect):
        if not self.rect.colliderect(screenRect):
            self.kill()
            print ('remove')

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Tank:
    def __init__(self, speed, bulletSpeed, cartridgeClip, tankRect, location, direction=pg.K_d):
        self.speed = speed
        self.keys = pg.key.get_pressed()
        self.direction = direction
        self.directionStack = []
        self.preDirection = None
        self.frames = self.get_frames()
        self.walkframeDict = self.dict_frames()
        self.screen = pg.display.get_surface()
        self.screenRect = self.screen.get_rect()
        self.objects = pg.sprite.Group()
        self.center = []
        self.bulletSpeed = bulletSpeed
        self.cartridgeClip = cartridgeClip - 1
        self.rect = tankRect
        self.location = location

    def add_direction(self, key):
        if key in DIRECT_DICT:
            if key in self.directionStack:
                self.directionStack.remove(key)
            self.directionStack.append(key)
            self.direction = self.directionStack[-1]
            # print('Add',self.directionStack[0],self.direction,self.preDirection)

    def pop_direction(self, key):
        if key in DIRECT_DICT:
            if key in self.directionStack:
                self.directionStack.remove(key)
            if self.directionStack:
                self.direction = self.directionStack[-1]
            #print('Pop',self.directionStack)

    def dict_frames(self):
        frames = {pg.K_w: self.frames[0],
                  pg.K_s: self.frames[1],
                  pg.K_a: self.frames[2],
                  pg.K_d: self.frames[3]}
        return frames

    def control_frames(self):
        if self.preDirection != self.direction:
            self.walkframe = self.walkframeDict[self.direction]
            self.preDirection = self.direction

    def control_speed_direction(self):
        self.control_frames()
        tankPos = [x, y] = [0, 0]

        if self.directionStack:
            vector = DIRECT_DICT[self.direction]
            tankPos[0] += self.speed * vector[0]
            tankPos[1] += self.speed * vector[1]

        return tankPos

    def update(self):
        self.objects.update(self.screenRect)

    def draw(self):
        self.objects.draw(self.screen)

    def catch_event_key(self, event):
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    print ('Shoot')
                    if len(self.objects.sprites()) <= self.cartridgeClip:
                        print len(self.objects.sprites())
                        self.objects.add(Bullets(self.center, self.direction, self.bulletSpeed))
                else:
                    self.add_direction(event.key)
            elif event.type == pg.KEYUP:
                self.pop_direction(event.key)

    def play_tank(self):
        cur_speed = self.control_speed_direction()
        self.rect = self.rect.move(cur_speed).clamp(windowSize)# Rect的clamp方法使用移动范围限制在窗口内
        self.center = self.rect
        screen.blit(self.walkframe, self.rect)

        self.update()
        self.draw()

        text_pos = "Position: (%d , %d)" % (self.rect.left, self.rect.top)
        show_text(screen, (20, 450), text_pos, (0, 255, 0), False, 30, False)

    def get_frames(self):
        frames = []
        frames.append(mytankUp)
        frames.append(mytankDown)
        frames.append(mytankLeft)
        frames.append(mytankRight)
        return frames


class Control:
    """docstring for Control"""
    def __init__(self, rect):
        readyPos = (1*UNIT, 19*UNIT)
        self.keys = pg.key.get_pressed()
        self.done = False
        self.rect = rect
        self.rect.x = readyPos[0]
        self.rect.y = readyPos[1]
        self.player_1 = Tank(2, 4, 2, self.rect, [1*UNIT, 19*UNIT])
        self.image = block.get_image()

    def event_loop(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == QUIT or self.keys[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()
            self.player_1.catch_event_key(event)

    def update():
        pass

    def main_loop(self):
        posX = 0
        posY = 0
        while not self.done:
            screen.fill(color)
            self.event_loop()
            block.build_battle(self,self.image,screen)
            self.player_1.play_tank()
            posX -= 0.1
            if posX < -textSurface.get_width():
                posX = 640 - textSurface.get_width()
            rolling_text(posX, posY)
            normal_text()
            pg.display.flip()

if __name__ == "__main__":
        pg.init()
        color = (0, 0, 0)
        windowSize = Rect(0, 0, 672, 640)
        screen = pg.display.set_mode(windowSize.size)
        pg.display.set_caption(CAPTION)
        font = pg.font.SysFont('arial', 40)
        textSurface = font.render('Hello', True, (0, 0, 255))
        mytankUp = load_image('myTank_up.png')
        mytankDown = load_image('myTank_down.png')
        mytankLeft = load_image('myTank_left.png')
        mytankRight = load_image('myTank_right.png')
        bullet = load_image('bullet_square.jpg')
        bullet.set_colorkey(COLOR_KEY)
        mytankRect = (mytankUp.get_rect())
        run = Control(mytankRect)
        run.main_loop()
