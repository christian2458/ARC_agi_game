import sys

import pygame

from settings import Settings

from button import Button

class Grid() :

    def __init__(self):

        self.settings     = Settings()

        self.button       = Button()

        self.color_number = 1

        self.list_grid    = []  # EMPTY LIST WHERE WE WILL STORE AN ARRAY OF LISTS

    def render_box_colors(self, row, column):
        # RENDER all boxes WHITE
        pygame.draw.rect(self.grid_surface_display,
                                self.settings.button_color.get('white'),
                                [(self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_width')) * column + self.settings.grid_surface.get('cell_margin'),
                                (self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_hight')) * row + self.settings.grid_surface.get('cell_margin'),
                                self.settings.grid_surface.get('cell_width'),
                                self.settings.grid_surface.get('cell_hight')])

        # RENDER GREEN BOXES
        if self.list_grid[row][column] == 1:
            pygame.draw.rect(self.grid_surface_display,
                        self.settings.button_color.get('green'),
                        [(self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_width')) * column + self.settings.grid_surface.get('cell_margin'),
                        (self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_hight')) * row + self.settings.grid_surface.get('cell_margin'),
                        self.settings.grid_surface.get('cell_width'),
                        self.settings.grid_surface.get('cell_hight')])
        # RENDER RED BOXES
        elif self.list_grid[row][column] == 2:
            pygame.draw.rect(self.grid_surface_display,
                        self.settings.button_color.get('red'),
                        [(self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_width')) * column + self.settings.grid_surface.get('cell_margin'),
                        (self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_hight')) * row + self.settings.grid_surface.get('cell_margin'),
                        self.settings.grid_surface.get('cell_width'),
                        self.settings.grid_surface.get('cell_hight')])

    def draw_grid(self):

        self.grid_surface_display = pygame.Surface((self.settings.grid_surface.get('width'),self.settings.grid_surface.get('hight')))
        
        self.display              = pygame.display.get_surface()

        self.grid_surface_display.fill(self.settings.grid_surface.get('back_ground_color'))

        click                      = pygame.mouse.get_pressed()

        pos                        = pygame.mouse.get_pos()
        
        # Create a 2 dimensional array. A two dimensional array is simply a list of lists.
        for row in range(10):
            
            self.list_grid.append([]) # Add an empty array that will hold each cell in this row

            for column in range(10):

                self.list_grid[row].append(0)  # Append a cell
    

        for row in range(10): # Draw the grid
              
            for column in range(10):

                self.render_box_colors(row, column)

                self.display.blit(self.grid_surface_display, (self.settings.grid_surface.get('grid_start_x'), self.settings.grid_surface.get('grid_start_y')))

        #change color for selecting boxes 
        if self.button.x_scale + self.button.grid_start_x > pos[0] > self.button.grid_start_x and self.button.y_scale + self.button.display_y + self.button.y_margin > pos[1] > self.button.display_y + self.button.y_margin:

            self.button.draw_bright_button()

            if click[0] == True:

                self.color = self.RED

                self.button.draw_button()

        else:
            self.button.draw_button()

    def grid_event (self):

        pos = pygame.mouse.get_pos()  #   Change the x/y screen coordinates to grid coordinates
        
    
        self.column =  (pos[0] - self.settings.grid_surface.get('grid_start_x')) // (self.settings.grid_surface.get('cell_width') + self.settings.grid_surface.get('cell_margin'))

        self.row =  (pos[1] - self.settings.grid_surface.get('grid_start_y')) // (self.settings.grid_surface.get('cell_hight') + self.settings.grid_surface.get('cell_margin'))

        # Set that location to one
        try:
            pass
    
            self.list_grid[self.row][self.column] = self.color_number

        except Exception as e: 
            
            self.color_number = 2
            
            pass

        print("Click ", pos, "Grid coordinates: ", self.column,self.row)

  

                
                
            



    

     


     
     
     
     
     
    

