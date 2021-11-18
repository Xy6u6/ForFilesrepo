import csv
import json

with open('mycsv.csv','r') as f:
    reader = csv.DictReader(f)
    mydict = [reader]
    for i in reader:
        mydict = [i]
    print(mydict,type(mydict))
with open('myjson.json', 'w') as f:
    jsonstring = json.dumps(mydict)
    json.dump(mydict,f, indent=4)

