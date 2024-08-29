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
            1: (0, 0, 255), # blue
            2: (255, 0, 0), # red
            3: (0, 255, 0), # green
            4: (255, 211, 67), # yellow
            5: (192, 192, 192), # grey
            6: (255, 0, 255), # fuschia
            7: (255, 165, 0), # orange
            8: (32, 178, 170), # teal
            9: (165, 42, 42), # brown
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

