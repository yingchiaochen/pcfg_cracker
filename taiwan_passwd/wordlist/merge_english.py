import os

fw = open("wordlist_without_zhuyin.txt", "w+")

for dirname in os.listdir("../../Rules/ZhuyinRule"):
    if dirname == 'Alpha':
        for file in os.listdir("../../Rules/ZhuyinRule/" + dirname):
            with open("../../Rules/ZhuyinRule/" + dirname + "/" + file, 'r') as f:
                for line in f:
                    line = line.strip('\n').split('\t')
                    fw.write(line[0] + '\n')

    elif dirname == 'Context':
        for file in os.listdir("../../Rules/ZhuyinRule/" + dirname):
            with open("../../Rules/ZhuyinRule/" + dirname + "/" + file, 'r') as f:
                for line in f:
                    line = line.strip('\n').split('\t')
                    fw.write(line[0] + '\n')

    elif dirname == 'Digits':
        for file in os.listdir("../../Rules/ZhuyinRule/" + dirname):
            with open("../../Rules/ZhuyinRule/" + dirname + "/" + file, 'r') as f:
                for line in f:
                    line = line.strip('\n').split('\t')
                    fw.write(line[0] + '\n')

    elif dirname == 'Emails':
        for file in os.listdir("../../Rules/ZhuyinRule/" + dirname):
            with open("../../Rules/ZhuyinRule/" + dirname + "/" + file, 'r') as f:
                for line in f:
                    line = line.strip('\n').split('\t')
                    fw.write(line[0] + '\n')

    elif dirname == 'Grammer':
        for file in os.listdir("../../Rules/ZhuyinRule/" + dirname):
            with open("../../Rules/ZhuyinRule/" + dirname + "/" + file, 'r') as f:
                for line in f:
                    line = line.strip('\n').split('\t')
                    fw.write(line[0] + '\n')

    elif dirname == 'Keyboard':
        for file in os.listdir("../../Rules/ZhuyinRule/" + dirname):
            with open("../../Rules/ZhuyinRule/" + dirname + "/" + file, 'r') as f:
                for line in f:
                    line = line.strip('\n').split('\t')
                    fw.write(line[0] + '\n')

    elif dirname == 'Other':
        for file in os.listdir("../../Rules/ZhuyinRule/" + dirname):
            with open("../../Rules/ZhuyinRule/" + dirname + "/" + file, 'r') as f:
                for line in f:
                    line = line.strip('\n').split('\t')
                    fw.write(line[0] + '\n')
        
    elif dirname == 'Websites':
        for file in os.listdir("../../Rules/ZhuyinRule/" + dirname):
            with open("../../Rules/ZhuyinRule/" + dirname + "/" + file, 'r') as f:
                for line in f:
                    line = line.strip('\n').split('\t')
                    fw.write(line[0] + '\n')

    elif dirname == 'Years':
        for file in os.listdir("../../Rules/ZhuyinRule/" + dirname):
            with open("../../Rules/ZhuyinRule/" + dirname + "/" + file, 'r') as f:
                for line in f:
                    line = line.strip('\n').split('\t')
                    fw.write(line[0] + '\n')

  

    