import Levenshtein
import os
import csv


def get_distance_matrix_levenshtein(filepath):
    dir_list = os.listdir(filepath)
    str_list = []
    for dir in dir_list:
        dir = filepath + dir
        with open(dir, 'r') as f:
            content = f.read()
            str_list.append(content)
    print(len(str_list))
    distance_matrix = []
    for i in range(len(str_list)):
        distance_row = []
        for j in range(len(str_list)):
            distance = Levenshtein.distance(str_list[i], str_list[j])
            print(distance)
            distance_row.append(distance)
        print(distance_row)
        distance_matrix.append(distance_row)
    print(distance_matrix)
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

    distance_matrix = []
    for i in range(len(str_list)):
        distance_row = []
        for j in range(len(str_list)):
            distance = manhattan(str_list[i], str_list[j])
            print(distance)
            distance_row.append(distance)
        print(distance_row)
        distance_matrix.append(distance_row)
    return distance_matrix


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


if __name__ == '__main__':
    location = './string_test/pre/'
    # distance_matrix_levenshtein = get_distance_matrix_levenshtein(location)
    distance_matrix_manhattan = get_distance_matrix_manhattan(location)
    print(distance_matrix_manhattan)
