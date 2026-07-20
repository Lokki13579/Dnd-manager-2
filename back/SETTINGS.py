import os
MAIN_DIR = os.getenv("HOME")+"/.local/dnd-manager/"
def main_init():
    files = []
    try:
        files = os.listdir(MAIN_DIR)
    except FileNotFoundError:
        os.mkdir(MAIN_DIR)