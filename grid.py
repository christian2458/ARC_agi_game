import os
import pygame
from settings import Settings
from button import Button
from pathlib import Path
import json

class Grid() :

    def __init__(self, grid_data, grid_position,cell_width,cell_height,cell_margin):

        self.settings = Settings()

        self.cell_width = cell_width

        self.cell_height = cell_height

        self.cell_margin = cell_margin

        self.default_color_number = 0

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
                        [(self.cell_margin + self.cell_width) * column + self.cell_margin,
                        (self.cell_margin + self.cell_height) * row + self.cell_margin,
                        self.cell_width,
                        self.cell_height])
        
        


    def draw_grid(self):

        self.display = pygame.display.get_surface()
        # setting grid width and height
        self.grid_surface_display = pygame.Surface((self.settings.grid_surface.get('width'),
                                                    self.settings.grid_surface.get('height')))

        self.grid_surface_display.fill(self.settings.grid_surface.get('back_ground_color'))
        # Create a 2 dimensional array. A two dimensional array is simply a list of lists.

        for row_number, row in enumerate(self.current_list_grid):
            for column_number, cell_color in enumerate(row):
                self.render_cell_color(cell_color, row_number, column_number)
                self.display.blit(self.grid_surface_display, (self.grid_position[0], self.grid_position[1]))

        
    def grid_update(self, current_color):

        pos = pygame.mouse.get_pos()  #   Change the x/y screen coordinates to grid coordinates

        if self.grid_position[0] < pos[0] < self.grid_position[0] + self.settings.grid_surface.get("width") and \
            self.grid_position[1] < pos[1] < self.grid_position[1] + self.settings.grid_surface.get("height"):

            # Transform mouse position to Grid Position
            self.column =  (pos[0] - self.grid_position[0]) // (self.settings.grid_surface.get('cell_width') + self.settings.grid_surface.get('cell_margin'))
            self.row =  (pos[1] - self.grid_position[1]) // (self.settings.grid_surface.get('cell_height') + self.settings.grid_surface.get('cell_margin'))
            print("trying to update cell color")
            # Color grid box when clicked
            try:
                self.current_list_grid[self.row][self.column] = current_color
                print("grid update: ", self.current_list_grid)

            except Exception as e:
                pass

            print("Click ", pos, "Grid coordinates: ", self.column,self.row)

