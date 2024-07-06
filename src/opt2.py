import christofides
import Graph
import math


def opt2(cost, path, nodes):
    n = len(path)
    # print(cost, end=" => ")
    for i in range(-1, n - 1):
        newCost = 0
        path[i], path[i + 1] = path[i + 1], path[i]
        for j in range(-1, n - 1):
            newCost += math.sqrt(
                (nodes[path[j]][0] - nodes[path[j + 1]][0]) ** 2
                + (nodes[path[j]][1] - nodes[path[j + 1]][1]) ** 2
            )
        
        if newCost < cost:
            cost = newCost
        else:
            path[i], path[i + 1] = path[i + 1], path[i]
    # print(cost)
    return (cost, path)
