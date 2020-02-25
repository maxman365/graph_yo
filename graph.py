__autor__ = "Max Begue"
__date__ = "19/02/2020"
__file_name__ = "graph.py"


import numpy as np

class Directgraph:

    def __init__(self):

        self.edges = {}

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, new_edges):
        assert type(new_edges) == dict
        self.__edges = new_edges

    @property
    def verticies(self):
        vert = []
        for i in self.edges:
            vert += [i]
        return vert

    def add_vertex(self, vertex):
        self.edges[vertex] = {}

    def remove_vertex(self, vertex):
        """ remove a vertex from the graph. Modify the graph"""

        if vertex in self.edges:
            del self.edges[vertex]
            for i in self.edges:
                if vertex in i:
                    del i[vertex]

    def add_edge(self, vertex1, vertex2, weight):

        """ adds an edge in the graph. Modifies the graph"""

        assert weight >= 0

        if vertex1 not in self.edges:
            self.add_vertex(vertex1)

        if vertex2 not in self.edges:
            self.add_vertex(vertex2)

        self.edges[vertex1][vertex2] = weight

    def remove_edge(self, vertex1, vertex2):

        """ removes an edge in the graph. Modifies the graph"""

        if vertex1 in self.edges:
            if vertex2 in self.edges[vertex1]:
                del self.edges[vertex1][vertex2]

    def modify_weight(self, vertex1, vertex2, weight):

        """changes the weight of an edge. Modifies the graph"""
        assert weight >= 0

        if vertex1 in self.edges:
            if vertex2 in self.edges[vertex1]:
                self.edges[vertex1][vertex2] = weight

    def zero(self):
        self.edges = {}

    def induced_under_graph(self, vertex_list):

        res = Directgraph()
        for i in vertex_list:
            if i in self.verticies:
                for j in self.edges[i]:
                    if j in vertex_list:
                        res.add_edge(i, j, self.edges[i][j])

    ### induced à retravailler car complexité dégueue

    def __len__(self):
        """ return tuple ( |V|, |E| )"""
        nb_edges = 0
        for i in self.edges:
            nb_edges += len(self.edges[i])

        return (len(self.verticies), nb_edges)

    def __getitem__(self, item):
        return self.edges[item]

    def __setitem__(self, key, value):
        self.edges[key] = value

    def __iter__(self):
        return iter(self.verticies)

    def __str__(self):
        res = []
        print("liste de successeur")
        for i in self.verticies:
            res += ["succeurs de " + str(i) + "="]

            for j in self.edges[i]:
                res += [str((j, "poids =",  self.edges[i][j]))]

        return str(res)

    def affiche_mat(self):
        mat = [[ float('inf') for k in range(len(self.verticies))] for i in range(len(self.verticies))]
        for i in self.edges:
            for j in self.edges[i]:
                mat[i - 1][j - 1] = self.edges[i][j]
        for p in mat:
            print(p, end="\n")





















