'''
@author: avalanchy (at) google mail dot com
@version: 0.1; python 2.7; pygame 1.9.2pre; SDL 1.2.14; MS Windows XP SP3
@date: 2012-04-08
@license: This document is under GNU GPL v3

README on the bottom of document.

@font: from http://www.dafont.com/coders-crux.font
      more abuot license you can find in data/coders-crux/license.txt
'''
# Based on menu.py (c) 2012 avalancy@googlemail.com

import pygame
from pygame.locals import *
import sys

from pygame_interfaces import Font, Fade

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()

menu_font = Font(font_path='../data/fonts/coders_crux/coders_crux.ttf', 
                 font_size=32, antialias=1, fg_color=(255, 255, 153))

# Set the background image, or None to use single color.
background_image = '../data/image/OpenRPG.png'

class Menu:
    menu_items = []
    field = []
    dest_surface = pygame.Surface
    n_menu_items = 0
    menu_background_color = (51,51,51)
    selection_color = (153,102,255)
    position_selection = 0
    position_embed = (0,0)
    menu_width = 0
    menu_height = 0

    class MenuItem:
        field_rect = pygame.Rect
        selection_rect = pygame.Rect

        def __init__(self, text, func):
            self.text = text
            self.func = func
            self.field = menu_font.simple_render(self.text)
            self.field_rect = self.field.get_rect()
    
    def __init__(self, surface, options):
        self.dest_surface = surface
        
        for text, func in options:
            self.menu_items.append(self.MenuItem(text, func))
        self.n_menu_items = len(options)

    def run(self):
        self.create_structure()
        if background_image:
            size = self.dest_surface.get_size()
            surface = pygame.Surface(size)
            self.dest_surface.fill((0,0,0))
            #self.draw()
            # Fade in
            image = pygame.image.load(background_image).convert()
            pygame.transform.smoothscale(image, size, surface)
            Fade(self.dest_surface, surface, 2)
            #alpha = 0.0
            #while alpha <= 100:
            #    surface.set_alpha(alpha)
            #    self.dest_surface.blit(surface, (0,0))
                #self.draw()
            #    pygame.display.update()
            #    alpha += 2
            #    pygame.time.wait(10)
            self.draw()
        else:
            self.dest_surface.fill(self.menu_background_color)
            self.draw()
        
        pygame.key.set_repeat(199,69)#(delay,interval)
        pygame.display.update()
        
        while 1:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.draw(-1) #here is the Menu class function
                    if event.key == K_DOWN:
                        self.draw(1) #here is the Menu class function
                    if event.key == K_RETURN:
                        self.menu_items[self.get_position()].func()                  
                    if event.key == K_ESCAPE:
                        pygame.display.quit()
                        sys.exit()
                    pygame.display.update()
                elif event.type == QUIT:
                    pygame.display.quit()
                    sys.exit()
            pygame.time.wait(8)
    

    def move_menu(self, top, left):
        """Set the menu position.  If called before the first draw, the position
        is relative to the center.  After the first draw, it is relative to the 
        window."""
        self.position_embed = (top,left) 

    def set_colors(self, text, selection, background):
        self.menu_background_color = background
        menu_font.set_color(text)
        self.selection_color = selection
        
    def set_fontsize(self,font_size):
        menu_font.set_size(font_size)
        
    def set_font(self, path):
        menu_font.set_path(path)
        
    def get_position(self):
        return self.position_selection  
        
    def draw(self,move=0):
        if move:
            self.position_selection += move 
            if self.position_selection == -1:
                self.position_selection = self.n_menu_items - 1
            self.position_selection %= self.n_menu_items
        menu = pygame.Surface((self.menu_width, self.menu_height))
        menu.fill(self.menu_background_color)
        selection_rect = self.menu_items[self.position_selection].selection_rect
        pygame.draw.rect(menu,self.selection_color,selection_rect)

        for i in xrange(self.n_menu_items):
            menu.blit(self.menu_items[i].field,self.menu_items[i].field_rect)
        self.dest_surface.blit(menu,self.position_embed)
        return self.position_selection

    def create_structure(self):
        self.menu_height = 0
        spacer = int(menu_font.size * 0.2)
        for i in xrange(self.n_menu_items):
            menu_item = self.menu_items[i]

            height = menu_item.field_rect.height
            menu_item.field_rect.left = spacer
            menu_item.field_rect.top = spacer+(spacer*2+height)*i

            width = menu_item.field_rect.width+spacer*2
            height = menu_item.field_rect.height+spacer*2            
            left = menu_item.field_rect.left-spacer
            top = menu_item.field_rect.top-spacer

            menu_item.selection_rect = (left,top ,width, height)
            if width > self.menu_width:
                    self.menu_width = width
            self.menu_height += height
        x = self.dest_surface.get_rect().centerx - self.menu_width / 2
        y = self.dest_surface.get_rect().centery - self.menu_height / 2
        mx, my = self.position_embed
        self.position_embed = (x+mx, y+my) 



        
