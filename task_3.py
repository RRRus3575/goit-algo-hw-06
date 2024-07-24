import networkx as nx
import pprint


G = nx.Graph()
stations = [f"Station {i}" for i in range(1, 18)]
G.add_nodes_from(stations)


routes = [
    ("Station 1", "Station 2", 5),
    ("Station 1", "Station 3", 3),
    ("Station 2", "Station 4", 2),
    ("Station 3", "Station 5", 7),
    ("Station 4", "Station 6", 1),
    ("Station 5", "Station 7", 4),
    ("Station 6", "Station 8", 3),
    ("Station 7", "Station 9", 2),
    ("Station 8", "Station 10", 6),
    ("Station 9", "Station 11", 1),
    ("Station 10", "Station 12", 5),
    ("Station 11", "Station 13", 2),
    ("Station 12", "Station 14", 4),
    ("Station 13", "Station 15", 7),
    ("Station 14", "Station 16", 3),
    ("Station 15", "Station 17", 1)
]
G.add_weighted_edges_from(routes)

def dijkstra_all_paths(graph):
    paths = {}
    for node in graph.nodes:
        paths[node] = {}
        for target in graph.nodes:
            if node != target:
                try:
                    path = nx.dijkstra_path(graph, node, target)
                    weight = nx.dijkstra_path_length(graph, node, target)
                    paths[node][target] = (path, weight)
                except nx.NetworkXNoPath:
                    paths[node][target] = (None, float('inf'))
    return paths


all_shortest_paths = dijkstra_all_paths(G)


pprint.pprint(all_shortest_paths)
