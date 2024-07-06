import christofides
import Graph


def opt2(cost, path, g):
    n = len(path)
    for i in range(-1, n - 1):
        path[i], path[i + 1] = path[i + 1], path[i]
        newCost = 0
        for i in range(-1, n - 2):
            path[i], path[i + 1] = path[i + 1], path[i]
            g.node[i], g.nodes[i + 1] = g.node[i + 1], g.nodes[i]
            for j in range(-1, n):
                newCost += math.dist(g.nodes[i], g.nodes[i + 1])
            if (newCost < cost):
                cost = newCost
            else:
                path[i], path[i + 1] = path[i + 1], path[i]
                g.node[i], g.nodes[i + 1] = g.node[i + 1], g.nodes[i]
    return(cost, path)