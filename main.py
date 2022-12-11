import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv


pattern = r'(\+?)(7|8){1}\s*\(*(\d{3})\)*\s*[-]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*\(?\w*\.*\s*(\d{0,4})\)*'

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
print('-' * 100)
print('Исходные данные')
print('-' * 100)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

for row in contacts_list:
    if 'доб' in row[5]:
        row[5] = re.sub(pattern, r'+7(\3)\4-\5-\6 доб.\7', row[5])
    else:
        row[5] = re.sub(pattern, r'+7(\3)\4-\5-\6', row[5])
    word_count = re.split(' ', row[0])
    if len(word_count) == 3:
        row[0] = word_count[0]
        row[1] = word_count[1]
        row[2] = word_count[2]
        continue
    elif len(word_count) == 2:
        row[0] = word_count[0]
        row[1] = word_count[1]
        continue
    else:
        word_count = re.split(' ', row[1])
        if len(word_count) == 2:
            row[1] = word_count[0]
            row[2] = word_count[1]

for i in range(len(contacts_list)):
    for j in range(len(contacts_list)):
        if i != j and contacts_list[i][0] == contacts_list[j][0] and contacts_list[i][1] == contacts_list[j][1]:
            for k in range(2, 7):
                if contacts_list[i][k] != contacts_list[j][k]:
                    contacts_list[i][k] += contacts_list[j][k]
            contacts_list[j][0] = 'double'

new_contacts_list = [row for row in contacts_list if row[0] != 'double']
print('-' * 100)
print('Результат обработки')
print('-' * 100)
pprint(contacts_list)
pprint(new_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
