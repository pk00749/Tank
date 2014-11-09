#-*-coding=utf-8-*-

import os
import sys
import time
import datetime
import pygame as pg
import math
from pygame.locals import *
from pygame.font import *

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


def control_tank(event):

        #相对偏移坐标
        mytankpos = [x, y] = [0, 0]
        pre_mytankpos = [prex, prey] = [0, 0]

        #检查被按下的按键
        key = pg.key.get_pressed()                  

        if key[pg.K_a]:
                pre_mytankpos[0] = mytankpos[0]
                mytankpos[0] -= 5

        if key[pg.K_d]:
                pre_mytankpos[0] = mytankpos[0]
                mytankpos[0] += 5

        if key[pg.K_w]:
                pre_mytankpos[1] = mytankpos[1]
                mytankpos[1] -= 5

        if key[pg.K_s]:
                pre_mytankpos[1] = mytankpos[1]
                mytankpos[1] += 5

        
        return mytankpos, pre_mytankpos
        #return mytankpos
  

def play_tank():

        
        mytank_rect = mytank_up.get_rect() 
         #加载窗口背景图片 
        backgroud_image = load_image('backgroud.jpg')
             

        font = pg.font.SysFont('arial', 40)
        text_surface = font.render('Hello', True, (0, 0, 255))
       
        xx = 0
        yy = 0


        #循环，直到接收到窗口关闭事件
        while True:
                #退出事件处理  
                for event in pg.event.get():
                        if event.type == QUIT: 
                                pg.quit()
                                sys.exit()
                                
                #使小球移动，速度由speed变量控制 
                cur_speed, pre_speed = control_tank(event)
                #cur_speed= control_tank(event)
                #Rect的clamp方法使用移动范围限制在窗口内
                mytank_rect = mytank_rect.move(cur_speed).clamp(window_size)
                
                #设置窗口背景asd
                screen.blit(backgroud_image, (0, 0))

                
                #在背景Surface上绘制坦克
                screen.blit(mytank_up, mytank_rect)
                

                xx -= 0.1
                if xx < -text_surface.get_width():
                        xx = 640 - text_surface.get_width()

                rolling_text = "Hello"
                show_text(screen, (xx, yy), rolling_text, (0, 0, 255), False, 40, False)
                
                author_info = "Editor: YorkLi"
                show_text(screen, (20, 390), author_info, (0, 255, 0), False, 30, False)
    
                text_time = "Time: %s" % time.strftime("%H:%M:%S", time.gmtime())
                show_text(screen, (20, 420), text_time, (0, 255, 0), False, 30, False)

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
        
        play_tank()
