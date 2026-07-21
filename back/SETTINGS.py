import os
import json
LOCAL_DIR = os.getenv("HOME")+"/.local/dnd-manager/"
CLASSES_DIR = LOCAL_DIR+"classes/"
RACES_DIR = LOCAL_DIR+"races/"
SAVES_DIR = LOCAL_DIR+"saves/"
LEVELS = {}
def get_levels_data():
    with open(LOCAL_DIR+"levels") as f:
        f.readline()
        _ = [tuple(map(int,line.split())) for line in f.readlines()]
        levels = dict(_)
    return levels
def init_consts():
    try:
        os.listdir(LOCAL_DIR)
    except FileNotFoundError:
        os.mkdir(LOCAL_DIR)