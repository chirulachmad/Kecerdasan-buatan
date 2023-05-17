from matplotlib import animation
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
from queue import PriorityQueue

def ucs_animation(graph, start_node, positions):
    limit_galoon = 20
    galoon_cost_tracker = 0
    print(galoon_cost_tracker)
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_node))  # Masukkan node awal ke antrian dengan biaya 0

    fig, ax = plt.subplots()
    G = nx.Graph(graph)

    pos = positions  # Use the provided positions for the nodes

    def update(frame):
        nonlocal galoon_cost_tracker 
        if not queue.empty():
            cost, current_node = queue.get()

            # Cek apakah node sudah dikunjungi sebelumnya
            if current_node in visited:
                return

            # Periksa apakah semua node telah dikunjungi
            if len(visited) == len(graph):
                ani.event_source.stop()
                print("Urutan node yang dikunjungi:")
                print(" -> ".join(visited))
                return

            visited.add(current_node)

            # Periksa tetangga-tetangga yang belum dikunjungi
            for neighbor, neighbor_cost in graph[current_node].items():
                if neighbor not in visited and neighbor[0] != "D":
                    new_cost = cost + neighbor_cost
                    queue.put((new_cost, neighbor))
                    # galoon_cost_tracker = galoon_cost_tracker + galoon_cost[]
                    node_string = neighbor.split(" ")
                    print(f"Mengunjungi {node_string[0]}: Cost -> {neighbor_cost} : Galon yang dibeli -> {neighbor[-2]}")
                    if(galoon_cost_tracker + int(neighbor[-2]) > limit_galoon):
                        print("GALON HABIS")
                        galoon_cost_tracker = 0
                    galoon_cost_tracker = galoon_cost_tracker + int(neighbor[-2])
                    

        # Update node colors
        node_colors = [
            "purple" if node in visited else "darkolivegreen" for node in G.nodes()
        ]
        nx.draw(G, pos=pos, with_labels=True, node_color=node_colors, ax=ax, node_size=900, font_size=10, font_color="white")

    ani = FuncAnimation(
        fig, update, frames=range(len(graph) + 1), interval=1500, repeat=False
    )

    plt.show()


galoon_cost = {
    2: 1,
    3: 7,
    4: 9,
    5: 2,
    6: 4,
    7: 9,
    8: 9,
    9: 3,
    10: 2,
    11: 4,
    12: 6,
    13: 8,
}


# Representasi graf
graph = {
    "D1": {f"3 ({galoon_cost[3]})": 4},
    "D4": {f"5 ({galoon_cost[5]})": 7, f"4 ({galoon_cost[4]})": 8},
    f"3 ({galoon_cost[3]})": {f"6 ({galoon_cost[6]})": 6, f"9 ({galoon_cost[9]})": 2, f"5 ({galoon_cost[5]})": 5},
    f"4 ({galoon_cost[4]})": {f"5 ({galoon_cost[5]})": 3, f"7 ({galoon_cost[7]})": 9},
    f"5 ({galoon_cost[5]})": {f"7 ({galoon_cost[7]})": 16, f"4 ({galoon_cost[4]})": 3},
    f"6 ({galoon_cost[6]})": {"D2": 14, f"9 ({galoon_cost[9]})": 1},
    f"7 ({galoon_cost[7]})": {f"8 ({galoon_cost[8]})": 10, f"11 ({galoon_cost[11]})": 11},
    f"8 ({galoon_cost[8]})": {f"9 ({galoon_cost[9]})": 14},
    f"9 ({galoon_cost[9]})": {f"8 ({galoon_cost[8]})": 14, f"12 ({galoon_cost[12]})": 13},
    "D2": {f"6 ({galoon_cost[6]})": 14},
    f"11 ({galoon_cost[11]})": {f"12 ({galoon_cost[12]})": 12},
    f"12 ({galoon_cost[12]})": {f"9 ({galoon_cost[9]})": 13, "D3": 15},
    "D3": {f"12 ({galoon_cost[12]})": 15},
}

start_node = "D1"

positions = {
    "D1": (0, 2),
    "D4": (-2, 1),
    f"3 ({galoon_cost[3]})": (1, 2),
    f"4 ({galoon_cost[4]})": (-2, 0),
    f"5 ({galoon_cost[5]})": (0, 0),
    f"6 ({galoon_cost[6]})": (2, 0),
    f"7 ({galoon_cost[7]})": (-2, -1),
    f"8 ({galoon_cost[8]})": (0, -1),
    f"9 ({galoon_cost[9]})": (1, -1),
    "D2": (2, -1),
    f"11 ({galoon_cost[11]})": (-1, -2),
    f"12 ({galoon_cost[12]})": (0, -2),
    "D3": (1, -2),
}

ucs_animation(graph, start_node, positions)