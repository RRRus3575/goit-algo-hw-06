import networkx as nx

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


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))
    return None


def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None


dfs_result = dfs_path(G, "Station 1", "Station 17")
bfs_result = bfs_path(G, "Station 1", "Station 17")

print(f'dfs: {dfs_result}, bfs: {bfs_result}')
