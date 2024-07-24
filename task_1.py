import networkx as nx
import matplotlib.pyplot as plt

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

# Додавання ребер (з'єднань між станціями)
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


plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, k=0.1)
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=8, font_weight="bold", edge_color="gray")
plt.title("Метро Києва")
plt.show()


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())

print(f'Аналіз основних характеристик:\n'
      f'Кількість вершин (станцій): {num_nodes}\n'
      f'Кількість ребер (маршрутів): {num_edges}\n'
      f'Ступінь вершин (кількість сполучень для кожної станції): {degree}')
