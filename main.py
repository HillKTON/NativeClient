import os

base_folder = 'native_client'


def start():
    print('Native client:')
    setup()


def setup():
    if os.path.isdir(base_folder) is False:
        print('Производится установка')
        os.mkdir(base_folder)
        os.mkdir(f'{base_folder}\\bin')
    else:
        pass
    os.system('cls')
    main()


def main():
    if os.listdir(path=f'{base_folder}\\bin').__len__() > 0:
        if 'NativeTrainer.asi' in os.listdir(path='.'):
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
                        print('Успех!')
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
        with open(file, 'wb') as io_file:
            io_file.write(files[file])


def disable():
    file_names = os.listdir(path=f"{base_folder}\\bin")
    for name in file_names:
        os.remove(name)


if __name__ == '__main__':
    start()
