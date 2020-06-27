import sys

path = sys.argv[1]
filename = sys.argv[2]

fg = open(path, 'r')
d = dict()

count = 0
for line in fg:
    line = line.strip('\n')
    count += 1
    if count % 1000000 == 0:
        print(f'{count // 1000000} M lines')
    if line not in d:
        d[line] = 0
    
fg.close()

fw = open(filename, 'w+')
count = 0

with open('../../testing_data/testing_pass', 'r') as f:
    for line in f:
        line = line.strip('\n')
        count += 1
        if count % 1000000 == 0:
            print(f'{count // 1000000} M lines')
        if line in d:
            print(line)
            fw.write(line + '\n')

    











