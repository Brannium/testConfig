from shutil import copy2
from os import path

print("working")
if not path.isfile('config.json'):
    copy2('config_default.json', 'config.json')
