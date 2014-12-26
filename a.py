#-*-coding=utf-8-*-

import os
import sys
import time
import datetime
import pygame as pg
import math
from pygame.locals import *
from pygame.font import *

CAPTION = 'Tanks'
DIRECT_DICT = {pg.K_w : ( 0,-1),
               pg.K_s : ( 0, 1),
               pg.K_a : (-1, 0),
               pg.K_d : ( 1, 0)}
COLOR_KEY = (0, 0, 0)

def load_image(pic_name):
    #获取当前脚本文件所在目录的绝对路径
    current_dir = os.path.split(os.path.abspath(__file__))[0]

    #指定图片目录
    path = os.path.join(current_dir, 'Resources', pic_name)

    #加载图片
    return pg.image.load(path).convert()

def show_text(surface_handle, pos, text, color, font_bold = False, font_size = 20, font_italic = 
False):

    #获取系统字体，并设置文字大小
    cur_font = pg.font.SysFont('arial', font_size)
    #设置是否加粗属性
    cur_font.set_bold(font_bold)
    #设置是否斜体属性
    cur_font.set_italic(font_italic)
    #设置文字内容
    text_fmt = cur_font.render(text, True, color)
    #绘制文字
    surface_handle.blit(text_fmt, pos)

def text():
    author_info = "Editor: York Li"
    show_text(screen, (20, 390), author_info, (0, 255, 0), False, 30, False)
    text_time = "Time: %s" % time.strftime("%H:%M:%S", time.gmtime())
    show_text(screen, (20, 420), text_time, (0, 255, 0), False, 30, False)
           
  
class Bullets(pg.sprite.Sprite):
    """docstring for Bullets"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.original_bullet = bullet.subsurface((0, 0, 32, 32))
        self.image = self.original_bullet
        self.speed = 5
        self.rect = self.image.get_rect()
        self.move = [self.rect.x, self.rect.y]

    def update(self, screen_rect):
        self.move[0] += self.speed
        self.move[1] += self.speed
        self.rect.topleft = self.move
        self.remove(screen_rect)
        print ('update')

    def remove(self, screen_rect):
        if not self.rect.colliderect(screen_rect):
            self.kill()
            print ('remove')

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
        
class Tank:
    def __init__(self, speed, direction=pg.K_d):

        self.speed = speed
        self.keys = pg.key.get_pressed()
        self.direction = direction
        self.direction_stack = []
        self.old_direction = None
        self.frames = self.get_frames()
        self.walkframe_dict = self.make_frames_dict()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.bullets = Bullets()
        self.objects = pg.sprite.Group()

    def add_direction(self, key):
        if key in DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            self.direction_stack.append(key)
            self.direction = self.direction_stack[-1]
            # print('Add',self.direction_stack[0],self.direction,self.old_direction)

    def pop_direction(self, key):
        if key in DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            if self.direction_stack:
                self.direction = self.direction_stack[-1]
            #print('Pop',self.direction_stack)
        
    def make_frames_dict(self):
        frames = {  pg.K_w : self.frames[0],
                    pg.K_s : self.frames[1],
                    pg.K_a : self.frames[2],
                    pg.K_d : self.frames[3]}
        return frames
        
    def adjust_frames(self):
        if self.old_direction != self.direction:
            self.walkframe = self.walkframe_dict[self.direction]
            self.old_direction = self.direction
                
    def control_tank(self):        
        self.adjust_frames()
        TankPos = [x, y] = [0, 0]

        if self.direction_stack:       
            vector = DIRECT_DICT[self.direction]           

            TankPos[0] += self.speed * vector[0]
            TankPos[1] += self.speed * vector[1]

        return TankPos

    def update(self):
        self.objects.update(self.screen_rect)

    def draw(self):
        self.objects.draw(self.screen)

    def catch_event_key(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == QUIT or self.keys[pg.K_ESCAPE]: 
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    print ('1')
                    self.objects.add(Bullets())
                else:
                    self.add_direction(event.key)               
            elif event.type == pg.KEYUP:
                self.pop_direction(event.key)


          
    def play_tank(self):
        mytank_rect = mytank_up.get_rect()
         
        xx = 0
        yy = 0

        #循环，直到接收到窗口关闭事件
        while True:
            
            #退出事件处理  
            self.catch_event_key()
            
            cur_speed = self.control_tank()
            #Rect的clamp方法使用移动范围限制在窗口内
            mytank_rect = mytank_rect.move(cur_speed).clamp(window_size)
                       
            # print self.direction,self.old_direction       
            screen.blit(backgroud_image, (0, 0))
            screen.blit(self.walkframe, mytank_rect)
           
            self.update()
            self.draw()
            xx -= 0.1
            if xx < -text_surface.get_width():
                    xx = 640 - text_surface.get_width()

            rolling_text = "Testing"
            show_text(screen, (xx, yy), rolling_text, (0, 0, 255), False, 40, False)
            
            text()

            text_pos = "Position: (%d , %d)" % (mytank_rect.left, mytank_rect.top)
            show_text(screen, (20, 450), text_pos, (0, 255, 0), False, 30, False)
            
            #将Surface对象上帝绘制在屏幕上		
            pg.display.flip()
	

    def get_frames(self):
        frames = []
        frames.append(mytank_up)
        frames.append(mytank_down)
        frames.append(mytank_left)
        frames.append(mytank_right)
        return frames          


if __name__ == "__main__":
        pg.init()
        window_size = Rect(0, 0, 700, 500)
        screen = pg.display.set_mode(window_size.size)
        pg.display.set_caption(CAPTION)
        backgroud_image = load_image('backgroud.jpg')
        font = pg.font.SysFont('arial', 40)
        text_surface = font.render('Hello', True, (0, 0, 255))
        mytank_up = load_image('myTank_up.png')
        mytank_down = load_image('myTank_down.png')
        mytank_left = load_image('myTank_left.png')
        mytank_right = load_image('myTank_right.png')            
        bullet = load_image('bullet_square.jpg')
        bullet.set_colorkey(COLOR_KEY)
        player_1 = Tank(5)
        player_1.play_tank()
