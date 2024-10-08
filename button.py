import os
import pygame
from settings import Settings

class Button ():

    def __init__(self, color_number):

        self.settings = Settings()

        self.x_scale = self.settings.button.get('x_scale') #pixles

        self.y_scale = self.settings.button.get('y_scale')

        self.y_margin = self.settings.button.get('button_margin')

        self.grid_start_x = self.settings.grid_surface.get('grid_start_x')

        self.button_pos_y = self.settings.grid_surface.get('grid_start_y') + self.settings.grid_surface.get('height') + self.settings.button.get('button_margin')

        self.button_pos_x = self.settings.grid_surface.get('grid_start_x')

        self.display = pygame.display.get_surface() # devuelve la superfice que creamos 

        self.color_number = color_number


    def load_image(self, image_path):
        image = pygame.image.load(image_path).convert_alpha()

        scaled_image = pygame.transform.scale(image, (self.x_scale,self.y_scale))

        return scaled_image
    

    def draw_button(self, display, scaled_image, pos_x, pos_y):
        
        self.rect = scaled_image.get_rect()   # Le creo un rectangulo para la imagen  escalada

        display.blit(scaled_image,(pos_x, pos_y)) # dibuja la superfice con las coordenadas 


    def draw_bright_button (self, display, scaled_image, pos_x, pos_y):

        self.rect = scaled_image.get_rect()   # Le creo un rectangulo para la imagen  escalada

        display.blit(scaled_image,(pos_x, pos_y))


