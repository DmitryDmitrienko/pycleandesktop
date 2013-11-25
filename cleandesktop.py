#coding=utf-8
''' Codeant, 
    Development company for web and desktop applications 
    Скрипт для очистки рабочего стола
    Автор: Дмитрий Дмитриенко <dmitry.dmitrienko@outlook.com>
'''
__version__ = '0.3'

import argparse
import codecs
import shutil
import os
import json


class DesktopError(Exception):
    'Ошибка для не верного пути к папке'

    def __init__(self, message):
        self.mesage = message

    def __str__(self):
        return repr(self.message)


DEFAULT_FOLDER = os.path.expanduser('~/Desktop') + '/'

DEFAULT_OPTION = {
    'Documents': ('.txt', '.doc', '.pdf'),
    'Pictures': ('.jpg', '.png', '.gif'),
}


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
        if '~' in path_to_desktop:
            path_to_desktop = os.path.expanduser(path_to_desktop)
        root, dir, files = iter(os.walk(path_to_desktop)).next()
    except StopIteration as e:
        raise DesktopError(u'Fail desktop path')
    for file in files:
        file = unicode(file, 'utf-8')
        for name_folder, ext in option.items():
            for e in ext:
                if file.endswith(e):
                    new_folder = path_to_desktop + name_folder
                    path_file = path_to_desktop + file
                    move_file(path_file, new_folder)


def run_with_option_file(path_to_desktop, option_file):
    '''(str,str) -> NoneType
    Запуск очистки рабочего стола с файлами настроек и путём до рабочего стола
    '''
    if os.path.exists(option_file):
        with codecs.open(option_file, 'r', encoding='utf-8') as json_file:
            try:
                json_data = json.load(json_file)
            except ValueError as e:
                raise DesktopError(e.message)
            cleand_desktop(path_to_desktop, json_data)
            json_file.close()
    else:
        raise DesktopError(u'Fail path option file')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Clean desktop')
    parser.add_argument('--desktop', help='path to desktop folder', default=DEFAULT_FOLDER)
    parser.add_argument('--option', help='path to option file', default='./option.json')
    args = parser.parse_args()
    try:
        run_with_option_file(args.desktop, args.option)
    except DesktopError as e:
        print e.message