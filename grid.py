import os
import pygame
from settings import Settings
from button import Button
from pathlib import Path
import json

class Grid() :

    def __init__(self, grid_data, grid_position):

        self.settings = Settings()

        self.default_color_number = 0

        self.current_color = 0

        self.current_list_grid = []  # EMPTY LIST WHERE WE WILL STORE AN ARRAY OF LISTS

        self.grid_position = grid_position
        
        for row_num, row in enumerate(grid_data):
            self.current_list_grid.append([]) # Add an empty array that will hold each cell in this row
            for col_num, color_value in enumerate(row):
                self.current_list_grid[row_num].append(color_value)

        print("grid position: ", grid_position)

    def render_cell_color(self, color_number, row, column):

        pygame.draw.rect(self.grid_surface_display,
                        self.settings.button_color[color_number],
                        [(self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_width')) * column + self.settings.grid_surface.get('cell_margin'),
                        (self.settings.grid_surface.get('cell_margin') + self.settings.grid_surface.get('cell_height')) * row + self.settings.grid_surface.get('cell_margin'),
                        self.settings.grid_surface.get('cell_width'),
                        self.settings.grid_surface.get('cell_height')])


    def render_buttons(self, button_images, hover_button_images, mouse_pos):
        x_distance_between_buttons = 0

        for idx, (scaled_button_image, scaled_hover_button_image) in enumerate(zip(button_images, hover_button_images)):
            # 0, (rojo.png, rojo_hover.png)
            # 1, (verde.png, ...)

            # Create the Button Instance to draw on screen
            button = Button(color_number=idx)
            button_pos_x = x_distance_between_buttons + button.grid_start_x
            button_pos_y = button.button_pos_y
            
            if button.x_scale + button.grid_start_x + x_distance_between_buttons > mouse_pos[0] > button.grid_start_x + x_distance_between_buttons \
            and button.y_scale + button.button_pos_y + button.y_margin > mouse_pos[1] > button.button_pos_y + button.y_margin:
        
                button.draw_bright_button(display=self.display,
                                            scaled_image=scaled_hover_button_image, 
                                            pos_x=button_pos_x, 
                                            pos_y=button_pos_y)

            else:    
                button.draw_button(display=self.display,
                                        scaled_image=scaled_button_image,
                                        pos_x=button_pos_x,
                                        pos_y=button_pos_y)

            # update the distance between buttons
            x_distance_between_buttons += button.x_scale + 10


    def handle_color_change(self, button_images, hover_button_images, mouse_pos):
        x_distance_between_buttons = 0
        for idx, (scaled_button_image, scaled_hover_button_image) in enumerate(zip(button_images, hover_button_images)):
            # 0, (rojo.png, rojo_hover.png)
            # 1, (verde.png, ...)

            # Create the Button Instance to draw on screen
            button = Button(color_number=idx)
            
            if button.x_scale + button.grid_start_x + x_distance_between_buttons > mouse_pos[0] > button.grid_start_x + x_distance_between_buttons \
            and button.y_scale + button.button_pos_y + button.y_margin > mouse_pos[1] > button.button_pos_y + button.y_margin:
                self.current_color = button.color_number
                print(f"changing current color to {self.current_color}")

            x_distance_between_buttons += button.x_scale + 10


    def draw_grid(self, button_images, hover_button_images):

        self.display = pygame.display.get_surface()
        
        self.grid_surface_display = pygame.Surface((self.settings.grid_surface.get('width'),
                                                    self.settings.grid_surface.get('height')))

        self.grid_surface_display.fill(self.settings.grid_surface.get('back_ground_color'))
        # Create a 2 dimensional array. A two dimensional array is simply a list of lists.

        pos = pygame.mouse.get_pos()
        # (x, y) integers between 1280 and 720

        for row_number, row in enumerate(self.current_list_grid):
            for column_number, cell_color in enumerate(row):
                self.render_cell_color(cell_color, row_number, column_number)
                self.display.blit(self.grid_surface_display, (self.grid_position[0], self.grid_position[1]))

        # #change color for selecting boxes TODO: FOR LOOP to create extra buttons goes here
        
        # self.render_buttons(button_images=button_images,
        #                     hover_button_images=hover_button_images,
        #                     mouse_pos=pos)

        # Potential bug - Code runs many times with 1 click
        # self.handle_color_change(button_images=button_images,
        #                         hover_button_images=hover_button_images,
        #                         mouse_pos=pos)
        

    def grid_update(self):

        pos = pygame.mouse.get_pos()  #   Change the x/y screen coordinates to grid coordinates
        print("grid position: ", self.grid_position)
        print("x bounds: ", self.grid_position[0] + self.settings.grid_surface.get("width"))
        print("y bounds: ", self.grid_position[1] + self.settings.grid_surface.get("height"))
        print("mouse pos: ", pos)

        if self.grid_position[0] < pos[0] < self.grid_position[0] + self.settings.grid_surface.get("width") and \
            self.grid_position[1] < pos[1] < self.grid_position[1] + self.settings.grid_surface.get("height"):

            self.column =  (pos[0] - self.grid_position[0]) // (self.settings.grid_surface.get('cell_width') + self.settings.grid_surface.get('cell_margin'))
            self.row =  (pos[1] - self.grid_position[1]) // (self.settings.grid_surface.get('cell_height') + self.settings.grid_surface.get('cell_margin'))
            print("trying to update cell color")
            # Color grid box when clicked
            try:
                self.current_list_grid[self.row][self.column] = self.current_color
                print("grid update: ", self.current_list_grid)

            except Exception as e:
                pass

            print("Click ", pos, "Grid coordinates: ", self.column,self.row)

