__author__ = "tristan"
__file__ = "test_graph_generation.py"
__date__ = "19/02/2020"

from Generation.Source.graph_generation import *


def test_graph_generation():

    G = generate_random_graph(0, 0, True)
    assert((len(G), G.nb_edges()) == (0, 0))

    G = generate_random_graph(5, 7, True)
    assert((len(G), G.nb_edges()) == (5, 7))

    G = generate_random_graph(10, 16, True)
    assert((len(G), G.nb_edges()) == (10, 16))

    G = generate_random_graph(10, 89, True)
    assert((len(G), G.nb_edges()) == (10, 89))

    G = generate_random_graph(0, 0, False)
    assert((len(G), G.nb_edges()) == (0, 0))

    G = generate_random_graph(5, 7, False)
    assert((len(G), G.nb_edges()) == (5, 7))

    G = generate_random_graph(10, 16, False)
    assert((len(G), G.nb_edges()) == (10, 16))

    G = generate_random_graph(10, 45, False)
    assert((len(G), G.nb_edges()) == (10, 45))


test_graph_generation()

print(generate_random_community_graph([5, 5, 5, 5], 0.7, 0.4))
