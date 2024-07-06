import Graph
import math


def nearestNeighbour(g):
    prev = g.nodes[0]
    vis = [0 for i in range(g.n)]
    path = [0]
    vis[0] = 1
    netCost = 0

    for i in range(g.n - 1):
        cost, best = math.inf, i
        for j in range(g.n):
            if j == prev or vis[j]:
                continue
            curr = g.nodes[j]
            if math.sqrt((prev[0] - curr[0]) ** 2 + (prev[1] - curr[1]) ** 2) < cost:
                cost, best = (
                    math.sqrt((prev[0] - curr[0]) ** 2 + (prev[1] - curr[1]) ** 2),
                    j,
                )

        prev = g.nodes[best]
        vis[best] = 1
        path.append(best)
        netCost += cost

    netCost += math.sqrt(
        (g.nodes[path[0]][0] - g.nodes[path[-1]][0]) ** 2
        + (g.nodes[path[0]][1] - g.nodes[path[-1]][1]) ** 2
    )
    return (netCost, path)
