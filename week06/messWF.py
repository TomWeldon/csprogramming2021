import os.path

filename = 'count2.txt'



def writeNumber(number):
    with open(filename, 'wt') as f:
        f.write(str(number))

if not os.path.isfile(filename):
    print('File does not exist')
    writeNumber(0)