#filename = 'test-a.txt'

with open(filename, 'r') as f:
    data = f.read('test a\n')
    print(data)


with open('test-a.txt', r') as f2:
    data = f2.write('another line')
    print(data)    