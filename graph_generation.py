__author__ = "tristan"
__file__ = "graph_generation.py"
__date__ = "19/02/2020"

import random as rd
from Directed_Undirected.Source.Undirected_graph import *
from copy import *


def generate_random_graph(n_nodes, n_edges, directed):
    """ Creates a graph with randomly generated edges"""

    if not directed:

        if n_nodes != 0:
            assert (n_nodes <= n_edges <= n_nodes * (n_nodes - 1)/2)

        else:
            assert (n_edges == 0)
            G = Undirected_graph()
            return G

        possible_edges = set()
        for n1 in range(n_nodes):
            for n2 in range(n_nodes):
                if n1 != n2 and (n1, n2) not in possible_edges and (n2, n1) not in possible_edges:
                    possible_edges.add((n1, n2))

        G = Undirected_graph()

        G.add_vertex(0)
        for i in range(1, n_nodes):
            G.add_vertex(i)
            n2 = rd.randrange(0, len(G)-1)
            G.add_edge(i, n2, 1)
            if (i, n2) in possible_edges:
                possible_edges.remove((i, n2))
            else:
                possible_edges.remove((n2, i))

        while G.nb_edges() < n_edges:
            edge = rd.sample(possible_edges, 1)[0]
            G.add_edge(edge[0], edge[1], 1)
            possible_edges.remove(edge)

        return G

    elif directed:

        if n_nodes != 0:
            assert (n_nodes <= n_edges <= n_nodes * (n_nodes - 1))

        else:
            assert (n_edges == 0)
            G = Directedgraph()
            return G

        possible_edges = set()
        for n1 in range(n_nodes):
            for n2 in range(n_nodes):
                if n1 != n2:
                    possible_edges.add((n1, n2))

        possible_nodes = [i for i in range(n_nodes)]

        G = Directedgraph()

        G.add_vertex(possible_nodes[0])
        possible_nodes.remove(possible_nodes[0])

        for i in possible_nodes:
            G.add_vertex(i)
            n2 = rd.randrange(0, len(G)-1)
            G.add_edge(i, n2, 1)
            possible_edges.remove((i, n2))

        while G.nb_edges() < n_edges:
            edge = rd.sample(possible_edges, 1)[0]
            G.add_edge(edge[0], edge[1], 1)
            possible_edges.remove(edge)

        return G


def generate_random_community_graph(n_nodes_per_community, p_intra, p_inter):

    G = Undirected_graph()
    communities = []

    c = 0
    for k in n_nodes_per_community:
        com = Undirected_graph()
        for i in range(c, c + k):
            com.add_vertex(i)
            G.add_vertex(i)
        for v1 in com.verticies:
            for v2 in com.verticies:
                if rd.random() <= p_intra:
                    com.add_edge(v1, v2, 1)
                    G.add_edge(v1, v2, 1)
        communities.append(com)
        c += k

    while len(communities) != 1:
        com1 = communities[0]
        for v1 in com1.verticies:
            for j in range(1, len(communities)):
                com2 = communities[j]
                for v2 in com2.verticies:
                    if rd.random() <= p_inter:
                        G.add_edge(v1, v2, 1)
        communities.remove(com1)

    return G
