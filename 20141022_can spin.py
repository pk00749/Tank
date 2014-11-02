#-*-coding=utf-8-*-

import os
import sys
import time
import datetime
import pygame
import math
from pygame.locals import *
from pygame.font import *

def load_image(pic_name):

        #获取当前脚本文件所在目录的绝对路径
        current_dir = os.path.split(os.path.abspath(__file__))[0]

        #指定图片目录
        path = os.path.join(current_dir, 'Resources', pic_name)

        #加载图片
        return pygame.image.load(path).convert()


def control_tank(event):

        #相对偏移坐标
        mytankpos = [x, y] = [0, 0]
        pre_mytankpos = [prex, prey] = [0, 0]
        degrees = 0

        #检查被按下的按键
        key = pygame.key.get_pressed()                  

        if key[pygame.K_a]:
                pre_mytankpos[0] = mytankpos[0]
                mytankpos[0] -= 5
        if key[pygame.K_d]:
                pre_mytankpos[0] = mytankpos[0]
                mytankpos[0] += 5
        if key[pygame.K_w]:
                pre_mytankpos[1] = mytankpos[1]
                mytankpos[1] -= 5
        if key[pygame.K_s]:
                pre_mytankpos[1] = mytankpos[1]
                mytankpos[1] += 5
        degrees = 0
        return mytankpos, pre_mytankpos, degrees
        #return mytankpos

def show_text(surface_handle, pos, text, color, font_bold = False, font_size = 20, font_italic = 
False):
        
        #获取系统字体，并设置文字大小
        cur_font = pygame.font.SysFont('arial', font_size)
        #设置是否加粗属性
        cur_font.set_bold(font_bold)
        #设置是否斜体属性
        cur_font.set_italic(font_italic)
        #设置文字内容
        text_fmt = cur_font.render(text, True, color)
        #绘制文字
        surface_handle.blit(text_fmt, pos)        

def play_tank():
        #任何pygame程序均需要执行此句进行模块初始化 
        pygame.init()

        #窗口大小  
        window_size = Rect(0, 0, 700, 500)
        
        #设置窗口模式
        screen = pygame.display.set_mode(window_size.size)

        #设置窗口标题
        pygame.display.set_caption('Tank')

        #加载小球图片
        mytank_image = load_image('myTank.png')
         #加载窗口背景图片 
        backgroud_image = load_image('backgroud.jpg')
        mytank_rect = mytank_image.get_rect()       

        font = pygame.font.SysFont('arial', 40)
        text_surface = font.render('Hello', True, (0, 0, 255))
       
        xx = 0
        yy = 0


        #循环，直到接收到窗口关闭事件
        while True:
                #退出事件处理  
                for event in pygame.event.get():
                        if event.type == QUIT: 
                                pygame.quit()
                                sys.exit()
                                
                #使小球移动，速度由speed变量控制 
                cur_speed, pre_speed, cur_degrees = control_tank(event)
                #cur_speed= control_tank(event)
                #Rect的clamp方法使用移动范围限制在窗口内
                mytank_rect = mytank_rect.move(cur_speed).clamp(window_size)
                
                #设置窗口背景asd
                screen.blit(backgroud_image, (0, 0))
                
                #获取小球图片的区域型状
                #if cur_speed[0] != pre_speed[0] and cur_speed[1] == pre_speed[1]:
                if cur_speed[0] != pre_speed[0]:
                        cur_degrees = 90
                
                mytank_image = pygame.transform.rotate(mytank_image, cur_degrees)
                #mytank_rect = cur_speed
                
                #在背景Surface上绘制坦克
                screen.blit(mytank_image, mytank_rect)

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
                pygame.display.flip()
		
if __name__ == "__main__":
        play_tank()
