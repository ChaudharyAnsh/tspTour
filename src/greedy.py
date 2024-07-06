import Graph
import math
import DSU


def greedySolution(g):
    path = []
    cost = 0
    dsu = DSU.dsu(g.n)
    deg = [0 for i in range(g.n)]

    for e in g.edges:
        if dsu.find(e[0]) == dsu.find(e[1]) or deg[e[0]] == 2 or deg[e[1]] == 2:
            continue
        deg[e[0]] += 1
        deg[e[1]] += 1
        cost += e[2]
        dsu.union(e[0], e[1])
        path.append((e[0], e[1]))

    a, b = -1, -1
    for i, x in enumerate(deg):
        if x == 1 and a == -1:
            a = i
        elif x == 1:
            b = i
    cost += math.dist(g.nodes[a], g.nodes[b])
    path.append((a, b))
    return (cost, path)
