import sys

import pygame

from settings import  Settings

from ship import Ship

class AlienInvasion:
    """""OVERALL CLASS TO MANAGE GAME ASSETS AND BEHAVIOR"""
    def __init__(self) :
        """Initialize the game, and creat game resources"""
        pygame.init() # INICIA LOS SETTING DEL JUEGO ES NECESARIO

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_with, self.settings.screen_height))

        self.ship = Ship(self)

        pygame.display.set_caption("Alien Invasion")

    def _check_events (self):

     for event in pygame.event.get():

        if event.type == pygame.QUIT :

         sys.exit() 

         #elif  event.type == pygame.KEYDOWN :
            
            ##if event.key == pygame.k_RIGHT :

    def _update_screen(self):
        
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        pygame.display.flip()

    def run_game(self):
    
        while  True:
    
          self._check_events() 

          self._update_screen()

          self.clock.tick(60)

if __name__ == '__main__':
      
    ai = AlienInvasion()

    ai.run_game()
