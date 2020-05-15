import os
import json
from colorama import init as color_init
from termcolor import colored
from time import sleep

base_folder = 'native_client'
__version__ = '1.0 (15.05.2020)'


def start():
    os.system('cls')
    color_init()
    print(f'Версия: {__version__}')
    description = 'Программа не для продажи...\n\n' \
                  'NativeClient предназначен для быстрой установки и удаления чита NativeTrainer, для использования\n' \
                  'переместите файлы чита в папку "native_client\\bin", а также укажите путь до папки игры в файле\n' \
                  '"native_client\\settings.json", вместо "none". Путь должен быть в формате\n' \
                  '"D:\\\\Steam\\\\steamapps\\\\common\\\\Grand Theft Auto V"\n'
    print(colored(description, 'yellow'))
    main()


def setup():
    os.system('cls')
    if os.path.isdir(base_folder) is False:
        print(colored('Производится установка', 'yellow'))
        sleep(1)
        os.mkdir(base_folder)
        os.mkdir(f'{base_folder}\\bin')
        with open(f'{base_folder}\\settings.json', 'w') as io_file:
            settings_text = {'Game Folder': None}
            json.dump(settings_text, io_file, indent=2)
        print(colored('Установка прошла успешно', 'yellow'))
        sleep(3)
    else:
        pass
    start()


def main():
    if os.listdir(path=f'{base_folder}\\bin').__len__() > 0:
        with open(f'{base_folder}\\settings.json', 'r') as io_file:
            global game_folder
            game_folder = json.load(io_file)['Game Folder']
        if 'NativeTrainer.asi' in os.listdir(path=game_folder):
            print(colored('Трейнер уже установлен, хотите его удалить?\n'
                          '[1] Да\n'
                          '[2] Нет', 'green'))
            while True:
                q = input('\n>> ')
                if q in ['1', '2']:
                    if q == '1':
                        disable()
                        print(colored('\nУдаление прошло успешно!', 'cyan'))
                        stop()
                    else:
                        stop()
                else:
                    print(colored('\nНеизвесный индекс', 'cyan'))
                    continue
        else:
            print(colored('Трейнер не установлен, хотите его установить?\n'
                          '[1] Да\n'
                          '[2] Нет', 'cyan'))
            while True:
                q = input('\n>> ')
                if q in ['1', '2']:
                    if q == '1':
                        enable()
                        print(colored('\nУстановка прошла успешно!', 'cyan'))
                        stop()
                    else:
                        stop()
                else:
                    print(colored('\nНеизвесный индекс', 'cyan'))
                    continue
    else:
        print(colored('\nТрейнер отсутствует в папке "bin"', 'cyan'))
        stop()


def stop():
    input(colored('Нажмите Enter что-бы выйти...\n', 'yellow'))
    quit()


def enable():
    file_names = os.listdir(path=f"{base_folder}\\bin")
    files = {}
    for name in file_names:
        with open(f"{base_folder}\\bin\\{name}", 'rb') as io_file:
            files[name] = io_file.read()
    for file in files:
        with open(f'{game_folder}\\{file}', 'wb') as io_file:
            io_file.write(files[file])


def disable():
    file_names = os.listdir(path=f"{base_folder}\\bin")
    for name in file_names:
        os.remove(f'{game_folder}\\{name}')


if __name__ == '__main__':
    setup()
