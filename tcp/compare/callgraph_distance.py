

def get_distance(path_t1, path_t2):  # 计算t1->t2的距离
    methods_t1 = open(path_t1, 'r').readlines()
    methods_t2 = open(path_t2, 'r').readlines()
    rel = list(set(methods_t1).difference(set(methods_t2)))
    return len(rel)


path_t1 = './testcases/000001.java'
path_t2 = './testcases/000002.java'
path_t3 = './testcases/000295.java'
path_t4 = './testcases/000296.java'

print(get_distance(path_t1, path_t2))
print(get_distance(path_t1, path_t3))
print(get_distance(path_t1, path_t4))

print(get_distance(path_t2, path_t1))
print(get_distance(path_t2, path_t3))
print(get_distance(path_t2, path_t4))

print(get_distance(path_t3, path_t1))
print(get_distance(path_t3, path_t2))
print(get_distance(path_t3, path_t4))

print(get_distance(path_t4, path_t1))
print(get_distance(path_t4, path_t2))
print(get_distance(path_t4, path_t3))
