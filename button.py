import sys 

import pygame

from settings import Settings

class Button ():

    def __init__(self):

        self.settings = Settings()

        self.x_scale = self.settings.button.get('x_scale') #pixles

        self.y_scale = self.settings.button.get('y_scale')

        self.y_margin = self.settings.button.get('button_margin')

        self.scaled_image_rojo = pygame.transform.scale(self.settings.button.get('image'),(self.x_scale,self.y_scale))

        self.scaled_image_rbrillante = pygame.transform.scale(self.settings.button.get('bright_image'),(self.x_scale,self.y_scale))

        self.display_x = self.settings.grid_surface.get('grid_start_x')

        self.display_y = self.settings.grid_surface.get('grid_start_y') + self.settings.grid_surface.get('hight') + self.settings.button.get('button_margin')

        self.dis_x = self.settings.grid_surface.get('grid_start_x')
        
    def draw_button(self):
        
        self.rect = self.scaled_image_rojo.get_rect()   # Le creo un rectangulo para la imagen  escalada

        self.display = pygame.display.get_surface() # devuelve la superfice que creamos 

        self.display.blit(self.scaled_image_rojo,(self.display_x,self.display_y)) # dibuja la superfice con las coordenadas 

    def draw_bright_button (self):

        self.rect = self.scaled_image_rbrillante.get_rect()   # Le creo un rectangulo para la imagen  escalada

        self.display = pygame.display.get_surface() # devuelve la superfice que creamos 

        self.display.blit(self.scaled_image_rbrillante,(self.display_x,self.display_y))

    def button_event(self):


        pos = pygame.mouse.get_pos()

        if self.x_scale + self.display_x > pos[0] > self.display_x and self.y_scale + self.display_y + self.y_margin > pos[1] > self.display_y + self.y_margin :
        
            self.draw_bright_button()

        else:
         
            self.draw_button() 
  