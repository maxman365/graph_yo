__autor__ = "Max Begue"
__date__ = "25/02/2020"
__file_name__ = "test_undirected.py"



from source.undirected_graph import Undirecetd_graph


print("on passe au vrai test mainteneant")


graph = Undirecetd_graph()
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

graph.modify_weight(2, 3, 0)
print(graph)