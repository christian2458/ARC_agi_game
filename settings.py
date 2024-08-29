import sys
import pygame

class Settings:

    def __init__(self) :

        self.screen = {
            'screen_with'   : 1280,           
            'screen_height' : 720,                 
            'bg_color'      :  (230, 230 ,230)  
                         }

        self.grid_surface = {                     
            'back_ground_color' : (175, 175 , 175),           
            'width'             : 255,     
            'height'             : 255,
            'cell_width'        : 20,
            'cell_height'        : 20, 
            'cell_margin'       : 5, 
            'grid_start_x'      : 90,
            'grid_start_y'      : 90,
                          }
        
        self.button = {
            'images_path'        : "fotos",
            'x_scale'      : 18,   
            'y_scale'      : 18,  
            'button_margin': 5,
                         }
        
        self.button_color = {
            0: (0, 0, 0), # black,
            1: (55, 35, 248), # blue
            2: (248, 30, 20), # red
            3: (26, 208, 40), # green
            4: (224, 222, 13), # yellow
            5: (125, 125, 125), # grey
            6: (255, 0, 255), # fuschia
            7: (236, 155, 0), # orange
            8: (12, 201, 163), # teal
            9: (122, 70, 15), # brown
            'black': (0, 0, 0),
            'blue': (0, 0, 255),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'yellow': (255, 211, 67),
            'grey': (192, 192, 192),
            'fuschia': (255, 0, 255),
            'orange': (255, 165, 0),
            'teal': (32, 178, 170),
            'brown': (165, 42, 42),
            'white': (255, 255, 255)
                         }

