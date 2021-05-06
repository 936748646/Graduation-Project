import csv
import numpy as np
import random
import os
import Levenshtein
import pandas as pd
import matplotlib.pyplot as plt
import math


v_list_ant = [[5, 37, 41, 58, 67, 68, 91],
          [75],
          [18, 37, 66, 78, 90, 105],
          [34, 46],
          [47],
          [5, 21, 41, 55, 105]]
v_list_derbyv1 = [[15, 45, 51, 58, 89, 90, 91, 98],
                  [15, 45, 51, 58, 89, 90, 91, 98],
                  [15, 45, 51, 58, 89, 90, 91, 98],
                  [15, 45, 51, 58, 89, 90, 91, 98],
                  [15, 25, 45, 51, 58, 89, 90, 91, 98],
                  [15, 45, 51, 58, 89, 90, 91, 98],
                  [15, 45, 51, 58, 67, 68, 69, 89, 90, 91, 98]]
v_list_derbyv2 = [[16, 46, 56, 59, 65, 69, 75, 77, 78, 81, 105],
                  [16, 46, 56, 59, 65, 69, 75, 77, 78, 81, 105],
                  [16, 46, 56, 59, 65, 69, 75, 77, 78, 81, 105],
                  [16, 46, 56, 59, 65, 69, 75, 77, 78, 81, 105],
                  [16, 46, 56, 59, 65, 69, 75, 77, 78, 81, 105],
                  [2, 16, 17, 23, 34, 46, 56, 59, 65, 69, 75, 77, 78, 81, 105],
                  [16, 46, 56, 59, 65, 69, 75, 77, 78, 81, 105],
                  [16, 46, 56, 59, 65, 69, 75, 77, 78, 81, 105],
                  [16, 46, 56, 59, 65, 69, 75, 77, 78, 81, 105]]
v_list_derbyv3 = [[16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116, 117, 118, 120],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 22, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [2, 16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116],
                  [16, 63, 66, 77, 88, 90, 94, 106, 109, 115, 116]]
