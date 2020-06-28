import search

nguess = ['nguess1.txt', 'nguess2.txt', 'nguess3.txt']
omen_nguess = ['omen_nguess1.txt', 'omen_nguess2.txt', 'omen_nguess3.txt']
# zguess = ['zguess1.txt', 'zguess2.txt', 'zguess3.txt']
z2guess = ['z2guess1.txt', 'z2guess2.txt', 'z2guess3.txt']
z3guess = ['z3guess1.txt', 'z3guess2.txt', 'z3guess3.txt']
omen_z2guess = ['omen_z2guess1.txt', 'omen_z2guess2.txt', 'omen_z2guess3.txt']
omen_z3guess = ['omen_z3guess1.txt', 'omen_z3guess2.txt', 'omen_z3guess3.txt']


nw = open('nfinal.txt', 'w+')
z2w = open('z2final.txt', 'w+')
z3w = open('z3final.txt', 'w+')
omen_nw = open('omen_nfinal.txt', 'w+')
omen_z2w = open('omen_z2final.txt', 'w+')
omen_z3w = open('omen_z3final.txt', 'w+')


nd = dict()
z2d = dict()
z3d = dict()
omen_nd = dict()
omen_z2d = dict()
omen_z3d = dict()

ncount = 0
z2count = 0
z3count = 0
omen_ncount = 0
omen_z2count = 0
omen_z3count = 0

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

for file in z2guess:
    with open(file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line not in z2d:
                z2d[line] = 0
                z2w.write(line + '\n')
                z2count += 1
            else:
                z2d[line] += 1

for file in z3guess:
    with open(file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line not in z3d:
                z3d[line] = 0
                z3w.write(line + '\n')
                z3count += 1
            else:
                z3d[line] += 1

for file in omen_nguess:
    with open(file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line not in omen_nd:
                omen_nd[line] = 0
                omen_nw.write(line + '\n')
                omen_ncount += 1
            else:
                omen_nd[line] += 1

for file in omen_z2guess:
    with open(file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line not in omen_z2d:
                omen_z2d[line] = 0
                omen_z2w.write(line + '\n')
                omen_z2count += 1
            else:
                omen_z2d[line] += 1

for file in omen_z3guess:
    with open(file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line not in omen_z3d:
                omen_z3d[line] = 0
                omen_z3w.write(line + '\n')
                omen_z3count += 1
            else:
                omen_z3d[line] += 1


x = search.SearchZhuyin()

nl = []
z2l = []
z3l = []
omen_nl = []
omen_z2l = []
omen_z3l = []

f2 = open('z2_zhu.txt', 'w+')
f3 = open('z3_zhu.txt', 'w+')

for password in list(nd.keys()):
    success, ret = x.search(password)
    if success:
        print(ret)
        nl.append(ret)

for password in list(z2d.keys()):
    success, ret = x.search(password)
    f2.write(password + '\n')
    if success:
        # print(ret)
        z2l.append(ret)

for password in list(z3d.keys()):
    success, ret = x.search(password)
    f3.write(password + '\n')
    if success:
        # print(ret)
        z3l.append(ret)

for password in list(omen_nd.keys()):
    success, ret = x.search(password)
    if success:
        # print(ret)
        omen_nl.append(ret)

for password in list(omen_z2d.keys()):
    success, ret = x.search(password)
    if success:
        # print(ret)
        omen_z2l.append(ret)

for password in list(omen_z3d.keys()):
    success, ret = x.search(password)
    if success:
        # print(ret)
        omen_z3l.append(ret)


print(f'ncount = {ncount}')
print(f'z2count = {z2count}')
print(f'z3count = {z3count}')
print(f'omen_ncount = {omen_ncount}')
print(f'omen_z2count = {omen_z2count}')
print(f'omen_z3count = {omen_z3count}')
print(f'zhuyin in nd = {len(nl)}')
print(f'zhuyin in z2d = {len(z2l)}')
print(f'zhuyin in z3d = {len(z3l)}')
print(f'zhuyin in omen_nd = {len(omen_nl)}')
print(f'zhuyin in omen_z2d = {len(omen_z2l)}')
print(f'zhuyin in omen_z3d = {len(omen_z3l)}')

nw.close()
z2w.close() 
z3w.close()
omen_nw.close()
omen_z2w.close()
omen_z3w.close()





