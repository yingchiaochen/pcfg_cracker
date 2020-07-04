import search

x = search.SearchZhuyin()
# nguess = ['nguess1.txt', 'nguess2.txt', 'nguess3.txt']
# omen_nguess = ['omen_nguess1.txt', 'omen_nguess2.txt', 'omen_nguess3.txt']
# # zguess = ['zguess1.txt', 'zguess2.txt', 'zguess3.txt']
# z2guess = ['z2guess1.txt', 'z2guess2.txt', 'z2guess3.txt']
# z3guess = ['z3guess1.txt', 'z3guess2.txt', 'z3guess3.txt']
# omen_z2guess = ['omen_z2guess1.txt', 'omen_z2guess2.txt', 'omen_z2guess3.txt']
# omen_z3guess = ['omen_z3guess1.txt', 'omen_z3guess2.txt', 'omen_z3guess3.txt']
# new_zhuyin3 = ['new_z3guess1.txt']
# no_zhuyin = ['nzguess1.txt']

# nw = open('nfinal.txt', 'w+')
# z2w = open('z2final.txt', 'w+')
# z3w = open('z3final.txt', 'w+')
# omen_nw = open('omen_nfinal.txt', 'w+')
# omen_z2w = open('omen_z2final.txt', 'w+')
# omen_z3w = open('omen_z3final.txt', 'w+')
# newz3w = open('newz3final.txt', 'w+')
# nzw = open('nzfinal.txt', 'w+')


# nd = dict()
# z2d = dict()
# z3d = dict()
# omen_nd = dict()
# omen_z2d = dict()
# omen_z3d = dict()
# newz3d= dict()
# nzd = dict()

# ncount = 0
# z2count = 0
# z3count = 0
# omen_ncount = 0
# omen_z2count = 0
# omen_z3count = 0
# newz3count= 0
# nzcount = 0

# for file in nguess:
#     with open(file, 'r') as f:
#         for line in f:
#             line = line.strip('\n')
#             if line not in nd:
#                 nd[line] = 0
#                 nw.write(line + '\n')
#                 ncount += 1
#             else:
#                 nd[line] += 1

# for file in z2guess:
#     with open(file, 'r') as f:
#         for line in f:
#             line = line.strip('\n')
#             if line not in z2d:
#                 z2d[line] = 0
#                 z2w.write(line + '\n')
#                 z2count += 1
#             else:
#                 z2d[line] += 1

# for file in z3guess:
#     with open(file, 'r') as f:
#         for line in f:
#             line = line.strip('\n')
#             if line not in z3d:
#                 z3d[line] = 0
#                 z3w.write(line + '\n')
#                 z3count += 1
#             else:
#                 z3d[line] += 1

# for file in omen_nguess:
#     with open(file, 'r') as f:
#         for line in f:
#             line = line.strip('\n')
#             if line not in omen_nd:
#                 omen_nd[line] = 0
#                 omen_nw.write(line + '\n')
#                 omen_ncount += 1
#             else:
#                 omen_nd[line] += 1

# for file in omen_z2guess:
#     with open(file, 'r') as f:
#         for line in f:
#             line = line.strip('\n')
#             if line not in omen_z2d:
#                 omen_z2d[line] = 0
#                 omen_z2w.write(line + '\n')
#                 omen_z2count += 1
#             else:
#                 omen_z2d[line] += 1

# for file in omen_z3guess:
#     with open(file, 'r') as f:
#         for line in f:
#             line = line.strip('\n')
#             if line not in omen_z3d:
#                 omen_z3d[line] = 0
#                 omen_z3w.write(line + '\n')
#                 omen_z3count += 1
#             else:
#                 omen_z3d[line] += 1

# for file in new_zhuyin3:
#     with open(file, 'r') as f:
#         for line in f:
#             line = line.strip('\n')
#             if line not in newz3d:
#                 newz3d[line] = 0
#                 newz3w.write(line + '\n')
#                 newz3count += 1
#             else:
#                 newz3d[line] += 1

# for file in no_zhuyin:
#     with open(file, 'r') as f:
#         for line in f:
#             line = line.strip('\n')
#             if line not in nzd:
#                 nzd[line] = 0
#                 nzw.write(line + '\n')
#                 nzcount += 1
#             else:
#                 nzd[line] += 1

# x = search.SearchZhuyin()

# nl = []
# z2l = []
# z3l = []
# omen_nl = []
# omen_z2l = []
# omen_z3l = []
# newz3l = []
# nzl = []

# f2 = open('z2_zhu.txt', 'w+')
# f3 = open('z3_zhu.txt', 'w+')
# fnew = open('new_z3.txt', 'w+')
# fnz = open('nz.txt', 'w+')

