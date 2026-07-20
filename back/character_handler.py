import os
import json
from character_data.character import Character

all_characters = []


def save_characters():
    with open(SAVE_CHAR_PATH,w,encoding="utf-8"):
        pass

def add_character(char):
    global all_characters
    all_characters.append(char)
def create_character(name):
    available_id = len(all_characters) + 1
    new_character = Character(available_id)
