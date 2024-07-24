import networkx as nx

G = nx.Graph()

stations = ["Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska", 
            "Shuliavska", "Politekhnichnyi Instytut", "Vokzalna", "Universytet", "Teatralna", 
            "Khreshchatyk", "Arsenalna", "Dnipro", "Hidropark", "Livoberezhna", 
            "Darnytsia", "Chernihivska", "Lisova",
            "Heroiv Dnipra", "Minska", "Obolon", "Pochaina", "Tarasa Shevchenka", 
            "Kontraktova Ploshcha", "Poshtova Ploshcha", "Maidan Nezalezhnosti", "Ploshcha Lva Tolstoho", 
            "Olimpiiska", "Palats Ukraina", "Lybidska", "Demiyivska", "Holosiivska", 
            "Vasylkivska", "Vystavkovyi Tsentr", "Ipodrom", "Teremky",
            "Syrets", "Dorohozhychi", "Lukianivska", "Zoloti Vorota", "Palats Sportu", 
            "Klovska", "Pecherska", "Druzhby Narodiv", "Vydubychi", 
            "Slavutych", "Osokorky", "Pozniaky", "Kharkivska", "Vyrlytsia", 
            "Boryspilska", "Chervony Khutir"]
G.add_nodes_from(stations)


routes = [
    # Червона лінія
    ("Akademmistechko", "Zhytomyrska"), ("Zhytomyrska", "Sviatoshyn"), ("Sviatoshyn", "Nyvky"),
    ("Nyvky", "Beresteiska"), ("Beresteiska", "Shuliavska"), ("Shuliavska", "Politekhnichnyi Instytut"),
    ("Politekhnichnyi Instytut", "Vokzalna"), ("Vokzalna", "Universytet"), ("Universytet", "Teatralna"),
    ("Teatralna", "Khreshchatyk"), ("Khreshchatyk", "Arsenalna"), ("Arsenalna", "Dnipro"),
    ("Dnipro", "Hidropark"), ("Hidropark", "Livoberezhna"), ("Livoberezhna", "Darnytsia"),
    ("Darnytsia", "Chernihivska"), ("Chernihivska", "Lisova"),
    
    # Синя лінія
    ("Heroiv Dnipra", "Minska"), ("Minska", "Obolon"), ("Obolon", "Pochaina"),
    ("Pochaina", "Tarasa Shevchenka"), ("Tarasa Shevchenka", "Kontraktova Ploshcha"),
    ("Kontraktova Ploshcha", "Poshtova Ploshcha"), ("Poshtova Ploshcha", "Maidan Nezalezhnosti"),
    ("Maidan Nezalezhnosti", "Ploshcha Lva Tolstoho"), ("Ploshcha Lva Tolstoho", "Olimpiiska"),
    ("Olimpiiska", "Palats Ukraina"), ("Palats Ukraina", "Lybidska"), ("Lybidska", "Demiyivska"),
    ("Demiyivska", "Holosiivska"), ("Holosiivska", "Vasylkivska"), ("Vasylkivska", "Vystavkovyi Tsentr"),
    ("Vystavkovyi Tsentr", "Ipodrom"), ("Ipodrom", "Teremky"),
    
    # Зелена лінія
    ("Syrets", "Dorohozhychi"), ("Dorohozhychi", "Lukianivska"), ("Lukianivska", "Zoloti Vorota"),
    ("Zoloti Vorota", "Palats Sportu"), ("Palats Sportu", "Klovska"), ("Klovska", "Pecherska"),
    ("Pecherska", "Druzhby Narodiv"), ("Druzhby Narodiv", "Vydubychi"), ("Vydubychi", "Slavutych"),
    ("Slavutych", "Osokorky"), ("Osokorky", "Pozniaky"), ("Pozniaky", "Kharkivska"),
    ("Kharkivska", "Vyrlytsia"), ("Vyrlytsia", "Boryspilska"), ("Boryspilska", "Chervony Khutir"),
    
    # Пересадкові станції
    ("Teatralna", "Zoloti Vorota"), ("Khreshchatyk", "Maidan Nezalezhnosti"),
    ("Ploshcha Lva Tolstoho", "Palats Sportu")
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


dfs_result = dfs_path(G, "Akademmistechko", "Teremky")
bfs_result = bfs_path(G, "Akademmistechko", "Teremky")

print(f'dfs: {dfs_result} \n' 
      f'bfs: {bfs_result}')
