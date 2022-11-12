import tasks1.test
import tasks2.test
import os

technic = [('Ноутбук', 1500, 'Татьяна', '89002001020'),
           ('Смартфон', 500, 'Анна', '89202202325'),
           ('Проектор ', 300, 'Андрей', '89505205656'),
           ('Принтер', 750, 'Игорь', '89303303236'),
           ('Планшет', 2300, 'Игорь', '89303303236'),
           ('Смартфон', 1000, 'Андрей', '89505205656'),
           ('Ноутбук', 4800, 'Татьяна', '89002001020'),
           ('Наушники', 780, 'Марина', '89562002350'),
           ('Сканер', 550, 'Сергей', '89808564559'),
           ('Планшет', 1200, 'Анна', '89202202325'),
           ('Ноутбук', 1100, 'Игорь', '89303303236'),
           ('Смартфон', 3500, 'Татьяна', '89002001020')]

path = os.getcwd()
print(path)
root_path = "/Users/administrator/Documents/GitHub/TASKS/files"
file_list = []
with os.scandir(root_path) as listOfEntries:
    for entry in listOfEntries:
        if entry.is_file():
            file_list.append(entry.name)
print(type(file_list[0]))

tasks1.test.service_center(technic, os.path.join(root_path, file_list[0]))
tasks2.test.file_name(file_list, root_path)
