import os
import json

base_folder = 'native_client'


def start():
    print('Native client:')
    setup()


def setup():
    if os.path.isdir(base_folder) is False:
        print('Производится установка')
        os.mkdir(base_folder)
        os.mkdir(f'{base_folder}\\bin')
        with open(f'{base_folder}\\settings.json', 'w') as io_file:
            settings_text = {'Game Folder': None}
            json.dump(settings_text, io_file, indent=2)
    else:
        pass
    os.system('cls')
    main()


def main():
    if os.listdir(path=f'{base_folder}\\bin').__len__() > 0:
        with open(f'{base_folder}\\settings.json', 'r') as io_file:
            global game_folder
            game_folder = json.load(io_file)['Game Folder']
        if 'NativeTrainer.asi' in os.listdir(path=game_folder):
            print('Трейнер уже установлен, хотите его откючить?\n'
                  '[1] Да\n'
                  '[2] Нет')
            while True:
                q = input('>> ')
                if q in ['1', '2']:
                    if q == '1':
                        disable()
                        print('Отключение прошло успешно!')
                        stop()
                    else:
                        stop()
                else:
                    print('Неизвесный индекс')
                    continue
        else:
            print('Трейнер не установлен, хотите его установить?\n'
                  '[1] Да\n'
                  '[2] Нет')
            while True:
                q = input('>> ')
                if q in ['1', '2']:
                    if q == '1':
                        enable()
                        print('Установка прошла успешно!')
                        stop()
                    else:
                        stop()
                else:
                    print('Неизвесный индекс')
                    continue
    else:
        print('Трейнер отсутствует в папке "bin"')
        stop()


def stop():
    input('Нажмите Enter что-бы выйти...\n')
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
    start()
