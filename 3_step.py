# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f_result_1 = open('01.txt', 'r')
f_result_2 = open('02.txt', 'r')
res_list = open('res_list.txt','w')
results_1 = f_result_1.read().split()
list_res = []
for i in range(len(results_1)/3):
    list_res.append([results_1[3 * i], results_1[3 * i + 2], 'T'])
results_2 = f_result_2.read().split()
for i in range(len(results_2)/3):
    list_res.append([results_2[3 * i], results_2[3 * i + 2], 'N'])
m = []
for i in range(len(list_res)):
    for j in range(i):
        if float(list_res[i][1]) < float(list_res[j][1]):
            m = list_res[i]
            list_res[i] = list_res[j]
            list_res[j] = m
sum = 0.0
ch = 0.0
for i in range(len(list_res)):
    if list_res[i][2] == 'T':
        sum += (ch + 1)/(i + 1)
        ch += 1
    res_list.write(' '.join(list_res[i]) + '\n')
print str(sum/ch)
f_result_1.close()
f_result_2.close()