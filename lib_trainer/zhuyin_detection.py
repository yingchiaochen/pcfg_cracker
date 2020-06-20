######################
#
# This function is to detect Zhuyin pattern.
# pattern example: []
#
######################

def detect_zhuyin(section, zdic):
    parsing = []
    zhuyin_word = []

    start = -1
    current = 0
    index = 0

    # ex: '123ㄨㄛˇ456ㄞˋ789ㄋㄧˇ'
    while index < len(section):
        # not a zhuyin character
        if section[index] not in zdic:
            index += 1
            continue
        
        # the start of a zhuyin word, add the previous segment in the parsing
        # not index + 1 because we should not include the index character
        if current != index:
            parsing.append((section[current:index], None))

        # the end of a zhuyin word
        if section[index] in '-ˊˇˋ':
            # not correct operation
            if start == -1:
                index += 1
                current = index
                continue

            s = section[start:index + 1]
            l = ''
            for i in s:
                l += zdic[i]

            zhuyin_word.append(l)
            start = -1

        else: 
            # save the start position of the zhuyin character
            if start == -1:
                start = index

        index += 1
        current = index
        
    if len(zhuyin_word) > 0:
        zstring = ''.join(zhuyin_word)
        parsing.append((zstring, len(zhuyin_word)))
        return parsing, (zstring, len(zhuyin_word))

    return parsing, None


def zhuyin_detection(section_list):
    zhuyin_list = []

    zdic = { 'ㄅ' : '1', 
             'ㄆ' : 'q', 
             'ㄇ' : 'a', 
             'ㄈ' : 'z', 
             'ㄉ' : '2', 
             'ㄊ' : 'w', 
             'ㄋ' : 's', 
             'ㄌ' : 'x', 
             'ㄍ' : 'e', 
             'ㄎ' : 'd', 
             'ㄏ' : 'c', 
             'ㄐ' : 'r', 
             'ㄑ' : 'f', 
             'ㄒ' : 'v', 
             'ㄓ' : '5', 
             'ㄔ' : 't', 
             'ㄕ' : 'g', 
             'ㄖ' : 'b', 
             'ㄗ' : 'y', 
             'ㄘ' : 'h', 
             'ㄙ' : 'n', 
             'ㄧ' : 'u', 
             'ㄨ' : 'j', 
             'ㄩ' : 'm', 
             'ㄚ' : '8', 
             'ㄛ' : 'i', 
             'ㄜ' : 'k', 
             'ㄝ' : ',', 
             'ㄞ' : '9', 
             'ㄟ' : 'o', 
             'ㄠ' : 'l', 
             'ㄡ' : '.', 
             'ㄢ' : '0', 
             'ㄣ' : 'p', 
             'ㄤ' : ';', 
             'ㄥ' : '/', 
             'ㄦ' : '-', 
             '-' : '-', 
             'ˊ' : '6', 
             'ˇ' : '3', 
             'ˋ' : '4'
            }

    index = 0
    while index < len(section_list):
        # if not had been classified as one of the categories
        if section_list[index][1] == None:
            parsing, zhuyin_string = detect_zhuyin(section_list[index], zdic)

            # if a zhuyin string was detected
            if zhuyin_string != None:
                zhuyin_list.append(zhuyin_string)

                # This is a trick to use the list extend but at an index
                del section_list[index]
                section_list[index:index] = parsing
            
        index += 1

    return zhuyin_list










