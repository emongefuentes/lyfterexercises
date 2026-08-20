import csv

with open("games_csv.csv", 'r', encoding='utf-8') as file:
    read_file = csv.DictReader(file)
    for fila in read_file:
        for colum in fila:
            print(fila , colum)