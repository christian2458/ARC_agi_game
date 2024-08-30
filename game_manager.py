from data_handling import GridDataLoader


grid_data_path = 'grid_data/0a938d79.json'


class GameManager():
    def __init__(self) -> None:
        pass

    def next_arc_problem(self):
        pass

    def load_grids(self, grid_data_path):
        data_loader = GridDataLoader()  
        train_input, train_output, test_input, test_answer = data_loader.load_json_data(grid_data_path=grid_data_path)
        self.train_input = train_input
        self.train_output = train_output
        self.test_input = test_input
        self.test_answer = test_answer


    def next_train_grids(self):
        pass


    def previous_train_grids(self):
        pass

