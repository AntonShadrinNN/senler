from csv import writer
from os import getcwd

def get_id_and_name(row: str):
    name, ident = row.split('\t')
    ident = ident.replace('https://vk.com/id', '').strip()
    return name, ident


def preprocess():
    with open('data/students_flash.txt', encoding='utf-8') as txt_file:
        data = txt_file.readlines()

    data = list(map(get_id_and_name, data))

    with open('data/students.csv', 'w', encoding='utf-8', newline='') as csv_file:
        wr = writer(csv_file)
        wr.writerow(('name', 'id'))
        wr.writerows(data)

