#coding=utf-8
''' Codeant, 
	Developed web application and desktop application company.
	Скрипт для очистки рабочего стола
	Автор: Дмитрий Дмитриенко <dmitry.dmitrienko@outlook.com>
'''
import os
import shutil

def print_info(path_folder):
	'''(str) -> NoneType
	Печать структуру папок и файлов в папке
	'''	
	for root, dir, files in os.walk(path_folder):
	    path = root.split('/')
	    print (len(path) - 1) *'---' , os.path.basename(root)       
	    for file in files:
	        print len(path)*'---', file

def move_file(file_path,new_folder):
	''''(str, str) -> NoneType
	Перено файла в новую папку
	'''
	if os.path.exists(new_folder):
		shutil.move(file_path,new_folder)
	else:
		os.makedirs(new_folder)
		shutil.move(file_path, new_folder)

def cleand_desktop(path_to_desktop, option):
	'''(str,dict) -> NoneType
	Очистка рабочего стола используя настройки 'option'
	'''
	root, dir, files = iter(os.walk(path_to_desktop)).next()
	for file in files:
		for name_folder, ext in option.items():
			for e in ext:
				if e in file:
					new_folder = path + name_folder
					path_file = path + file
					move_file(path_file, new_folder)


if __name__ == '__main__':
	option = {
		'document': ('.txt', '.doc', '.pdf'),
		'pictures': ('.jpg','.png', '.gif'),
	}
	path = '/Users/dmitriydmitrienko/Desktop/'
	cleand_desktop(path_to_desktop, option)


