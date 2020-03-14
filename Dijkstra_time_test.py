__author__ = "tristan"
__file__ = "Dijkstra_basic.py"
__date__ = "08/03/2020"

import time
import matplotlib.pyplot as plt
from Generation.Source.graph_generation import *

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
