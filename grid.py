import sys

import pygame

from settings import Settings

class Grid() :

    def __init__(self):

        self.settings = Settings()
        
        self.BLACK = (0, 0, 0)

        self.WHITE = (255, 255, 255)

        self.GREEN = (0, 255, 0)

        self.RED = (255, 0, 0) 

        self.list_grid = []  # EMPTY LIST WHERE WE WILL STORE AN ARRAY OF LISTS
    
    def draw_grid(self):

        self.grid_surface_display = pygame.Surface((self.settings.grid_surface.get('width'),self.settings.grid_surface.get('hight')))
        
        self.display = pygame.display.get_surface()

        self.grid_surface_display.fill(self.settings.grid_surface.get('back_ground_color'))

        # Create a 2 dimensional array. A two dimensional array is simply a list of lists.

        for row in range(10):
            
            self.list_grid.append([]) # Add an empty array that will hold each cell in this row

            for column in range(10):

              self.list_grid[row].append(0)  # Append a cell
    
         # Set row 1, cell 5 to one. (Remember rows and column numbers start at zero.) ->  self.list_grid[0][0] = 0 
         
       
        for row in range(10):  # Draw the grid

            for column in range(10):

                color = self.WHITE

                if self.list_grid[row][column] == 1:

                    color = self.GREEN
                
                pygame.draw.rect(self.grid_surface_display,
                                color,
                                [(self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_width')) * column + self.settings.grid_surface.get('cell_margin'),
                                (self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_hight')) * row + self.settings.grid_surface.get('cell_margin'),
                                self.settings.grid_surface.get('cell_width'),
                                self.settings.grid_surface.get('cell_hight')])
                
                self.display.blit(self.grid_surface_display, (self.settings.grid_surface.get('grid_start_x'), self.settings.grid_surface.get('grid_start_y')))
    

    def grid_event (self):

        pos = pygame.mouse.get_pos()
        # User clicks the mouse. Get the position
        # print("position",pos)
        # Change the x/y screen coordinates to grid coordinates

        self.column =  (pos[0] - self.settings.grid_surface.get('grid_start_x')) // (self.settings.grid_surface.get('cell_width') + self.settings.grid_surface.get('cell_margin'))

        self.row =  (pos[1] - self.settings.grid_surface.get('grid_start_y')) // (self.settings.grid_surface.get('cell_hight') + self.settings.grid_surface.get('cell_margin'))

        # Set that location to one
        try:
            # print("x: ", self.column)
            # print("y: ", self.row)
            self.list_grid[self.row][self.column] = 1
        except Exception as e:
            # print(f"error avoided... {e}")
            pass
        print("Click ", pos, "Grid coordinates: ", self.column,self.row)

    

     


     
     
     
     
     
    

