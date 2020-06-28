
ZHUYIN='ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ˙ˊˇˋ-'
ENGLISH='1qaz2wsxedcrfv5tgbyhnujm8ik,9ol.0p;/-7634 '
END='˙ˊˇˋ-'

english_to_zhuyin = dict()
for (zhuyin, english) in zip(ZHUYIN, ENGLISH):
    english_to_zhuyin[english] = zhuyin
    english_to_zhuyin[english.upper()] = zhuyin

english_to_zhuyin['}'] = ''

fn = open('nfinal_trans.txt', 'w+')
f2 = open('z2_zhu_trans.txt', 'w+')
f3 = open('z3_zhu_trans.txt', 'w+')

with open('nfinal.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        r = ''
        for ch in line:
            if ch in english_to_zhuyin:
                r += english_to_zhuyin[ch]
            else: 
                r += ch

        fn.write(r + '\n')
        print(r)

## for analyze zhuyin pattern
with open('z2_zhu.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        r = ''
        for ch in line:
            if ch in english_to_zhuyin:
                r += english_to_zhuyin[ch]
            else:
                r += ch

        f2.write(r + '\n')
        print(r)

with open('z3_zhu.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        r = ''
        for ch in line:
            if ch in english_to_zhuyin:
                r += english_to_zhuyin[ch]
            else:
                r += ch

        f3.write(r + '\n')
        print(r)







