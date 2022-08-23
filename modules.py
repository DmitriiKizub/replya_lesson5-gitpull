import random
import os
import sys
import shutil
import famous_persons
# 3. Сторонние модули
#import gjango
import numpy


# os - основые функции
# возвращает путь до текущей папки
print(os.getcwd())

# список файлов и папок
print(os.listdir())

for i in range(5):
    # Создать папау педеаем путь
    if not os.path.exists(f'new{i}'):
        os.mkdir(f'new{i}')

for i in range(5):
    # удалить папки
    os.rmdir(f'new{i}')

# соединение путей
path = os.path.join(os.getcwd(),'main','other','file.txt')
print(path)

# shutil
shutil.copy('famous_info.py','famous_info_copy.py')

# sys
print(sys.platform)
print(f'{sys.path}\n') # Пути где питон ищет файлы

sys.path.remove('C:\\Users\\d.kizub\\PycharmProjects\\trplya_lessens5')
sys.path.remove('C:\\Users\\d.kizub\\PycharmProjects\\trplya_lessens5')
sys.path.append('/home/dante')

print(sys.path)

print(sys.executable)

