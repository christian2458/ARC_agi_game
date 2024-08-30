from data_handling import GridDataLoader

from settings import Settings
    
class GridManager():
    def __init__(self, grid_data_path, settings) -> None:
        self.grid_data_path = grid_data_path
        self.grid_width = settings.grid_surface.get("width")
        self.grid_height = settings.grid_surface.get("height")
        self.cell_margin = settings.grid_surface.get("cell_margin")

    def load_grid_sizes(self, train_input):

        cell_width = 0
        cell_height = 0
        train_grid_sizes = []
        for train in train_input:
            cell_width = (self.grid_width-self.cell_margin)/(len(train[0]))-self.cell_margin
            cell_height = (self.grid_height-self.cell_margin)/(len(train)) -self.cell_margin
            train_grid_sizes.append([cell_width, cell_height])

        return train_grid_sizes

# answer: cell_width = 36.67, cell_height = 36.67
# (255 - 5)/6 - 5 = 36.67
# (width - cell_margin)/num_columns - cell_margin   ==> cell_width
# (height - cell_margin)/num_rows - cell_margin   ==> cell_height