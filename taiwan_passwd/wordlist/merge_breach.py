
f1 = open("../Breach1_convert.txt", 'r')
f2 = open("../Breach2_convert.txt", 'r')
f3 = open("../Validation_temp_convert.txt", 'r')


with open("wordlist_breach.txt", "w+") as fw:
    for line in f1:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')

    for line in f2:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')

    for line in f3:
        line = line.strip('\n').split('\t')
        fw.write(line[0] + '\n')

f1.close()  
f2.close()  
f3.close()  

