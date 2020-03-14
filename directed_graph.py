__autor__ = "Max Begue"
__date__ = "19/02/2020"
__file_name__ = "directed_graph.py"


import numpy as np
from copy import *
import heapq as hq

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
        return res

    ### induced à retravailler car complexité dégueue

    def __len__(self):
        """ return |V|"""
        return len(self.verticies)

    def nb_edges(self):
        """return |E|"""
        len_edges = 0
        for i in self.edges:
            len_edges += len(self.edges[i])
        return len_edges

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

        """affiche la matrice d'adjacence, les noeuds doivent etre numérotés de 0 à n-1"""

        mat = [[ float('inf') for k in range(len(self.verticies))] for i in range(len(self.verticies))]
        for i in self.edges:
            for j in self.edges[i]:
                mat[i][j] = self.edges[i][j]
        for p in mat:
            print(p, end="\n")


    def dijkstra_base(self, s):
        """basic dijkstra algorithm, return distances from s to all other verticies"""
        F = set(copy(self.verticies))
        dist = {}
        for v in self.verticies:
            dist[v] = float('inf')
        dist[s] = 0

        while len(F) != 0:

            print(F)

            mini = float("inf")
            index = - 1
            for j in F:
                if dist[j] < mini:
                    mini = dist[j]
                    index = j

            u = index
            print(u)

            if u == -1:
                return dist
            else:
                F.remove(u)

            for v in F & self.edges[u].keys():
                if dist[u] + self.edges[u][v] < dist[v]:
                    dist[v] = dist[u] + self.edges[u][v]
        return dist

    def dijkstra_binary_heap(self, s):
        """upgraded dijkstra using a binary heap to get the argmin in constant time, assuming connexity of graph"""

        F = set(copy(self.verticies))
        dist = {}
        for v in self.verticies:
            dist[v] = float('inf')
        dist[s] = 0

        preheap = [(dist[v], v) for v in dist]

        hq.heapify(preheap)

        while len(F) != 0:

            u = hq.heappop(preheap)[1]

            F.remove(u)

            for v in F & self.edges[u].keys():
                if dist[v] > dist[u] + self.edges[u][v]:
                    dist[v] = dist[u] + self.edges[u][v]
                    hq.heappush(preheap, (dist[v], v))

        return dist


    def dijkstra_binary_heap_one_track(self, start, finish):
        """upgraded dijkstra using a binary heap to get the argmin in constant time, assuming connexity of graph"""

        F = set(copy(self.verticies))
        dist = {}
        for v in self.verticies:
            dist[v] = float('inf')
        dist[start] = 0

        preheap = [(dist[v], v) for v in dist]

        hq.heapify(preheap)

        while len(F) != 0:

            u = hq.heappop(preheap)[1]

            if u == finish:
                return dist[finish]

            F.remove(u)

            for v in F & self.edges[u].keys():
                if dist[v] > dist[u] + self.edges[u][v]:
                    dist[v] = dist[u] + self.edges[u][v]
                    hq.heappush(preheap, (dist[v], v))

        return dist





















