
f1 = open("../../Rules/ZhuyinRule/Zhuyin/1.txt", 'r')
f2 = open("../../Rules/ZhuyinRule/Zhuyin/2.txt", 'r')
f3 = open("../../Rules/ZhuyinRule/Zhuyin/3.txt", 'r')
f4 = open("../../Rules/ZhuyinRule/Zhuyin/4.txt", 'r')
f5 = open("../../Rules/ZhuyinRule/Zhuyin/5.txt", 'r')
f6 = open("../../Rules/ZhuyinRule/Zhuyin/6.txt", 'r')
f7 = open("../../Rules/ZhuyinRule/Zhuyin/7.txt", 'r')

with open("wordlist_with_zhuyin.txt", "w+") as fw:
    for line in f1:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')

    for line in f2:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')
        
    for line in f3:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')

    for line in f4:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')

    for line in f5:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')

    for line in f6:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')

    for line in f7:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
      




