from shutil import copy
from os import path

print("working")
if not path.isfile('config.json'):
    copy('config_default.json', 'config.json')
