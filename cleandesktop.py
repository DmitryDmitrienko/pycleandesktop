#coding=utf-8
''' Codeant, 
	Development company for web and desktop applications 
	Скрипт для очистки рабочего стола
	Автор: Дмитрий Дмитриенко <dmitry.dmitrienko@outlook.com>
'''
__version__ = '0.1'

import argparse
import shutil
import os

class DesktopError(Exception):
    'Ошибка для не верного пути к папке'
    def __init__(self, mesage):
        self.mesage = mesage
    def __str__(self):
        return repr(self.mesage)

DEFAULT_FOLDER = os.path.expanduser('~/Desktop') + '/'


def print_info(path_folder):
    '''(str) -> NoneType
    Печать структуры папок и файлов в указанной папке
    '''
    for root, dir, files in os.walk(path_folder):
        path = root.split('/')
        print (len(path) - 1) * '---', os.path.basename(root)
        for file in files:
            print len(path) * '---', file


def move_file(file_path, new_folder):
    ''''(str, str) -> NoneType
    Перенос файла в новую папку
    '''
    if os.path.exists(new_folder):
        shutil.move(file_path, new_folder)
    else:
        os.makedirs(new_folder)
        shutil.move(file_path, new_folder)


def cleand_desktop(path_to_desktop, option):
    '''(str,dict) -> NoneType
    Очистка рабочего стола используя настройки 'option'
    '''
    try:
        root, dir, files = iter(os.walk(path_to_desktop)).next()
    except StopIteration:
        raise DesktopError(u'Fail path')
    for file in files:
        for name_folder, ext in option.items():
            for e in ext:
                if e in file:
                    new_folder = path_to_desktop + name_folder
                    path_file = path_to_desktop + file
                    move_file(path_file, new_folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Clean desktop')
    parser.add_argument('--desktop', help='path to desktop folder', default=DEFAULT_FOLDER)
    args = parser.parse_args()
    option = {
        'document': ('.txt', '.doc', '.pdf'),
        'pictures': ('.jpg', '.png', '.gif'),
    }
    try:
        cleand_desktop(args.desktop, option)
    except DesktopError as e:
        print e.mesage