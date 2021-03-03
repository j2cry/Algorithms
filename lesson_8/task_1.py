# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

from random import randint

# generate nodes count
nodes = randint(2, 15)

# generate graph: each friend shook hands with the other, but not with himself
friends = {node: [n for n in range(nodes) if node != n] for node in range(nodes)}
print(f'Total friends: {len(friends)}')

# поскольку рукопожатие - двусторонний процесс, значит граф неориентированный и матрица смежности симметрична
interactions_count = sum([len(n) for n in friends.values()]) / 2
print(f'Interactions: {interactions_count}')


# а вот если они начали друг в друга метать снежки, и кто-то в кого-то попал, а кто-то нет, то:
# generate graph
friends = {node: [n for n in range(randint(0, nodes - 1)) if node != n] for node in range(nodes)}

interactions_count = 0
for hits in friends.values():
    interactions_count += len(hits)

print(friends)
print(f'Snowball interactions: {interactions_count}')
