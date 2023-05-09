#Задание 4: Дан абсолютный путь до файла.
# Выведем название файла без расширения, названия диска и корневой папки.

path = 'C:/Users/ns.grigorova/python3/myfile.txt'

#находим название файла с расширением
file_name = path.split('/')[-1]
#находим название файла без расширения
file_not_extension = file_name.split('.')[0]
#находим название диска
name_disk = path.split(':/')[0]
#находим название корневой папки
root_folder = path.split('/')[1]

print("Название файла без расширения: ", file_not_extension)
print("Название диска: ", name_disk)
print("Название корневой папки: ", root_folder)
