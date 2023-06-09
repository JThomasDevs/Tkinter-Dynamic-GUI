import os
import sys


def _getpath_(file: str):
    path = os.getcwd()
    splitpath = path.split('\\')
    splitpath[-1] = file
    return '\\'.join(splitpath)


def imgpath(directory: str, file: str):
    if getattr(sys, 'frozen', False):   # This is for if the program is compiled into an exe using pyinstaller
        path = _getpath_(f'gui\\Images\\{directory}\\{file}')
        return path
    else:
        path = _getpath_(f'Images\\{directory}\\{file}')
        return path
