#-*-coding=utf-8-*-

import os
import sys
import time
import datetime
import pygame as pg
import math
from pygame.locals import *
from pygame.font import *


DIRECT_DICT = {pg.K_w : ( 0,-1),
               pg.K_s : ( 0, 1),
               pg.K_a : (-1, 0),
               pg.K_d : ( 1, 0)}

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
    author_info = "Editor: YorkLi"
    show_text(screen, (20, 390), author_info, (0, 255, 0), False, 30, False)
    text_time = "Time: %s" % time.strftime("%H:%M:%S", time.gmtime())
    show_text(screen, (20, 420), text_time, (0, 255, 0), False, 30, False)
           
  
class Tank:
    def __init__(self, speed, direction=pg.K_d):

        #self.direction = 
        self.speed = speed
        self.keys = pg.key.get_pressed()
        self.direction = direction
        self.direction_stack = []
        self.old_direction = None
        self.frames = self.get_frames()
        self.walkframe_dict = self.make_frame_dict()

    def add_direction(self, key):
        if key in DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            self.direction_stack.append(key)
            self.direction = self.direction_stack[-1]
            print('Add',self.direction_stack)

    def pop_direction(self, key):
        if key in DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            if self.direction_stack:
                self.direction = self.direction_stack[-1]
            print('Pop',self.direction_stack)
        
    def make_frame_dict(self):
        frames = {  pg.K_w : self.frames[0],
                    pg.K_s : self.frames[1],
                    pg.K_a : self.frames[2],
                    pg.K_d : self.frames[3]}
        return frames
        
    def adjust_image(self):
        if self.old_direction != self.direction:
            self.walkframe = self.walkframe_dict[self.direction]
            self.old_direction = self.direction
                
    def control_tank(self):
        
        self.adjust_image()
        mytankpos = [x, y] = [0, 0]

        if self.direction_stack:       
            vector = DIRECT_DICT[self.direction]           

            mytankpos[0] += self.speed*vector[0]

            mytankpos[1] += self.speed*vector[1]

        return mytankpos
        #return mytankpos

    def event_loop(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == QUIT or self.keys[pg.K_ESCAPE]: 
                            pg.quit()
                            sys.exit()
            elif event.type == pg.KEYDOWN:
                self.add_direction(event.key)
            elif event.type == pg.KEYUP:
                self.pop_direction(event.key)
        
    
    def play_tank(self):
        mytank_rect = mytank_up.get_rect() 

        backgroud_image = load_image('backgroud.jpg')
             
        font = pg.font.SysFont('arial', 40)
        text_surface = font.render('Hello', True, (0, 0, 255))
       
        xx = 0
        yy = 0

        #循环，直到接收到窗口关闭事件
        while True:
            #退出事件处理  
            self.event_loop()
                           
            #使小球移动，速度由speed变量控制
            
            cur_speed = self.control_tank()
            
            #cur_speed= control_tank(event)
            #Rect的clamp方法使用移动范围限制在窗口内
            mytank_rect = mytank_rect.move(cur_speed).clamp(window_size)
            
            #设置窗口背景asd
            screen.blit(backgroud_image, (0, 0))

            #if event.type == KEYDOWN:
                # elif event.key == K_d:
                #     screen.blit(mytank_right, mytank_rect)
                # elif event.key == K_w:
                #     screen.blit(mytank_up, mytank_rect)
                # elif event.key == K_s:
                #     screen.blit(mytank_down, mytank_rect)
                # elif event.type == KEYUP:
                #     if event.key == K_a:
                #         screen.blit(mytank_left, mytank_rect)
                #     elif event.key == K_d:
                #         screen.blit(mytank_right, mytank_rect)
                #     elif event.key == K_w:
                #         screen.blit(mytank_up, mytank_rect)
                #     elif event.key == K_s:
                #         screen.blit(mytank_down, mytank_rect)

            #在背景Surface上绘制坦克
            #screen.blit(mytank_up, mytank_rect)
            screen.blit(self.walkframe, mytank_rect)
            
            

            xx -= 0.1
            if xx < -text_surface.get_width():
                    xx = 640 - text_surface.get_width()

            rolling_text = "Hello"
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
        pg.display.set_caption('Tank')
        mytank_up = load_image('myTank_up.png')
        mytank_down = load_image('myTank_down.png')
        mytank_left = load_image('myTank_left.png')
        mytank_right = load_image('myTank_right.png')
        t = Tank(5)
        t.play_tank()
