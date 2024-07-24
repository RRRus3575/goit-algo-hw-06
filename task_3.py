import networkx as nx
import pprint


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
    # red
    ("Akademmistechko", "Zhytomyrska", 1.2), ("Zhytomyrska", "Sviatoshyn", 1.0), ("Sviatoshyn", "Nyvky", 1.1),
    ("Nyvky", "Beresteiska", 1.5), ("Beresteiska", "Shuliavska", 1.4), ("Shuliavska", "Politekhnichnyi Instytut", 1.2),
    ("Politekhnichnyi Instytut", "Vokzalna", 1.5), ("Vokzalna", "Universytet", 1.0), ("Universytet", "Teatralna", 0.7),
    ("Teatralna", "Khreshchatyk", 0.5), ("Khreshchatyk", "Arsenalna", 1.2), ("Arsenalna", "Dnipro", 0.8),
    ("Dnipro", "Hidropark", 1.5), ("Hidropark", "Livoberezhna", 2.0), ("Livoberezhna", "Darnytsia", 1.2),
    ("Darnytsia", "Chernihivska", 1.7), ("Chernihivska", "Lisova", 1.5),
    
    # blue
    ("Heroiv Dnipra", "Minska", 1.0), ("Minska", "Obolon", 1.2), ("Obolon", "Pochaina", 1.5),
    ("Pochaina", "Tarasa Shevchenka", 1.8), ("Tarasa Shevchenka", "Kontraktova Ploshcha", 1.0),
    ("Kontraktova Ploshcha", "Poshtova Ploshcha", 0.9), ("Poshtova Ploshcha", "Maidan Nezalezhnosti", 0.8),
    ("Maidan Nezalezhnosti", "Ploshcha Lva Tolstoho", 0.5), ("Ploshcha Lva Tolstoho", "Olimpiiska", 0.6),
    ("Olimpiiska", "Palats Ukraina", 1.0), ("Palats Ukraina", "Lybidska", 1.2), ("Lybidska", "Demiyivska", 1.5),
    ("Demiyivska", "Holosiivska", 1.3), ("Holosiivska", "Vasylkivska", 1.0), ("Vasylkivska", "Vystavkovyi Tsentr", 1.2),
    ("Vystavkovyi Tsentr", "Ipodrom", 1.4), ("Ipodrom", "Teremky", 1.1),
    
    # green
    ("Syrets", "Dorohozhychi", 1.6), ("Dorohozhychi", "Lukianivska", 1.2), ("Lukianivska", "Zoloti Vorota", 1.8),
    ("Zoloti Vorota", "Palats Sportu", 0.6), ("Palats Sportu", "Klovska", 1.0), ("Klovska", "Pecherska", 1.1),
    ("Pecherska", "Druzhby Narodiv", 1.3), ("Druzhby Narodiv", "Vydubychi", 1.5), ("Vydubychi", "Slavutych", 1.7),
    ("Slavutych", "Osokorky", 1.5), ("Osokorky", "Pozniaky", 1.2), ("Pozniaky", "Kharkivska", 1.4),
    ("Kharkivska", "Vyrlytsia", 1.8), ("Vyrlytsia", "Boryspilska", 1.5), ("Boryspilska", "Chervony Khutir", 1.7),
    
    # transfer
    ("Teatralna", "Zoloti Vorota", 0.1), ("Khreshchatyk", "Maidan Nezalezhnosti", 0.1),
    ("Ploshcha Lva Tolstoho", "Palats Sportu", 0.1)
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
