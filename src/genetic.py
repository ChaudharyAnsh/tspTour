import math
import random

def generateRandomPaths(n):
    randomPaths = []
    for _ in range(20000):
        randomPath = list(range(n))
        random.shuffle(randomPath)
        randomPaths.append(randomPath)
    return randomPaths

def totalDistance(nodes, path):
    return sum(math.dist(nodes[path[i - 1]], nodes[path[i]]) for i in range(len(path)))

def chooseSurvivors(nodes, oldGen):
    survivors = []
    random.shuffle(oldGen)
    midway = len(oldGen) // 2
    for i in range(midway):
        if totalDistance(nodes, oldGen[i]) < totalDistance(nodes, oldGen[i + midway]):
            survivors.append(oldGen[i])
        else:
            survivors.append(oldGen[i + midway])
    return survivors


def createOffspring(parentA, parentB):
    offspring = []
    start = random.randint(0, len(parentA) - 1)
    finish = random.randint(start, len(parentA))

    presentInA = [0 for i in range(len(parentA))]
    subPathA = parentA[start:finish]
    for item in subPathA:
        presentInA[item] += 1
    subPathB = list([item for item in parentB if not presentInA[item]])

    ida, idb = 0, 0
    for i in range(0, len(parentA)):
        if start <= i < finish:
            offspring.append(subPathA[ida])
            ida += 1
        else:
            offspring.append(subPathB[idb])
            idb += 1
    return offspring


def applyCrossovers(survivors):
    offsprings = []
    midway = len(survivors) // 2
    for i in range(midway):
        parentA, parentB = survivors[i], survivors[i + midway]
        for _ in range(2):
            offsprings.append(createOffspring(parentA, parentB))
            offsprings.append(createOffspring(parentB, parentA))
    return offsprings


def applyMutations(generation):
    mutated = []
    for path in generation:
        if random.randint(0, 1000) < 9:
            index1 = random.randint(0, len(path)-1)
            index2 = random.randint(0, len(path)-1)
            path[index1], path[index2] = path[index2], path[index1]
        mutated.append(path)
    return mutated


def generateNewPopulation(nodes, oldGen):
    survivors = chooseSurvivors(nodes, oldGen)
    crossovers = applyCrossovers(survivors)
    newPopulation = applyMutations(crossovers)
    return newPopulation


def choose_best(nodes, paths, count):
    return sorted(paths, key=lambda path: totalDistance(nodes, path))[:count]


def choose_worst(nodes, paths, count):
    return sorted(paths, reverse=True, key=lambda path: totalDistance(nodes, path))[
        :count
    ]


def choose_random(paths, count):
    return [random.choice(paths) for _ in range(count)]


def genetic(nodes):
    oldGen = generateRandomPaths(len(nodes))
    for _ in range(500):
        newGen = generateNewPopulation(nodes, oldGen)
        oldGen = newGen
    winner = choose_best(nodes, oldGen, 1)[0]
    return (totalDistance(nodes, winner), winner)