# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

from materials import Graph
from operator import itemgetter

g = [   # граф из урока про алгоритм Дейкстры
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]
if __name__ == '__main__':
    text = itemgetter(2)
    graph = Graph(7, matrix=g)
    # graph = Graph(7, directed=True)
    start = 7
    print(text(graph.find_paths_from(start)))
    # print(graph.breadth_first_search(1, 7))
