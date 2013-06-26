import pygame
import os

class Font(pygame.font.Font):
    def __init__(self, font_path, font_size, antialias=1, fg_color=(255,255,255), bg_color=None):
        super(Font, self).__init__(font_path, font_size)
        self.path = font_path
        self.size = font_size
        self.antialias = antialias
        self.fg_color = fg_color
        self.bg_color = bg_color
        
    def set_size(self, size):
        self.size = size
        super(Font, self).__init__(self.path, self.size)
        
    def set_path(self, path):
        self.path = path
        super(Font, self).__init__(self.path, self.size)
        
    def set_fg_color(self, color):
        self.fg_color = color
        
    def set_bg_color(self, color=None):
        self.bg_color = color
        
    def simple_render(self, text):
        if self.bg_color:
            return self.render(text, self.antialias, self.fg_color, self.bg_color)
        else:
            return self.render(text, self.antialias, self.fg_color)