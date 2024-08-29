import json

class GridDataLoader():
    
    def __init__(self) -> None:
        pass

    def load_json_data(self, grid_data_path):
        '''
        Sets the input and output examples from the TRAIN and TEST data
        '''
        with open(grid_data_path,  "r") as f:
            grid_data = json.load(f)

        train_data = grid_data["train"]
        test_data = grid_data["test"]

        train_input_grids = [example["input"] for example in train_data]
        train_output_grids = [example["output"] for example in train_data]

        test_input_grid = test_data[0]["input"]
        test_output_grid = test_data[0]["output"]

        return train_input_grids, train_output_grids, \
                test_input_grid, test_output_grid

    # all_input_examples = []
    # all_output_examples = []
    # for example in train_data:
    #     all_input_examples.append(example["input"])
    # for example in train_data:
    #     all_output_examples.append(example["output"])

