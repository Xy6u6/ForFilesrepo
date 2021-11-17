import csv

name1 = 'Anton'
name2 = 'Elena'
names = [("header1", "header2"),
         [name1, 'Voroniuk'],
         [name2, 'Vironiuk'],
         ["Alexandr", 'Voroniuk']
         ]
with open('mycsv.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(
        names
    )
with open('mycsv.csv', 'r') as file:
    data = csv.DictReader(file, delimiter=',')
    for i in data:
        print(i, type(i))