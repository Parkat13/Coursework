# -*- coding: utf-8 -*-
import sys
import time
import codecs
import math
reload(sys)
sys.setdefaultencoding('utf-8')
f_vectors = codecs.open('text_output.txt', 'r', 'utf8')
f_results = open('second_resWord2vec.txt', 'w')
f_group = codecs.open('second_phrases.txt', 'r', 'utf8')
group = f_group.read().split()
dict = {}
for i in range(len(group)/4):
    dict[group[4 * i + 1] + '_' + group[4 * i + 2]] = 0
    dict[group[4 * i + 1]] = 0
    dict[group[4 * i + 2]] = 0
word_vector = f_vectors.readline().split()
start = time.time()
while len(word_vector) != 0:
    if word_vector[0] in dict:
        dict[word_vector[0]] = word_vector[1:]
    word_vector = f_vectors.readline().split()
print "--- %s seconds ---" % (time.time() - start)
results = {}
for i in range(len(group)/4):
    sq1, sq2, sq3 = 0.0, 0.0, 0.0
    vector1 = dict[group[4 * i + 1] + '_' + group[i * 4 + 2]]
    vector2 = dict[group[4 * i + 1]]
    vector3 = dict[group[4 * i + 2]]
    if vector2 == 0 or vector3 == 0:
        results[group[4 * i] + ' ' + group[4 * i + 1] + ' ' + group[i * 4 + 2]] = 0.0
        continue
    for j in range(len(vector2)):
        sq1 += float(vector1[j]) ** 2
        sq2 += float(vector2[j]) ** 2
        sq3 += float(vector3[j]) ** 2
    sq1 = math.sqrt(sq1)
    sq2, sq3 = math.sqrt(sq2), math.sqrt(sq3)
    sum = 0.0
    sum_vector= 0.0
    for j in range(len(vector2)):
        sum += (float(vector2[j]) / sq2 + float(vector3[j]) / sq3) ** 2
        sum_vector += float(vector1[j]) * (float(vector2[j]) / sq2 + float(vector3[j]) / sq3)
        #sum_vector += float(vector2[j]) * float(vector3[j])
    #f_results.write(words_group[3 * i] + u' : ' + str(sum_vector/ (sq1 * math.sqrt(sum))) + '\n')
    results[group[4 * i] + ' ' + group[4 * i + 1] + ' ' + group[i * 4 + 2]] = math.fabs(sum_vector/ (sq1 * math.sqrt(sum)))
for i in sorted(results, key=results.__getitem__, reverse=False):
    f_results.write(str(i) + ' ' + str(results[i]) + '\n')
f_vectors.close()
f_results.close()
f_group.close()