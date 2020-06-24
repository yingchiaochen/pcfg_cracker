
w = open('Validation_temp_convert.txt', 'w+')


ZHUYIN='ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ˙ˊˇˋ-'
ENGLISH='1qaz2wsxedcrfv5tgbyhnujm8ik,9ol.0p;/-7634 '
END='˙ˊˇˋ-'

zhuyin_to_english = dict()
for (zhuyin, english) in zip(ZHUYIN, ENGLISH):
    zhuyin_to_english[zhuyin] = english

zhuyin_to_english['}'] = ''

with open('Validation_temp.txt', 'r') as f:
    for line in f:
        l = ''
        for i in line:
            if i in zhuyin_to_english:
                l += zhuyin_to_english[i]
            else:
                l += i
        
        w.write(l)

w.close()




