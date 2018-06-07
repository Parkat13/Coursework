# -*- coding: utf-8 -*-
import time
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
f_obuch = codecs.open('text.txt', 'r', 'utf8')
#f_slovosoch = codecs.open('group_1.txt', 'r', 'utf8')
f_finish = open('text_dipSubstitute.txt', 'w')
f_group = codecs.open('TF_substitute_phrases.txt', 'r', 'utf8')
words_group_normal = f_group.read().split()
dict = {}
for i in range(len(words_group_normal)//3):
    dict[words_group_normal[i*3] + ' ' + words_group_normal[i*3+1]] = 0
words_str = f_obuch.read(100000000)
flag_last_word = 0
if words_str[-1] == ' ':
    flag_last_word = 1
words = words_str.split()
str_nul = ''
if len(words) == 1:
    words.append(' ')
k = 0
while len(words) != 0:
    start_time = time.time()
    for j in range(len(words)-1):
        words[j] = words[j].lower()
        if (str_nul + ' ' + words[j]) in dict:
            f_finish.write(str_nul + '_' + words[j] + ' ')
            if (words[j] + ' ' + words[j + 1]) in dict:
                str_nul = words[j]
            else:
                str_nul = ''
        else:
            f_finish.write(str_nul + ' ')
            str_nul = words[j]
    print (k, "--- %s seconds ---" % (time.time() - start_time))
    k += 1
    if flag_last_word == 1:
        words_str = (words[-1] + ' ' + f_obuch.read(100000000).strip())
    else:
        words_str = (words[-1] + f_obuch.read(100000000).strip())
    flag_last_word = 0
    if (words_str == '  ') or (words_str == ' '):
        break
    if words_str[-1] == ' ':
        flag_last_word = 1
    words = words_str.split()
    if len(words) == 1:
        words.append(' ')
f_obuch.close()
#f_slovosoch.close()
f_finish.close()
f_group.close()
