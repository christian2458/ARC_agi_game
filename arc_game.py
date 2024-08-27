import sys
import os
import pygame  # NECESARIO PARA QUE FUNCIONE PYGAME
from pathlib import Path
from grid import Grid # DEL ARCHIVO GRID IMPORTA LA CLASS Grid

from settings import   Settings # DEL ARCHIVO SETTINGS IMPORTA LA CLASS Settings

from button import Button

class Arc_game():  # CLASS PRINCIPAL DEL JUEGO 

    def __init__(self): 

        pygame.init() # INICIA LO NECESARIO PARA EL JUEGO (ES NECESARIO EN CADA NUEVO JUEGO)

        self.grid = Grid()
        
        self.settings = Settings() 

        self.button = Button(color_number=0)  

        self.screen = pygame.display.set_mode((self.settings.screen.get('screen_with'), self.settings.screen.get('screen_height')))  # CREA UNA SUPERFICIE PARA DISPLAY QUE ES LA PANTALLA PRINCIPAL SACANDO DE UN DICTIONARY
       
        pygame.display.set_caption("Arc AGI game") # CREA UN NOMBRE PARA LA PANTALLA PRINCIPAL

        self.button_images = []
        self.hover_button_images = []
        images_path = "fotos"
        for item in os.listdir(images_path):
            # 03black_hover_button.png
            
            item_parts = item.split("_")
            item_path = Path(images_path, item)

            if len(item_parts) < 2 and os.path.isfile(item_path):
                scaled_button_image = self.button.load_image(image_path=item_path)
                self.button_images.append(scaled_button_image)
            else:
                scaled_hover_button_image = self.button.load_image(image_path=item_path)
                self.hover_button_images.append(scaled_hover_button_image)


    def check_events(self): # FUNCION PARA CHEQUEAR EVENTOS DE TECLADO O MOUSE
        pygame.display.update()
        for event in pygame.event.get(): 
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.grid.grid_update()

  
    def update_screen (self): 
        self.screen.fill(((self.settings.screen.get('bg_color')))) # LE DA EL COLOR DE FONDO A LA PANTALLA PRINCIPAL
        # prev_list_grid = self.grid.prev_list_grid
        self.grid.draw_grid(self.button_images, self.hover_button_images)

    def run_game(self) : # FUNCION DE LOOP PARA PARA IMPLEMENTAR TODO LOS COMPONENTES DEL JUEGO

        while True :
            self.check_events()
            self.update_screen()
            

if __name__ == '__main__' : # CONDICION QUE PONEMOS PARA USAR LA FUNCION .RUN_GAME()

    ai = Arc_game()
    ai.run_game()

