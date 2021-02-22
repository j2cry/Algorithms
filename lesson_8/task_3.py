# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
from materials import Graph

if __name__ == '__main__':
    start, finish = 2, 5
    graph = Graph(10, directed=True)
    print(graph)
    print(graph.first_search(start, finish))
    print(graph.first_search(start, finish, depth_search=True))
