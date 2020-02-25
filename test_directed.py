__autor__ = "Max Begue"
__date__ = "19/02/2020"
__file_name__ = "tetst.py"

from source.directed_graph import Directgraph


print("on passe au vrai test mainteneant")


graph = Directgraph()
graph.add_vertex(1)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 1, 1)
graph.add_edge(2, 3, 1)

print(graph.verticies)
print(len(graph))
print(graph[2])
print(graph)

for vertex in graph:
    print(vertex)


graph.remove_edge(1, 2)
print(graph)