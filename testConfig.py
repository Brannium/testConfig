import os
from shutil import copy2
from os import path

print("working")
print('os.getcwd(): %s' % os.getcwd())
print('os.listdir(os.getcwd()): %s' % os.listdir(os.getcwd()))

if not path.isfile('config.json'):
    copy2('config_default.json', 'config.json')

print('os.listdir(os.getcwd()): %s' % os.listdir(os.getcwd()))
