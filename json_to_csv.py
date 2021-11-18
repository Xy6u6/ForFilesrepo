import json
import csv


def open_json():
    with open('myjson.json', 'r') as f:
        data = json.load(f)
    return data


def write_to_csv(data):
    with open('mycsv.csv', 'w', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in data:
            writer.writerow(i)


if __name__ == '__main__':
    data = open_json()
    write_to_csv(data)
