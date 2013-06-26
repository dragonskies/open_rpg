import pygame
import os

def Fade(fade_from, fade_to, frameskip):
    origin_surface = None
    dest_surface = None
    if isinstance(fade_from, pygame.Surface):
        origin_surface = fade_from
    else:
        return False #bad
    if isinstance(fade_to, pygame.Surface):
        dest_surface = fade_to
    else:
        dest_surface = pygame.Surface(fade_from.get_size())
        dest_surface.fill(fade_to)
    alpha = 0.0
    while alpha <= 100.0:
        dest_surface.set_alpha(alpha)
        origin_surface.blit(dest_surface, (0,0))
        pygame.display.update()
        alpha += frameskip
        pygame.time.wait(10)
    

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
