# здесь будет происходить подгрузка классов из папки классов, которая будет получаться из файла настроек
from .SETTINGS import RACES_DIR, CLASSES_DIR, os, json
def get_files(path):
    files = os.listdir(path)
    return files
def get_full_file_info(target: str,path = ''):
    files = get_files(path)
    for file in files:
        with open(path+file) as f:
            data = json.loads(f.read())
            if data.get('name',"").lower() == target.lower():
                return data
def get_full_class_info(target):
    return get_full_file_info(target,CLASSES_DIR)
def get_full_race_info(target):
    return get_full_file_info(target,RACES_DIR)

