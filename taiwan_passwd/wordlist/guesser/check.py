import search

nguess = ['nguess1.txt', 'nguess2.txt', 'nguess3.txt']
zguess = ['zguess1.txt', 'zguess2.txt', 'zguess3.txt']

nw = open('nfinal.txt', 'w+')
zw = open('zfinal.txt', 'w+')

nd = dict()
zd = dict()

ncount = 0
zcount = 0

for file in nguess:
    with open(file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line not in nd:
                nd[line] = 0
                nw.write(line + '\n')
                ncount += 1
            else:
                nd[line] += 1

for file in zguess:
    with open(file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line not in zd:
                zd[line] = 0
                zw.write(line + '\n')
                zcount += 1



x = search.SearchZhuyin()

nl = []
zl = []

for password in list(nd.keys()):
    success, ret = x.search(password)
    if success:
        # print(ret)
        nl.append(ret)

for password in list(zd.keys()):
    success, ret = x.search(password)
    if success:
        # print(ret)
        zl.append(ret)

print(f'ncount = {ncount}')
print(f'zcount = {zcount}')
print(f'zhuyin in nd = {len(nl)}')
print(f'zhuyin in zd = {len(zl)}')

nw.close()
zw.close() 




