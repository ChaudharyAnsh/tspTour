import math
import DSU
from itertools import permutations


class Graph:
    def __init__(self, nodes):
        self.n = len(nodes)
        self.nodes = nodes
        self.edges = []
        self.baseline = math.inf
        self.__filledges__()

    def __filledges__(self):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                self.edges.append((i, j, math.dist(self.nodes[i], self.nodes[j])))
        self.edges.sort(key=lambda e: e[2])

    def mst(self, init=0):
        dsu = DSU.dsu(self.n)
        mstEdges = []
        for edge in self.edges:
            if dsu.find(edge[0]) == dsu.find(edge[1]):
                continue
            self.baseline += init * edge[2]
            dsu.union(edge[0], edge[1])
            mstEdges.append((edge[0], edge[1]))

        self.baseline += init * self.edges[0][2]
        return mstEdges

    def calculateBaseLine(self):
        if self.n < 10:
            for comb in permutations(self.nodes):
                cost = 0
                prev = comb[-1]
                for node in comb:
                    cost += math.sqrt(
                        (node[0] - prev[0]) ** 2 + (node[1] - prev[1]) ** 2
                    )
                    prev = node
                self.baseline = min(self.baseline, cost)
        else:
            self.baseline = 0
            self.mst(init=1)
        return self.baseline
