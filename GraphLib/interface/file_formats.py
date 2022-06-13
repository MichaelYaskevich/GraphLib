graph_adjacency_list_file_format = '''
В первой строке указано количество вершин N
В каждой из следующих N строк указна запись для каждой вершины в формате:
i j weight(i, j) k weight(i, k) ... m weight(i, m)
где j, k, ..., m соседи узла i
В предпоследней строке узел являющийся началом пути
В последней строке узел являющийся концом пути или '-'
 если вы хотите увидеть пути от источника до всех вершин

Пример:
4
a b 25 c 4
b 0
c a 0 b 7
d 0
a
-'''

graph_weight_matrix_file_format = '''
В первой строке указано количество вершин N
В следующих N строках представлен граф как матрица весов,
    где '-' означает, что ребра не существует
В предпоследней строке узел являющийся началом пути
В последней строке узел являющийся концом пути

Пример:
4
0 1 0 1
1 0 2 5
1 3 0 -4
0 0 5 0
1
4
'''
