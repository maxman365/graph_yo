__autor__ = "Max Begue"
__date__ = "25/02/2020"
__file_name__ = "test_dijkstra.py"

from source.directed_graph import Directgraph
graph = Directgraph()
graph.add_vertex(1)
graph.add_edge(1, 2, 4)
graph.add_edge(2, 1, 1)
graph.add_edge(2, 3, 1)
graph.add_edge(2, 4, 4)
graph.add_edge(3, 4, 1)

print(graph.dijkstra_base(2))

print(graph.dijkstra_binary_heap(2))

print("chemin de 2 à 4 = ", graph.dijkstra_binary_heap_one_track(2, 4))