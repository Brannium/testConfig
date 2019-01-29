import os
from shutil import copy2
from os import path

print("working")
print('os.getcwd(): %s' % os.getcwd())
print('os.path-dirname(os.path.realpath(__file__)): %s' % os.path.dirname(os.path.realpath(__file__)))
print('os.path.dirname(os.path.abspath(__file__)): %s' % os.path.dirname(os.path.abspath(__file__)))

if not path.isfile('config.json'):
    copy2('config_default.json', 'config.json')
