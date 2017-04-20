# -*- coding: utf-8 -*-
import sys
import time
import codecs
import math
reload(sys)
sys.setdefaultencoding('utf-8')
f_vectors = open('result_group_2.txt', 'r')
f_results = open('results_2.txt', 'w')
f_group = open('group2.txt', 'r')
group = f_group.read().split()
words_group = []
for i in range(len(group)/2):
    words_group.append(group[2 * i] + '_' + group[2 * i + 1])
    words_group.append(group[2 * i])
    words_group.append(group[2 * i + 1])
word_vector = f_vectors.readline().split()
group_vectors = []
for i in range(len(words_group)):
    group_vectors.append([])
start = time.time()
while len(word_vector) != 0:
    for j in range(len(words_group)):
        if word_vector[0] == words_group[j]:
            group_vectors[j] = word_vector[1:]
    word_vector = f_vectors.readline().split()
print "--- %s seconds ---" % (time.time() - start)
for i in range(len(words_group)/3):
    multi1, multi2, sq1, sq2, sq3 = 0.0, 0.0, 0.0, 0.0, 0.0
    vector1 = group_vectors[3 * i]
    vector2 = group_vectors[3 * i + 1]
    vector3 = group_vectors[3 * i + 2]
    flag1, flag2 = 0, 0
    if len (vector1) == 0:
        f_results.write(words_group[3 * i] + u' - Нет в словаре\n')
        continue
    if len(vector1) == 0:
        f_results.write(words_group[3 * i + 1] + u' - Нет в словаре\n')
        flag1 = 1
    if len(vector1) == 0:
        f_results.write(words_group[3 * i + 2] + u' - Нет в словаре\n')
        flag2 = 1
    for j in range(len(vector1)):
        sq1 += float(vector1[j]) ** 2
        if flag1 == 0:
            multi1 += float(vector1[j]) * float(vector2[j])
            sq2 += float(vector2[j]) ** 2
        if flag2 == 0:
            multi2 += float(vector1[j]) * float(vector3[j])
            sq3 += float(vector3[j]) ** 2
    if flag1 == 0:
        f_results.write(words_group[3 * i] + ' ' + words_group[3 * i + 1] + u' : ' + str(multi1 / (math.sqrt(sq1) * math.sqrt(sq2))) + '\n')
    if flag2 == 0:
        f_results.write(words_group[3 * i] + ' ' + words_group[3 * i + 2] + u' : ' + str(multi2 / (math.sqrt(sq1) * math.sqrt(sq3))) + '\n')
f_vectors.close()
f_results.close()
f_group.close()
