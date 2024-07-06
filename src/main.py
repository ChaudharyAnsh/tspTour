import Graph
import nearest
import greedy
import christofides
import random
import opt2
import opt3


def main(nodes):
    g = Graph.Graph(nodes)
    g.calculateBaseLine()
    if len(nodes) < 10:
        print("Using actual baseline", g.baseline)
        return (
            nearest.nearestNeighbour(g),
            greedy.greedySolution(g),
            christofides.solve(g),
        )
    else:
        ch = christofides.solve(g)
        o2 = opt2.opt2(ch[0], ch[1], nodes); 
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
    # print(a, b, c, d, e)
print(
    "%0.5f" % (nn / iter),
    "%0.5f" % (gr / iter),
    "%0.5f" % (ch / iter),
    "%0.5f" % (o2 / iter),
    "%0.5f" % (o3 / iter),
)
