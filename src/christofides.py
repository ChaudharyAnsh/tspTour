import Graph
import math
import DSU


def solve(g):
    mstEdges, deg, mpc = g.mst(), [0 for i in range(g.n)], {}
    oddNodes, induced = [], []

    for edge in mstEdges:
        deg[edge[0]] += 1
        deg[edge[1]] += 1

    for i in range(len(deg)):
        if deg[i] % 2:
            mpc[len(oddNodes)] = i
            oddNodes.append(g.nodes[i])

    for edge in mstEdges:
        induced.append((edge[0], edge[1]))

    subGraph = Graph.Graph(oddNodes)
    subGraphMST = subGraph.mst()

    vis = [0 for i in range(subGraph.n)]
    for edge in subGraph.edges:
        if vis[edge[0]] or vis[edge[1]]:
            continue

        induced.append((mpc[edge[0]], mpc[edge[1]]))
        vis[edge[0]] += 1
        vis[edge[1]] += 1

    neighbours = [[] for j in range(g.n)]
    for e in induced:
        neighbours[e[0]].append(e[1])
        neighbours[e[1]].append(e[0])

    vis = [0 for i in range(g.n)]
    path, prev, stack, vis = [], 0, [], [0 for i in range(g.n)]

    while stack or neighbours[prev]:
        if not neighbours[prev]:
            if not vis[prev]:
                path.append(prev)
                vis[prev] = 1
            prev = stack[-1]
            stack.pop()
        else:
            stack.append(prev)
            nxt = neighbours[prev][-1]
            neighbours[prev].pop()
            neighbours[nxt].pop(neighbours[nxt].index(prev))
            prev = nxt

    cost = 0
    for i in range(-1, g.n - 1):
        cost += math.dist(g.nodes[path[i]], g.nodes[path[i + 1]])
    return (cost, path)
