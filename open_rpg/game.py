import pygame
from title_menu import Menu
from pygame.locals import *
from pygame_interfaces import Fade

import sys
from locale import gettext as _

GAME_RESOLUTION=(800, 600)
GAME_TITLE=_('OpenRPG')

class Game:
    def __init__(self, resolution):
        self.surface = pygame.display.set_mode(GAME_RESOLUTION, pygame.DOUBLEBUF)
        pygame.display.set_caption(GAME_TITLE)
        self.menu = Menu(self.surface, options=[(_("New Game"), self.on_new_game),
                                      (_("Continue"), self.on_continue),
                                      (_("Quit"), self.on_quit)])
                                      
    def run(self):
        self.menu.run()
                                      
    def on_new_game(self):
        print 'start game'
        self.on_quit()
        
        
    def on_continue(self):
        print 'continue'
        
    def on_quit(self):
        Fade(self.surface, (0,0,0), 2)
        pygame.display.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game(GAME_RESOLUTION)
    game.run()
    
