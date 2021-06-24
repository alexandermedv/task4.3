import os

dic = {}
directory = 'Text_files'

# Сохраняем в словарь список всех файлов с количеством строк
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
            text = f.readlines()
            dic[filename] = len(text)

# Преобразование словаря в список кортежей, сортировка по второму значению
dic = sorted(dic.items(), key=lambda x: x[1])

# Очистка файла, если он уже существует
with open('result.txt', 'w') as result:
    pass

# Идем по списку файлов и сохраняем их содержимое в новый файл
for item in dic:
    if item[0].endswith(".txt"):
        with open(os.path.join(directory, item[0]), 'r', encoding='utf-8') as f:
            text = f.readlines()

            with open('result.txt', 'a') as result:
                result.write(item[0])
                result.write('\n')
                result.write(str(len(text)))
                result.write('\n')
                for line in text:
                    result.write(line)
                result.write('\n')

print('Создан файл result.txt')
