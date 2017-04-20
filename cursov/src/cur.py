# -*- coding: utf-8 -*-
import sys
import time
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
reload(sys)
sys.setdefaultencoding('utf-8')
f_obuch = codecs.open('global_text.txt', 'r', 'utf8')
f_slovosoch = codecs.open('group_1.txt', 'r', 'utf8')
f_finish = open('text_group_1.txt', 'w')
f_group = open('group1.txt', 'w')
words_group_normal = []
words_group = f_slovosoch.read().split()
for wd in range(len(words_group)):
    words_group_normal.append(morph.parse(words_group[wd].lower())[0].normal_form)
f_group.write(' '.join(words_group_normal))
f_group.close()
words_str = f_obuch.read(149).strip()
while (len(words_str) != 0) and (((words_str[0] >= 'a') and (words_str[0] <= 'z')) or (words_str[0] == ' ')):
    words_str = words_str[1:]
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
    for word in words[0:-1]:
        flag_sl = 0
        word = word.lower()
        for i in range(len(words_group_normal) / 2):
            if (words_group_normal[2 * i] + words_group_normal[2 * i + 1]) == (str_nul + word):
                f_finish.write(str_nul + '-' + word + ' ')
                flag_sl = 1
                break
        if flag_sl == 1:
            str_nul = ''
        else:
            f_finish.write(str_nul + ' ')
            str_nul = word
    print k, "--- %s seconds ---" % (time.time() - start_time)
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
f_slovosoch.close()
f_finish.close()
