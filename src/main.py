import Graph
import nearest
import greedy
import christofides
import random
import opt2
import opt3
import genetic


def main(nodes):
    g = Graph.Graph(nodes)
    g.calculateBaseLine()
    ch = christofides.solve(g)
    o2 = opt2.opt2(ch[0], ch[1], nodes)
    return (
        nearest.nearestNeighbour(g)[0] / g.baseline,
        greedy.greedySolution(g)[0] / g.baseline,
        ch[0] / g.baseline,
        o2[0] / g.baseline,
        opt3.opt3(o2[0], o2[1], nodes)[0] / g.baseline,
    )


nn, gr, ch, o2, o3 = 0, 0, 0, 0, 0
iter = 100
for i in range(iter):
    nodes = []
    for j in range(500):
        x, y = random.randint(0, 10000), random.randint(0, 10000)
        nodes.append((x, y))

    (a, b, c, d, e) = main(nodes)
    nn += a
    gr += b
    ch += c
    o2 += d
    o3 += e

print("Cost ration of deterministic Algorithms on random 500 node graphs.")
print(
    " Nearest Neighbout  : %0.5f\n" % (nn / iter),
    "Greedy             : %0.5f\n" % (gr / iter),
    "Christopheles      : %0.5f\n" % (ch / iter),
    "Christopheles 2opt : %0.5f\n" % (o2 / iter),
    "Christopheles 3opt : %0.5f\n" % (o3 / iter),
)


print(
    "Checking the value for a random graph using genetic Algorithm. ~2 min for n = 20 nodes. (scales linearly with n)"
)
nodes = []
for j in range(20):
    x, y = random.randint(0, 1000), random.randint(0, 1000)
    nodes.append((x, y))
g = Graph.Graph(nodes)

baseline = g.calculateBaseLine()
gen = genetic.genetic(nodes)[0] / g.baseline
print("Genetic: ", gen)

(nn, gr, ch, o2, o3) = main(nodes)
print(
    " Nearest Neighbour  : %0.5f\n" % (nn),
    "Greedy             : %0.5f\n" % (gr),
    "Christopheles      : %0.5f\n" % (ch),
    "Christopheles 2opt : %0.5f\n" % (o2),
    "Christopheles 3opt : %0.5f\n" % (o3),
)
