
import pygame


class Ship :
    # CLASS TO MANAGE SHIP                  
    def __init__(self,ai_game) :

        self.screen = ai_game.screen

        self.screen_rect = ai_game.screen.get_rect() 

        # LOAD THE SHIP IMAGE

        self.image = pygame.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()

        # START EACH NEW SHIP A THE BOTTOM CENTER OF THE SCREEN

        self.rect.midbottom = self.screen_rect.midbottom 

    def blitme(self):

        #DRAW THE SHIP AT ITS CURRENT LOCATION

        self.screen.blit(self.image, self.rect)



        