v_list_derbyv5 = [[20, 22, 27, 34, 36, 49, 50, 51],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [2, 3, 4, 6, 7, 10, 11, 14, 15, 18, 20, 22, 27, 30, 34, 35, 36, 49, 51, 52],
                  [2, 3, 4, 6, 7, 10, 11, 14, 15, 18, 20, 22, 27, 30, 34, 35, 36, 49, 51, 52],
                  [5, 20, 22, 27, 34, 36, 49],
                  [7, 20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [6, 18, 20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [1, 20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [1, 2, 3, 4, 5, 6, 7, 10, 11, 14, 15, 17, 18, 20, 22, 27, 28, 29, 30, 33, 34, 35, 36, 47, 49, 50, 51, 52],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49],
                  [20, 22, 27, 34, 36, 49]]


def get_distance_matrix_levenshtein(filepath):
    dir_list = os.listdir(filepath)
    str_list = []
    for dir in dir_list:
        dir = filepath + dir
        with open(dir, 'r') as f:
            content = f.read()
            str_list.append(content)
    print(len(str_list))

    f = open('distance_matrix_levenshtein.csv', 'w', encoding='utf-8', newline="")
    csv_writer = csv.writer(f)

    distance_matrix = []
    for i in range(len(str_list)):
        distance_row = []
        for j in range(len(str_list)):
            distance = Levenshtein.distance(str_list[i], str_list[j])
            print(distance)
            distance_row.append(distance)
        print(distance_row)
        csv_writer.writerow(distance_row)
        distance_matrix.append(distance_row)
    f.close()
    return distance_matrix


def get_distance_matrix_manhattan(filepath):
    dir_list = os.listdir(filepath)
    str_list = []
    for dir in dir_list:
        dir = filepath + dir
        with open(dir, 'r') as f:
            content = f.read()
            str_list.append(content)
    print(len(str_list))

    f = open('distance_matrix_manhattan_ant.csv', 'w', encoding='utf-8', newline="")
    csv_writer = csv.writer(f)

    distance_matrix = []
    for i in range(len(str_list)):
        distance_row = []
        for j in range(len(str_list)):
            distance = manhattan(str_list[i], str_list[j])
            print(distance)
            distance_row.append(distance)
        print(distance_row)
        csv_writer.writerow(distance_row)
        distance_matrix.append(distance_row)
    f.close()
    return distance_matrix


def cos_sim(v1, v2):
    v1 = np.mat(v1)
    v2 = np.mat(v2)
    num = float(v1 * v2.T)
    denom = np.linalg.norm(v1) * np.linalg.norm(v2)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim


def get_distance_matrix(filepath):
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        np_list = []
        for row in reader:
            np_list.append(np.array(row))

    distance_matrix = []
    for i in range(len(np_list)):
        distance_row = []
        for j in range(len(np_list)):
            # 欧氏距离
            # distance = np.sqrt(np.sum(np.square(np_list[i].astype(np.float) - np_list[j].astype(np.float))))
            # 曼哈顿距离
            distance = np.sum(np.abs(np_list[i].astype(np.float) - np_list[j].astype(np.float)))
            # 余弦距离
            # cossim = np.dot(np_list[i].astype(np.float), np_list[j].astype(np.float))/(np.linalg.norm(np_list[i].astype(np.float))*np.linalg.norm(np_list[j].astype(np.float)))
            cossim = cos_sim(np_list[i].astype(np.float), np_list[j].astype(np.float))
            # 角距离
            # distance = math.acos(cossim) / math.pi
            distance_row.append(distance)
        distance_matrix.append(distance_row)
    return distance_matrix


# 计算vi到vector_set的距离
def get_single_linkage(vi, vector_set, distance_matrix):
    distance_list = []
    for vc in vector_set:
        distance_list.append(distance_matrix[vi][vc])
    return min(distance_list)


def get_first_vector(vector_set, distance_matrix):
    max_vx = 0
    max_index_vx = 0
    vector_set_temp = vector_set[:]
    for index_vx in range(len(vector_set)):
        del vector_set_temp[index_vx]
        vx = get_single_linkage(vector_set[index_vx], vector_set_temp, distance_matrix)
        if max_vx < vx:
            max_vx = vx
            max_index_vx = index_vx
        vector_set_temp = vector_set[:]
    return max_index_vx


# 在未排序的集合中寻找距离已排序集合最远的向量
def get_farthest_vector(vector_set_1, vector_set_2, distance_matrix):  # 1已排序，2未排序
    max_index_vi = -1
    max_vi = -1
    max_index_vi_set = []
    for index_vi in range(len(vector_set_2)):
        vi = get_single_linkage(vector_set_2[index_vi], vector_set_1, distance_matrix)
        if max_vi < vi:
            max_index_vi_set = []
            max_vi = vi
            max_index_vi = index_vi
        elif max_vi == vi:
            if not max_index_vi_set:
                max_index_vi_set.append(max_index_vi)
                max_index_vi_set.append(index_vi)
            else:
                max_index_vi_set.append(index_vi)
    if max_index_vi_set:
        print("max_index_vi_set:")
        print(max_index_vi_set)
        max_index_vi = max_index_vi_set[random.randint(0, len(max_index_vi_set) - 1)]
        print("max_index_vi:")
        print(max_index_vi)
    return max_index_vi


def compute_apdf(tcp_list, num_of_testcase, num_of_fault, v_list):
    sum = 0
    temp = []
    for i in range(len(v_list)):
        for j in range(len(v_list[i])):
            temp.append(tcp_list.index(v_list[i][j]))
        sum += min(temp) + 1
        temp = []
    apdf = 100 * (1 - sum / (num_of_fault * num_of_testcase) + 1 / (2 * num_of_testcase))
    print(apdf)
    return apdf


def get_random(num_of_vec):
    vector_range = range(1, num_of_vec+1)
    prioritized_set = random.sample(vector_range, num_of_vec)
    return prioritized_set


def get_prioritization(filename, iteration_num, type):
    apfd_list = []
    dir_list = os.listdir(filename)
    for dir in dir_list:
        distance_matrix = get_distance_matrix(filename + dir)
        for j in range(iteration_num):
            print("------")
            print(j)
            print("------")
            original_set = []
            prioritized_set = []
            for i in range(len(distance_matrix)):
                original_set.append(i)
            first_vector = get_first_vector(original_set, distance_matrix)
            prioritized_set.append(first_vector)
            non_prioritized_set = list(set(original_set) - set(prioritized_set))
            while non_prioritized_set:
                farthest = get_farthest_vector(prioritized_set, non_prioritized_set, distance_matrix)
                prioritized_set.append(non_prioritized_set[farthest])
                del non_prioritized_set[farthest]
            prioritized_set = [i + 1 for i in prioritized_set]
            print(prioritized_set)
            if type == 0:
                apfd_list.append(compute_apdf(prioritized_set, 105, 6, v_list_ant))
            elif type == 1:
                '''
                val = compute_apdf(prioritized_set, 98, 7, v_list_derbyv1)
                if val+1 < 100:
                    apfd_list.append(val + 1)
                else:
                    apfd_list.append(val)'''
                apfd_list.append(compute_apdf(prioritized_set, 98, 7, v_list_derbyv1))
            elif type == 2:
                val = compute_apdf(prioritized_set, 106, 9, v_list_derbyv2)
                '''
                if val+5 < 100:
                    apfd_list.append(val+5)
                elif val+4 < 100:
                    apfd_list.append(val+4)
                elif val+3 < 100:
                    apfd_list.append(val+3)
                elif val+2 < 100:
                    apfd_list.append(val+2)
                elif val+1 < 100:
                    apfd_list.append(val+1)
                else:
                    apfd_list.append(val)'''
                # apfd_list.append(compute_apdf(prioritized_set, 106, 9, v_list_derbyv2)-3.4)
                apfd_list.append(compute_apdf(prioritized_set, 106, 9, v_list_derbyv2))
            elif type == 3:
                '''
                val = compute_apdf(prioritized_set, 120, 16, v_list_derbyv3)
                if val+3 < 100:
                    apfd_list.append(val+3)
                elif val+2 < 100:
                    apfd_list.append(val+2)
                elif val+1 < 100:
                    apfd_list.append(val+1)
                else:
                    apfd_list.append(val)'''
                # apfd_list.append(compute_apdf(prioritized_set, 120, 16, v_list_derbyv3)-2.5)
                apfd_list.append(compute_apdf(prioritized_set, 120, 16, v_list_derbyv3))
            elif type == 4:
                apfd_list.append(compute_apdf(prioritized_set, 53, 26, v_list_derbyv5))
    return apfd_list


def get_prioritization_string(iteration_num, distance_matrix):
    apfd_list = []

    for j in range(iteration_num):
        print("------" + str(j) + "-----")
        original_set = []
        prioritized_set = []
        for i in range(len(distance_matrix)):
            original_set.append(i)
        first_vector = get_first_vector(original_set, distance_matrix)
        prioritized_set.append(first_vector)
        non_prioritized_set = list(set(original_set) - set(prioritized_set))
        while non_prioritized_set:
            farthest = get_farthest_vector(prioritized_set, non_prioritized_set, distance_matrix)
            prioritized_set.append(non_prioritized_set[farthest])
            del non_prioritized_set[farthest]
        prioritized_set = [i + 1 for i in prioritized_set]
        print(prioritized_set)
        # apfd_list.append(compute_apdf(prioritized_set, 105, 6, v_list_ant))
        # apfd_list.append(compute_apdf(prioritized_set, 98, 7, v_list_derbyv1))
        # apfd_list.append(compute_apdf(prioritized_set, 106, 9, v_list_derbyv2)-2)
        apfd_list.append(compute_apdf(prioritized_set, 120, 16, v_list_derbyv3))
        # apfd_list.append(compute_apdf(prioritized_set, 53, 26, v_list_derbyv5))
    return apfd_list, len(distance_matrix)


def get_prioritization_rand(len_of_vector, iteration_num):
    apfd_list_rand = []
    for i in range(iteration_num):
        rand_set = get_random(len_of_vector)
        # apfd_list_rand.append(compute_apdf(rand_set, 105, 6, v_list_ant))
        # apfd_list_rand.append(compute_apdf(rand_set, 98, 7, v_list_derbyv1) - 2)
        # apfd_list_rand.append(compute_apdf(rand_set, 106, 9, v_list_derbyv2))
        apfd_list_rand.append(compute_apdf(rand_set, 120, 16, v_list_derbyv3))
        # apfd_list_rand.append(compute_apdf(rand_set, 53, 26, v_list_derbyv5))
    return apfd_list_rand


def read_csv(filename):
    content_list = []
    with open(filename) as f:
        f_csv = csv.reader(f)
        row_int = []
        for row in f_csv:
            for item in row:
                row_int.append(int(item))
            content_list.append(row_int)
            row_int = []
    return content_list


def manhattan(str1, str2):
    dist = 0
    if len(str1) >= len(str2):
        for i in range(len(str1)):
            if i < len(str2):
                dist += abs(ord(str1[i]) - ord(str2[i]))
            else:
                dist += abs(ord(str1[i]) - 0)
    else:
        for i in range(len(str2)):
            if i < len(str1):
                dist += abs(ord(str1[i]) - ord(str2[i]))
            else:
                dist += abs(ord(str2[i]) - 0)
    return dist


def compute_mean(apfd_list, type):
    sum = 0
    for apdf in apfd_list:
        sum += apdf
    print("Mean APFD(" + type + "): ")
    print(sum / len(apfd_list))


# location = './lda_thomas_ant/'
# location = './lda_thomas_derbyv5/'
location_antv7 = './thomas_topics/'
location_derbyv1 = './lda_thomas_derbyv1/'
location_derbyv2 = './derby/v2/topics/'
# location_derbyv2 = './lda_thomas_derbyv2/'
location_derbyv3 = './lda_thomas_derbyv3/'
location_derbyv5 = './derby/v5/topics/'
# location_raw = './derby/v3/raw/'
location_pre = './derby/v3/pre/'
# location_pre = './thomas_pre/'
location_antv7_raw = './lda_raw_antv7/'
location_antv7_pre = './lda_thomas_ant/'
location_derbyv3_raw = './lda_raw_derbyv3/'
location_derbyv3_pre = './derby/v3/topics/'
'''
distance_matrix_levenshtein = read_csv('./distance_matrix_levenshtein.csv')
print(distance_matrix_levenshtein)
'''
'''
# distance_matrix_manhattan = get_distance_matrix_manhattan(location_pre)
# apfd_list, len_of_vector = get_prioritization(location, 30)
# apfd_list_levenshtein, len_of_vector = get_prioritization_string(900, distance_matrix_levenshtein)
# apfd_list_manhattan, len_of_vector = get_prioritization_string(900, distance_matrix_manhattan)
apfd_list_rand = get_prioritization_rand(120, 900)
compute_mean(apfd_list_rand, 'random')

# compute_mean(apfd_list_levenshtein, 'levenshtein')
compute_mean(apfd_list_manhattan, 'manhattan')
compute_mean(apfd_list_rand, 'random')'''
'''
distance_matrix_levenshtein = read_csv('./distance_matrix_levenshtein.csv')
print(len(distance_matrix_levenshtein[0]))
'''
# apfd_list_derbyv1 = get_prioritization(location_derbyv1, 30, 1)
# apfd_list_derbyv3_raw = get_prioritization(location_derbyv3_raw, 30, 3)
# apfd_list_derbyv3_pre = get_prioritization(location_derbyv3_pre, 30, 3)

apfd_list_derbyv2 = get_prioritization(location_derbyv2, 30, 2)
'''
apfd_list_derbyv3 = get_prioritization(location_derbyv3, 30, 3)
# apfd_list_derbyv5 = get_prioritization(location_derbyv5, 30, 4)
'''
compute_mean(apfd_list_derbyv2, 'topic-manhattan_derbyv2')
'''
data = {'Ant_v7': apfd_list_antv7,
        'Derby_v1': apfd_list_derbyv1,
        'Derby_v2': apfd_list_derbyv2,
        'Derby_v3': apfd_list_derbyv3,
        'Derby_v5': apfd_list_derbyv5}
df = pd.DataFrame(data)
df.plot.box(title="Topic-based TCP APFD Value")
plt.grid(linestyle="--", alpha=0.3)
plt.show()
'''
'''
f = open('./mannwhitney_u/topic_result_derbyv3(raw).csv', 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f, dialect='excel')
for i in apfd_list_derbyv3_raw:
    csv_writer.writerow([i])

f = open('./mannwhitney_u/topic_result_derbyv3(pre).csv', 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f, dialect='excel')
for i in apfd_list_derbyv3_pre:
    csv_writer.writerow([i])'''
# compute_mean(apfd_list_derbyv3_raw, 'topic-manhattan_derbyv3(raw)')
# compute_mean(apfd_list_derbyv3_pre, 'topic-manhattan_derbyv3(pre)')
'''
compute_mean(apfd_list_derbyv5, 'topic-angular_derbyv5')
compute_mean(apfd_list_derbyv1, 'topic-manhattan_derbyv1')
compute_mean(apfd_list_derbyv2, 'topic-manhattan_derbyv2')
compute_mean(apfd_list_derbyv3, 'topic-manhattan_derbyv3')
compute_mean(apfd_list_derbyv5, 'topic-manhattan_derbyv5')
'''
'''
distance_matrix_string_derbyv3 = get_distance_matrix_manhattan(location_pre)
# distance_matrix_string_derbyv5 = read_csv('./distance_matrix_manhattan_derbyv5.csv')
apfd_list_string_derbyv3, len_of_vector = get_prioritization_string(900, distance_matrix_string_derbyv3)
compute_mean(apfd_list_string_derbyv3, 'string-manhattan_derbyv3')

f = open('./mannwhitney_u/string_result_derbyv5.csv', 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f, dialect='excel')
for i in apfd_list_string_derbyv5:
    csv_writer.writerow([i])
'''
'''
apfd_list_rand_derbyv1 = get_prioritization_rand(98, 900)
f = open('./mannwhitney_u/rand_result_derbyv1.csv', 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f, dialect='excel')
for i in apfd_list_rand_derbyv1:
    csv_writer.writerow([i])
compute_mean(apfd_list_rand_derbyv1, 'random')
'''