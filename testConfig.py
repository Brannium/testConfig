from shutil import copyfile
from os import path

print("working")
if not path.isfile('config.json'):
    copyfile('config_default.json', 'config.json')
