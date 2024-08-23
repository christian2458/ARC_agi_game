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
                                    
            'back_ground_color' : (0, 0 ,0), 
                          
            'width'             : 255,
                          
            'hight'             : 255,

            'cell_width'        : 20,

            'cell_hight'        : 20, 

            'cell_margin'       : 5, 

            'grid_start_x'      : 90,

            'grid_start_y'      : 90,


                          }
        
        self.button = {
            
            'images_path'        : "fotos",

            'bright_image' : pygame.image.load("fotos/02rojo_brillante.png"),
            
            'x_scale'      : 18,
                       
            'y_scale'      : 18,
                       
            'button_margin': 5,
                         
                         }
        
        self.button_color = {
            
            'red'  : (255, 0, 0),

            'green': (0,255,0),
            
            'blue'  : (0,0,255),
                       
            'white' : (255,255,255),
                        
                         }
        
        

          



        

    
        
        
        

        

   

        
