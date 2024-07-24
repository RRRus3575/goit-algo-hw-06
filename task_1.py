import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = [f"Station {i}" for i in range(1, 18)]
G.add_nodes_from(stations)


routes = [
    ("Station 1", "Station 2"),
    ("Station 1", "Station 3"),
    ("Station 2", "Station 4"),
    ("Station 3", "Station 5"),
    ("Station 4", "Station 6"),
    ("Station 5", "Station 7"),
    ("Station 6", "Station 8"),
    ("Station 7", "Station 9"),
    ("Station 8", "Station 10"),
    ("Station 9", "Station 11"),
    ("Station 10", "Station 12"),
    ("Station 11", "Station 13"),
    ("Station 12", "Station 14"),
    ("Station 13", "Station 15"),
    ("Station 14", "Station 16"),
    ("Station 15", "Station 17"),
    ("Station 3", "Station 6"),  
    ("Station 5", "Station 8"),
    ("Station 7", "Station 10"),
    ("Station 9", "Station 12"),
    ("Station 11", "Station 14")
]
G.add_edges_from(routes)


plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("Транспортна мережа міста")
plt.show()


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())

print(f'Аналіз основних характеристик:\n'
      f'Кількість вершин (станцій): {num_nodes}\n'
      f'Кількість ребер (маршрутів): {num_edges}\n'
      f'Ступінь вершин (кількість сполучень для кожної станції): {degree}')
