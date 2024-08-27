import json
from grid import Grid
import sys
import os
import pygame  # NECESARIO PARA QUE FUNCIONE PYGAME
from pathlib import Path
from grid import Grid # DEL ARCHIVO GRID IMPORTA LA CLASS Grid
from settings import   Settings # DEL ARCHIVO SETTINGS IMPORTA LA CLASS Settings
from button import Button
from arc_game import Arc_game

grid_data_file_path = "grid_data/0a938d79.json"

with open(grid_data_file_path,  "r") as f:
    grid_data = json.load(f)

train_data = grid_data["train"]

number_of_examples = len(train_data)

all_input_examples = []
all_output_examples = []
for example in train_data:
    all_input_examples.append(example["input"])
for example in train_data:
    all_output_examples.append(example["output"])

