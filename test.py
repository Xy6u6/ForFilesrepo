from datetime import datetime, timedelta, date
import json

my_dict = {'name': 'anton', 'surname': 'voroniuk', 'age': 28, 'birthdate': '1993.03.12',}
my_dict['name']
list_from_my_dict = list(my_dict.values())

my_set = {2, 1, 5, 2, 's', [2, 3, 4]}
birh = datetime(1993, 3, 12).strftime('%d.%m.%y')
# age = date.year - birh.year
for i, k in my_dict.items()
numdict = {
    12: 'a',
    12: 'b',
    52: 'c',
}
my_tuple = ('a', 2, 3, 'f', 's')
tup = ("hell", 2)
sstrin = 'hell'


def make_file(file):
    with open(f'{file}.txt', 'r', encoding='utf-8') as myfile:
        # myfile.write(file)
        # myfile.write(file)
        print(myfile.read())


if __name__ == '__main__':
    # with open('myjson.json', 'w') as file:
    # json.dump(my_dict, file, ensure_ascii=True, indent=4)
    # jsonString = json.dumps(my_dict)
    # print(json.dumps(my_dict), type(json.dumps(my_dict)))
    # print(json.loads(jsonString), type(json.loads(jsonString)))
    with open('text.txt', 'a+') as file:
        file.write('\nfuck')
        file.seek(0)
        print(file.read())