# for password in list(nd.keys()):
#     success, ret = x.search(password)
#     if success:
#         # print(ret)
#         nl.append(ret)

# for password in list(z2d.keys()):
#     success, ret = x.search(password)
#     f2.write(password + '\n')
#     if success:
#         # print(ret)
#         z2l.append(ret)

# for password in list(z3d.keys()):
#     success, ret = x.search(password)
#     f3.write(password + '\n')
#     if success:
#         # print(ret)
#         z3l.append(ret)

# for password in list(omen_nd.keys()):
#     success, ret = x.search(password)
#     if success:
#         # print(ret)
#         omen_nl.append(ret)

# for password in list(omen_z2d.keys()):
#     success, ret = x.search(password)
#     if success:
#         # print(ret)
#         omen_z2l.append(ret)

# for password in list(omen_z3d.keys()):
#     success, ret = x.search(password)
#     if success:
#         # print(ret)
#         omen_z3l.append(ret)

# for password in list(newz3d.keys()):
#     success, ret = x.search(password)
#     if success:
#         # print(ret)
#         fnew.write(password + '\n')
#         newz3l.append(ret)

# for password in list(nzd.keys()):
#     success, ret = x.search(password)
#     if success:
#         # print(ret)
#         # fnew.write(ret + '\n')
#         fnz.write(password + '\n')
#         nzl.append(ret)


# print(f'ncount = {ncount}')
# print(f'z2count = {z2count}')
# print(f'z3count = {z3count}')
# print(f'omen_ncount = {omen_ncount}')
# print(f'omen_z2count = {omen_z2count}')
# print(f'omen_z3count = {omen_z3count}')
# print(f'zhuyin in nd = {len(nl)}')
# print(f'zhuyin in z2d = {len(z2l)}')
# print(f'zhuyin in z3d = {len(z3l)}')
# print(f'zhuyin in omen_nd = {len(omen_nl)}')
# print(f'zhuyin in omen_z2d = {len(omen_z2l)}')
# print(f'zhuyin in omen_z3d = {len(omen_z3l)}')
# print(f'zhuyin in newz3l = {len(newz3l)}')
# print(f'zhuyin in nzl = {len(nzl)}')

# nw.close()
# z2w.close() 
# z3w.close()
# omen_nw.close()
# omen_z2w.close()
# omen_z3w.close()
# newz3w.close()
# nzw.close()

l = []
# fw = open('newz2_result.txt', 'w+')
# filename = 'new_z2guess1.txt'
# with open(filename, 'r') as f:
#     for password in f:
#         password = password.strip('\n')
#         success, ret = x.search(password)
#         if success:
#             fw.write(password + '\n')
#             l.append(ret)


# fw = open('markov_result.txt', 'w+')
# fz = open('markov_result_zhu.txt', 'w+')
# filename = 'markov_guess.txt'

# filename_write = 'prince_result.txt'
# filename_zhu = 'prince_result_zhu.txt'
# filename = 'prince_guess.txt'

# filename_write = 'markov_no_result.txt'
# filename_zhu = 'markov_no_result_zhu.txt'
# filename = 'markov_no_guess.txt'

# filename_write = 'markov_0_6_result.txt'
# filename_zhu = 'markov_0_6_result_zhu.txt'
# filename = 'markov_0_6_guess.txt'

# filename_write = 'markov_0_4_result.txt'
# filename_zhu = 'markov_0_4_result_zhu.txt'
# filename = 'markov_0_4_guess.txt'

# filename_write = 'original_8-6_result.txt'
# filename_zhu = 'origianl_8-6_result_zhu.txt'
# filename = 'original_8-6_guess.txt'

# filename_write = 'new_zhuyin_8-6_result.txt'
# filename_zhu = 'new_zhuyin_8-6_result_zhu.txt'
# filename = 'new_zhuyin_8-6_guess.txt'

# filename_write = 'markov_0_8_result.txt'
# filename_zhu = 'markov_0_8_result_zhu.txt'
# filename = 'markov_0_8_guess.txt'

filename_write = 'markov_0_2_result.txt'
filename_zhu = 'markov_0_2_result_zhu.txt'
filename = 'markov_0_2_guess.txt'

fw = open(filename_write, 'w+')
fz = open(filename_zhu, 'w+')

with open(filename, 'r') as f:
    for password in f:
        password = password.strip('\n')
        success, ret = x.search(password)
        if success:
            fw.write(password + '\n')
            fz.write(ret + '\n')
            l.append(ret)

print(f'zhuyin: {len(l)}')

# 100 M
# markov: 64412/648/138
# markov_no: 63644/52/22
# prince: 17846/596/94
# coverage = 0.8: 67377/655/148
# coverage = 0.2: 61976/703/189

# 8.6 M
# original: 45159/2/2
# newzhuyin: 47285/558/79




