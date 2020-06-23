######################
#
# This function is to detect Zhuyin pattern.
# pattern example: 
# EX1: '123ㄨㄛˇ456ㄞˋ789ㄋㄧˇ' : [('123', None), ('ㄨㄛˇ', Z1), ('456', None), ('ㄞˋ', 'Z1'), ('789', None), ('ㄋㄧˇ', 'Z1')]
# EX2: '123ㄨㄛˇㄞˋㄋㄧˇ' : [('123', None), ('ㄨㄛˇㄞˋㄋㄧˇ', Z3)]
# 
######################
from .search import SearchZhuyin


def detect_zhuyin(section, zdic):
    # print(section)
    parsing = []
    zhuyin_word = []
    temp = []

    start = -1
    current = 0
    index = 0
    END = '˙ˊˇˋ-}'

    # ex: '123ㄨㄛˇ456ㄞˋ789ㄋㄧˇ'
    while index < len(section):
        # not a zhuyin character
        if section[index] not in zdic:
            # the segment may be wrong, i.e., not detect char in END, abandon this segment
            if start != -1:
                start = -1

            # no more consecutive zhuyin word detected, add it in zhuyin word
            if len(temp) != 0:
                zstring = ''.join(temp)
                parsing.append((zstring, 'Z' + str(len(temp))))
                zhuyin_word.append((zstring, len(temp)))
                temp = []

            index += 1
            continue
        
        # print(section[index])
        # the start of a zhuyin word, add the previous segment in the parsing
        # not index + 1 because we should not include the index character
        if current != index:
            parsing.append((section[current:index], None))

        # the end of a zhuyin word
        if section[index] in END:
            # not correct operation
            if start == -1:
                index += 1
                current = index
                continue

            s = section[start:index + 1]
            l = ''
            for i in s:
                l += zdic[i]
            
            temp.append(l)
            start = -1

        else:
            # save the start position of the zhuyin character
            if start == -1:
                start = index

        index += 1
        current = index
    
    if len(temp) != 0:
        zstring = ''.join(temp)
        parsing.append((zstring, 'Z' + str(len(temp))))
        zhuyin_word.append((zstring, len(temp)))
        temp = []

    # print(f'parsing = {parsing}')
    # detect zhuyin pattern
    if len(zhuyin_word) > 0:
        return parsing, zhuyin_word

    return parsing, None


def zhuyin_detection(section_list, x):
    zhuyin_list = []

    ZHUYIN = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ˙ˊˇˋ-'
    ENGLISH = '1qaz2wsxedcrfv5tgbyhnujm8ik,9ol.0p;/-7634 '
    zhuyin_to_english = dict()

    for (zhuyin, english) in zip(ZHUYIN, ENGLISH):
        zhuyin_to_english[zhuyin] = english

    zhuyin_to_english['}'] = ''

    index = 0
    while index < len(section_list):
        # if not had been classified as one of the categories
        if section_list[index][1] == None:
            r = x.search(section_list[index][0])
            parsing, zhuyin_string = detect_zhuyin(r[1], zhuyin_to_english)

            # if a zhuyin string was detected
            if zhuyin_string != None:
                # print(zhuyin_string)
                # zhuyin_list.append(zhuyin_string)
                zhuyin_list.extend(zhuyin_string)

                # This is a trick to use the list extend but at an index
                del section_list[index]
                section_list[index:index] = parsing
            
        index += 1

    return zhuyin_list










