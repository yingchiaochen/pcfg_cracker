import os

os.system("python3 merge_zhuyin.py")
os.system("python3 merge_english.py")
os.system("python3 merge_breach.py")


# merge three data set
f1 = open("wordlist_with_zhuyin.txt", 'r')
f2 = open("wordlist_without_zhuyin.txt", 'r')
f3 = open("wordlist_breach.txt", 'r')

with open("wordlist_training_set.txt", "w+") as fw:
    for line in f1:
        if len(line) < 32:
            fw.write(line)

    for line in f2:
        if len(line) < 32:
            fw.write(line)

    for line in f3:
        if len(line) < 32:
            fw.write(line)

f1.close()
f2.close()
f3.close()


