import sys
import os
import pygame
from pathlib import Path
from grid import Grid # DEL ARCHIVO GRID IMPORTA LA CLASS Grid
from data_handling import GridDataLoader
from settings import   Settings # DEL ARCHIVO SETTINGS IMPORTA LA CLASS Settings
from button_manager import ButtonManager
from button import Button

class Arc_game():

    def __init__(self): 

        pygame.init() # INICIA LO NECESARIO PARA EL JUEGO (ES NECESARIO EN CADA NUEVO JUEGO)
        
        self.train_grids = {"input": [],
                            "output": []}
        self.test_grids = {"input": [],
                           "output": []}
        
        self.current_train_grid_pair = 0
        
        self.button_images = []
        self.hover_button_images = []
        images_path = "fotos"
        
        self.settings = Settings() 

        self.button = Button(color_number=0)  

        # CREA UNA SUPERFICIE PARA DISPLAY QUE ES LA PANTALLA PRINCIPAL SACANDO DE UN DICTIONARY
        self.screen = pygame.display.set_mode((self.settings.screen.get('screen_with'),
                                               self.settings.screen.get('screen_height')))  
       
        pygame.display.set_caption("Arc AGI game") # CREA UN NOMBRE PARA LA PANTALLA PRINCIPAL

        g_data_loader = GridDataLoader()
        train_in_g, train_out_g,test_in_g, test_out_g = g_data_loader.load_json_data(grid_data_path="grid_data/00d62c1b.json")

        self.load_button_images(images_path=images_path)
        self.initialize_train_grids(train_input=train_in_g, train_output=train_out_g)
        self.initialize_test_grids(test_input=test_in_g, test_output=test_out_g)

        self.display = pygame.display.get_surface()

        self.button_manager = ButtonManager(display=self.display,
                                          button_images=self.button_images,
                                          hover_button_images=self.hover_button_images)

    def load_button_images(self, images_path):
        # Load images for buttons from images_path
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


    def initialize_train_grids(self, train_input, train_output):
        for train_input_grid in train_input:
            self.train_grids["input"].append(train_input_grid)
        
        for train_output_grid in train_output:
            self.train_grids["output"].append(train_output_grid)
        
        train_initial_input = self.train_grids["input"][self.current_train_grid_pair]
        train_initial_output = self.train_grids["output"][self.current_train_grid_pair]
        self.l_train_input_grid = Grid(train_initial_input, (90, 90))   
        self.r_train_output_grid = Grid(train_initial_output, (self.settings.grid_surface.get("width") + 10, 90))


    def initialize_test_grids(self, test_input, test_output):
        
        self.test_grids["input"] = test_input
        self.test_grids["output"] = test_output

        grid_pos_x = self.settings.grid_surface.get("width") + 10
        grid_pos_y = self.settings.grid_surface.get("height") + 100
        
        self.l_test_input_grid = Grid(self.test_grids["input"], (90, grid_pos_y))   
        self.r_test_output_grid = Grid(self.test_grids["output"], (90 + grid_pos_x, grid_pos_y))


    def check_events(self): # FUNCION PARA CHEQUEAR EVENTOS DE TECLADO O MOUSE
        pygame.display.update()
        for event in pygame.event.get(): 

            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.current_color = self.button_manager.handle_color_change(mouse_pos=pos)
                self.r_test_output_grid.grid_update(current_color=self.current_color)

  
    def update_screen (self): 
        self.screen.fill(((self.settings.screen.get('bg_color')))) # LE DA EL COLOR DE FONDO A LA PANTALLA PRINCIPAL
        self.l_train_input_grid.draw_grid()
        self.r_train_output_grid.draw_grid()
        self.l_test_input_grid.draw_grid()
        self.r_test_output_grid.draw_grid()
        self.button_manager.render_buttons(mouse_pos=pygame.mouse.get_pos())


    def run_game(self) : # FUNCION DE LOOP PARA PARA IMPLEMENTAR TODO LOS COMPONENTES DEL JUEGO

        while True :
            self.check_events()
            self.update_screen()
            

if __name__ == '__main__' : # CONDICION QUE PONEMOS PARA USAR LA FUNCION .RUN_GAME()

    ai = Arc_game()
    ai.run_game()
