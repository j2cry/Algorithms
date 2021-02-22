from collections import namedtuple, deque
from random import randint, uniform, choice
from operator import itemgetter


class Graph:
    """ Это не полноценный рабочий класс, а только первое приближение на скорую руку -
        что-то может не работать или работать не так, как задумано """
    EdgeInfo = namedtuple('EdgeInfo', 'node, weight')       # не помню зачем я его ввел, пусть будет пока

    def __init__(self, nodes: int = 10, matrix: list[list] = None, directed=False, allow_cycles=False):
        self.nodes = nodes
        self.__allow_cycles = allow_cycles
        self.__max_edges = self.nodes ** 2
        self.__edges = 0        # кол-во активных ребер
        self.directed = directed

        self.__matrix = [[]]     # список смежностей
        if matrix:
            self.__matrix = matrix
            self.nodes = len(matrix)
        else:
            self.generate()

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, nodes):
        self.__nodes = nodes
        # self.generate()

    def set_edge(self, node_a: int, node_b: int, weight=1., back_weight=1., add_reverse=True):
        """ Создает/изменяет ребро из вершины a в вершину b с весом weight
            и если add_reverse=True - обратное ребро с весом back_weight """
        # Если граф ориентированный
        self.__matrix[node_a][node_b] = weight       # добавляем ребро из a в b

        # если это не кольцевое ребро, граф неориентированный и не сказано добавить обратное ребро
        if node_a != node_b and (not self.directed or add_reverse):
            self.__matrix[node_b][node_a] = back_weight if back_weight else weight      # добавляем ребро из b в a

    def generate(self, weights_range: (float, float) = None):
        """ Генерирует неизолированный (не)ориентированный граф """
        self.__matrix = [[0 for _ in range(self.nodes)] for _ in range(self.nodes)]
        self.__edges = 0

        # связываем все узлы хотя бы одной связью
        nodes_list = list(range(self.nodes))
        current_node = choice(nodes_list)
        nodes_list.remove(current_node)
        while nodes_list:
            next_node = choice(nodes_list)
            nodes_list.remove(next_node)
            self.set_edge(current_node, next_node)
            current_node = next_node
            self.__edges += 1

        # добавляем еще рандомных связей
        # создаем список пока еще не существующих ребер
        AvailableEdges = namedtuple('AvailableEdges', 'node_a, node_b')
        edges_list = []
        for node_a in range(self.nodes):
            for node_b in range(self.nodes):
                if not self.__allow_cycles and node_a == node_b:       # исключаем кольцевые ребра, если надо
                    continue
                if self.__matrix[node_a][node_b] != 0:      # если ребро уже существует, идем дальше
                    continue

                edges_list.append(AvailableEdges(node_a, node_b))

        add_edges = randint(0, len(edges_list))     # кол-во добавляемых ребер
        for _ in range(add_edges):
            edge = choice(edges_list)
            if weights_range:
                self.set_edge(edge.node_a, edge.node_b, weight=uniform(*weights_range), add_reverse=not self.directed,
                              back_weight=uniform(*weights_range))
            else:
                self.set_edge(edge.node_a, edge.node_b, add_reverse=not self.directed)

    def get_node(self, index):
        return self.__matrix[index]

    def get_matrix(self):
        return self.__matrix.copy()

    def as_str(self, rnd=1):
        matrix = ''
        for index, node in enumerate(self.__matrix):
            matrix += f'{index:02d} {[f"{round(float(weight), rnd):>{rnd + 2}}" for weight in node]}\n'
        return matrix

    def __str__(self):
        return self.as_str()

    def __getitem__(self, item):
        return self.get_node(item)

    def __len__(self):
        return self.nodes

    def find_paths_from(self, current):
        """ доработанный Алгоритм Дейкстры из урока """
        start = current
        visited = set()
        weights = [float('inf')] * self.nodes
        weights[current] = .0
        parent = [None for _ in range(self.nodes)]
        min_cost = 0
        while min_cost < float('inf'):
            visited.add(current)
            for node, weight in enumerate(self.get_node(current)):
                if weight and node not in visited:
                    if weights[node] > weight + weights[current]:
                        weights[node] = weight + weights[current]
                        parent[node] = current

            min_cost = float('inf')
            for node in range(self.nodes):
                if min_cost > weights[node] and node not in visited:
                    min_cost = weights[node]
                    current = node

        ways = []
        as_text = ''
        for node in range(self.nodes):
            ways.append(self.__get_way(parent, node))
            as_text += f'Way to node {node} from {start}: {ways[node]} costs {weights[node]}\n'
        return ways, weights, as_text

    @staticmethod
    def __get_way(parents, finish):
        # возвращает маршрут
        way = [finish]
        while parents[finish] is not None:
            way.append(parents[finish])
            finish = parents[finish]
        way.reverse()
        return way

    def __get_way_weight(self, parents, finish):
        # возвращает стоимость маршрута
        weight = 0
        while parents[finish] is not None:
            weight += self.get_node(parents[finish])[finish]
            finish = parents[finish]
        return weight

    def breadth_first_search(self, start, finish):
        """ Поиск кратчайшего пути из А в Б """
        deq = deque([start])
        visited = {start, }
        parent = [None for _ in range(self.nodes)]
        while len(deq) > 0:
            current = deq.pop()
            if current == finish:
                break
            # ищем все пути из текущей вершины и ставим в конец очереди, если они не были просмотрены
            for _node, _weight in enumerate(self.get_node(current)):
                if _weight and _node not in visited:
                    visited.add(_node)
                    deq.appendleft(_node)
                    parent[_node] = current
        else:
            return None
        return self.__get_way(parent, finish), self.__get_way_weight(parent, finish)

    def depth_first_search(self, start, finish):
        deq = deque([start])
        visited = {start, }
        parent = [None for _ in range(self.nodes)]
        while len(deq) > 0:
            current = deq.pop()
            if current == finish:
                break
            # ищем все пути из текущей вершины и приоритетно ставим в очередь, если они не были просмотрены
            for _node, _weight in enumerate(self.get_node(current)):
                if _weight and _node not in visited:
                    visited.add(_node)
                    deq.append(_node)
                    parent[_node] = current
        else:
            return None
        return self.__get_way(parent, finish), self.__get_way_weight(parent, finish)


if __name__ == '__main__':
    text = itemgetter(2)
    st, fn = 1, 5
    g = [  # граф из урока про поиск в ширину
        [0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0]
    ]
    graph = Graph(matrix=g)
    print(text(graph.find_paths_from(st)))
