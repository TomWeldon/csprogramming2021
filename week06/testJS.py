# Creating a json file. Then reading in dat and then printing the data
# Author: Tom Weldon

import json

filename = 'testdict.json'

sample =  dict(name = 'Fred', age = 31, grades =[1,34,55])


def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

writeDict(sample)


def readDict():
    with open(filename) as f:
        return json.load(f)

somedict = readDict()

print(somedict)