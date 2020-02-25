__autor__ = "Max Begue"
__date__ = "25/02/2020"
__file_name__ = "undirected_graph.py"

from source.graph import Directgraph

class Undirecetd_graph(Directgraph):

    def __init__(self):
        super().__init__()

    def add_edge(self, vertex1, vertex2, weight):
        """ adds an edge in the graph. Modifies the graph"""

        assert weight >= 0

        if vertex1 not in self.edges:
            self.add_vertex(vertex1)

        if vertex2 not in self.edges:
            self.add_vertex(vertex2)

        self.edges[vertex1][vertex2] = weight
        self.edges[vertex2][vertex1] = weight

    def remove_edge(self, vertex1, vertex2):
        """ removes an edge in the graph. Modifies the graph"""

        if vertex1 in self.edges:
            if vertex2 in self.edges[vertex1]:
                del self.edges[vertex1][vertex2]
                del self.edges[vertex2][vertex1]

    def modify_weight(self, vertex1, vertex2, weight):
        """changes the weight of an edge. Modifies the graph"""
        assert weight >= 0

        if vertex1 in self.edges:
            if vertex2 in self.edges[vertex1]:
                self.edges[vertex1][vertex2] = weight
                self.edges[vertex2][vertex1] = weight

