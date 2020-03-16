__author__ = "tristan"
__file__ = "Dijkstra_basic.py"
__date__ = "08/03/2020"

import time
import matplotlib.pyplot as plt
from Generation.Source.graph_generation import *


def compute_time(graph, start, end):
    t1 = time.process_time()
    d = graph.dijkstra_binary_heap_one_track(start, end)
    t2 = time.process_time()
    return t2 - t1

def trace_time_sample(nb_verticies, nb_edges, nb_experience, nb_sample_by_exp):
    liste_min = []
    liste_max = []
    liste_moyenne = []
    liste_median = []


    for i in range(nb_experience):
        print( i / nb_experience * 100, "%")
        graph_test = generate_random_graph(nb_verticies, nb_edges, True)
        liste_temps = []
        verticies = copy(graph_test.verticies)

        for j in range(nb_sample_by_exp):
            s0 = rdm.choice(verticies)
            vert2 = copy(verticies)
            vert2.remove(s0)
            s1 = rdm.choice(vert2)
            temps = compute_time(graph_test, s0, s1)
            liste_temps.append(temps)

        liste_temps.sort()
        liste_min.append(liste_temps[0])
        liste_max.append(liste_temps[-1])
        liste_moyenne.append(sum(liste_temps) / len(liste_temps))
        liste_median.append(liste_temps[int(len(liste_temps) / 2)])


    liste_exp = [j for j in range(nb_experience)]
    plt.plot(liste_exp, liste_min, label="temps minimum")

    plt.ylabel("temps")
    plt.xlabel("numéro exp")
    plt.legend()
    plt.show()

    plt.plot(liste_exp, liste_max, label="temps maximum")
    plt.ylim(0, 1.2)
    plt.ylabel("temps")
    plt.xlabel("numéro exp")
    plt.legend()
    plt.show()

    plt.plot(liste_exp, liste_moyenne, label="temps moyen")
    plt.ylim(0, 1.2)
    plt.ylabel("temps")
    plt.xlabel("numéro exp")
    plt.legend()
    plt.show()

    plt.plot(liste_exp, liste_median, label="temps median")
    plt.ylim(0, 1.2)
    plt.ylabel("temps")
    plt.xlabel("numéro exp")
    plt.legend()
    plt.show()


ta = []
tb = []
tc = []
n = []

for i in range(500, 3501,  500):
    n.append(i)
    G = generate_random_graph(i, int(0.5 * i*(i-1)/2), False)
    v1 = rd.choice(G.verticies)

    t1 = time.process_time()
    G.dijkstra_base(v1)
    t2 = time.process_time()
    ta.append(t2 - t1)

    t1 = time.process_time()
    G.dijkstra_binary_heap(v1)
    t2 = time.process_time()
    tb.append(t2 - t1)

    print(i)


plt.plot(n, ta)
plt.plot(n, tb)
plt.show()
plt.loglog(n, ta)
plt.loglog(n, tb)
plt.show()
