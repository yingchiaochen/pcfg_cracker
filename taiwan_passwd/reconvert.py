
ZHUYIN='ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ˙ˊˇˋ-'
ENGLISH='1qaz2wsxedcrfv5tgbyhnujm8ik,9ol.0p;/-7634 '
END='˙ˊˇˋ-'

english_to_zhuyin = dict()
for (zhuyin, english) in zip(ZHUYIN, ENGLISH):
    english_to_zhuyin[english] = zhuyin
    english_to_zhuyin[english.upper()] = zhuyin

## for analyze zhuyin pattern
for i in range(1, 8):
    file = f'../Rules/ZhuyinTest/Zhuyin/{i}.txt'
    count = 0
    result = []

    with open(file, "r") as f:
        for line in f:
            l = line.split()
            r = ''
            for ch in l[0]:
                r += english_to_zhuyin[ch]

            result.append((r, l[1].strip('\n')))
            print(r)
            # result.append(r[1])

    with open(f"analyze/ztest{i}.txt", 'w+') as f:
        for i in result:
            f.write(i[0] + '\t' + i[1] + '\n')






