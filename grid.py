import os
import pygame
from settings import Settings
from button import Button
from pathlib import Path

class Grid() :

    def __init__(self):

        self.settings = Settings()

        self.button = Button()

        self.color_number = 1

        self.list_grid = []  # EMPTY LIST WHERE WE WILL STORE AN ARRAY OF LISTS

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

    def draw_grid(self, button_images):

        self.display = pygame.display.get_surface()
        
        self.grid_surface_display = pygame.Surface((self.settings.grid_surface.get('width'),self.settings.grid_surface.get('hight')))

        self.grid_surface_display.fill(self.settings.grid_surface.get('back_ground_color'))

        click = pygame.mouse.get_pressed()
        # (False, True, False)

        pos = pygame.mouse.get_pos()
        # (x, y) integers between 1280 and 720
        
        # Create a 2 dimensional array. A two dimensional array is simply a list of lists.
        for row in range(10):
            
            self.list_grid.append([]) # Add an empty array that will hold each cell in this row

            for column in range(10):

                self.list_grid[row].append(0) # Append a cell
    

        for row in range(10): # Draw the grid
            
            for column in range(10):
                self.render_box_colors(row, column)

                self.display.blit(self.grid_surface_display, (self.settings.grid_surface.get('grid_start_x'), self.settings.grid_surface.get('grid_start_y')))

        #change color for selecting boxes TODO: FOR LOOP to create extra buttons goes here
        images_path = self.settings.button.get("images_path")
        algo = 0

        for scaled_button_image in button_images:
            # rojo_brillante.png
            # rojo.png

            button = Button()
            algo += button.x_scale + 5
            if button.x_scale + button.grid_start_x + algo > pos[0] > button.grid_start_x + algo and button.y_scale + button.button_pos_y + button.y_margin > pos[1] > button.button_pos_y + button.y_margin:
                button_pos_x = algo + button.grid_start_x
                button_pos_y = button.button_pos_y
                button.draw_bright_button(display=self.display,
                                            scaled_image=scaled_button_image, 
                                            pos_x=button_pos_x, 
                                            pos_y=button_pos_y)

            else:
                pass


            if click[0] == True:
                button_pos_x = algo + button.grid_start_x
                button_pos_y = button.button_pos_y
                self.color = self.settings.button_color.get("red")
                self.button.draw_button(display=self.display,
                                        scaled_image=scaled_button_image,
                                        pos_x=button_pos_x,
                                        pos_y=button_pos_y)

            else:
                button_pos_x = algo + button.grid_start_x
                button_pos_y = button.button_pos_y
                self.button.draw_button(display=self.display,
                                        scaled_image=scaled_button_image,
                                        pos_x=button_pos_x,
                                        pos_y=button_pos_y)

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


