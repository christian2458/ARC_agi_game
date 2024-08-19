import sys

import pygame  # NECESARIO PARA QUE FUNCIONE PYGAME

from grid import Grid # DEL ARCHIVO GRID IMPORTA LA CLASS Grid

from settings import   Settings # DEL ARCHIVO SETTINGS IMPORTA LA CLASS Settings

class Arc_game () :  # CLASS PRINCIPAL DEL JUEGO 

    def __init__(self) : # ASIGNACION DE VARIABLES PARA EL USO DE TODA LA CLASS

        pygame.init() # INICIA LO NECESARIO PARA EL JUEGO (ES NECESARIO EN CADA NUEVO JUEGO)

        self.grid = Grid() # LLAMANDO A LA CLASS Grid PARA QUE SEA ACCSESIBLE EN ESTA CLASS
        
        self.settings = Settings() # LLAMANDO A LA CLASS Settings PARA QUE SEA ACCSESIBLE EN ESTA CLASS

        self.screen = pygame.display.set_mode((self.settings.screen.get('screen_with'), self.settings.screen.get('screen_height')))  # CREA UNA SUPERFICIE PARA DISPLAY QUE ES LA PANTALLA PRINCIPAL SACANDO DE UN DICTIONARY
       
        pygame.display.set_caption("Arc AGI game") # CREA UN NOMBRE PARA LA PANTALLA PRINCIPAL
    
    def check_events (self): # FUNCION PARA CHEQUEAR EVENTOS DE TECLADO O MOUSE

        for event in pygame.event.get() : #FOR LOOP CIERRA EL JUEGO CUANDO SE PRESIONA LA X DE CERRAR LA PANTALLA

            if event.type == pygame.QUIT :

                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()

                print("position",pos)
                # Change the x/y screen coordinates to grid coordinates
                self.column =  (pos[0] - self.settings.grid_surface.get('grid_start_x')) // (self.settings.grid_surface.get('cell_width') + self.settings.grid_surface.get('cell_margin'))

                self.row =  (pos[1] - self.settings.grid_surface.get('grid_start_y')) // (self.settings.grid_surface.get('cell_hight') + self.settings.grid_surface.get('cell_margin'))

                # Set that location to one
                try:
                    print("x: ", self.column)
                    print("y: ", self.row)
                    self.grid.list_grid[self.row][self.column] = 1
                except Exception as e:
                    print(f"error avoided... {e}")
                    pass
                print("Click ", pos, "Grid coordinates: ", self.column,self.row)


    
    def update_screen (self): #FUNCION QUE DIBUJA LAS SUPERFICIES QUE TENGAMOS

     self.screen.fill(((self.settings.screen.get('bg_color')))) # LE DA EL COLOR DE FONDO A LA PANTALLA PRINCIPAL

     self.grid.draw_grid()
        
     pygame.display.update()  

        

    def run_game(self) : # FUNCION DE LOOP PARA PARA IMPLEMENTAR TODO LOS COMPONENTES DEL JUEGO

        while True :

            self.check_events()   

            self.update_screen()
            

if __name__ == '__main__' : # CONDICION QUE PONEMOS PARA USAR LA FUNCION .RUN_GAME()

    ai = Arc_game()

    ai.run_game()





