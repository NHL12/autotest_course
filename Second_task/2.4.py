#Задание 4: Дан абсолютный путь до файла.
# Выведем название файла без расширения, названия диска и корневой папки.

path = 'C:/Users/ns.grigorova/python3/myfile.txt'

print("Есть абсолютный путь до файла: ", path)
file_name = path.split('/')[-1]
file_not_extension = file_name.split('.')[0]
name_disk = path.split(':/')[0]
root_folder = path.split('/')[1]

print("Название файла без расширения: ", file_not_extension)
print("Название диска: ", name_disk)
print("Название корневой папки: ", root_folder)
