import operator
import random

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def find_route(json_data, from_id, to_id):
    for item in json_data['routes']:
        if item['source_id'] == from_id and item['target_id'] == to_id:
            return item
    return None


def get_point_data(json_data, id):
    for item in json_data['features']:
        if item['id'] == id:
            return item
    return None

class Point():
    def __init__(self, id, data_points, data_routes):
        self.id = id
        self.data_points = data_points
        self.data_routes = data_routes
        item = get_point_data(self.data_points, id)

        self.coords = item['geometry']['coordinates']
        self.name = item['properties']['iconCaption']
        if self.name[:5] == "Склад":
            self.type = 'storage'
        else:
            self.type = 'client'

    def get_distance(self, point):
        data = self.data_routes
        item = find_route(data, self.id, point.id)
        return item['distance']

    def get_duration(self, point):
        data = self.data_routes
        item = find_route(data, self.id, point.id)
        return item['duration']


class Product():
    def __init__(self,
                 id):
        self.id = id

class ProductOrder():
    def __init__(self,
                 point_to,
                 products
                ):
        self.to_point = point_to
        self.products = products


class Order():
    def __init__(self,
                 from_point,
                 productOrders
                ):
        self.from_point = from_point
        self.productOrders = productOrders


class Fitness():
    def __init__(self, order, optimizationOn='time'):
        self.order = order
        self.optimizationOn = optimizationOn
        self.distance = 0.0
        self.fitness = 0.0

    def routeDistance(self):
        if self.distance ==0:
            pathDistance = 0
            fromPoint = self.order.from_point
            for i in range(0, len(self.order.productOrders)+1):
                toPoint = None
                if i < len(self.order.productOrders):
                    toPoint = self.order.productOrders[i].to_point
                else:
                    toPoint = self.order.from_point
                if self.optimizationOn == 'distance':
                    pathDistance += fromPoint.get_distance(toPoint)
                elif self.optimizationOn == 'time':
                    pathDistance += fromPoint.get_duration(toPoint)
                if i < len(self.order.productOrders):
                    fromPoint = self.order.productOrders[i].to_point
            self.distance = pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness


def createOrder(productIds, clientIds, storageIds, points_json, routes_json, numProductOrders=5,
               numProducts=10):
    productOrders = []
    for i in range(numProductOrders):
        productOrders.append(ProductOrder(
            Point(clientIds[i], points_json, routes_json),
            [Product(productIds[j])
            for j in range(len(productIds))]
        ))
    productOrders = random.sample(productOrders, len(productOrders))
    order = Order(
        Point(storageIds[0], points_json, routes_json),
        productOrders
    )
    return order



def initialPopulation(popSize, productIds, clientIds, storageIds, points_json, routes_json, numProductOrders=5,
               numProducts=10):
    population = []

    for i in range(0, popSize):
        population.append(createOrder(productIds, clientIds, storageIds, points_json, routes_json, numProductOrders=numProductOrders))
    return population



def rankOrders(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def breed(parent1, parent2, points_json, routes_json):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1.productOrders))
    geneB = int(random.random() * len(parent1.productOrders))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    for i in range(startGene, endGene):
        childP1.append(parent1.productOrders[i].to_point.id)
    childP2 = [item.to_point.id for item in parent2.productOrders if item.to_point.id not in childP1]
    child = childP1 + childP2

    parent = Order(
        Point(parent1.from_point.id, points_json, routes_json),
        [ProductOrder(
        Point(point_id, points_json, routes_json),
        parent1.productOrders[0].products
    ) for point_id in child]
    )

    return parent


def breedPopulation(matingpool, eliteSize, points_json, routes_json):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))
    for i in range(0,eliteSize):
        children.append(matingpool[i])
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1], points_json, routes_json)
        children.append(child)
    return children


def mutate(individual, mutationRate):
    for swapped in range(len(individual.productOrders)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual.productOrders))

            city1 = individual.productOrders[swapped]
            city2 = individual.productOrders[swapWith]

            individual.productOrders[swapped] = city2
            individual.productOrders[swapWith] = city1
    return individual



def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop


def nextGeneration(currentGen, eliteSize, mutationRate, points_json, routes_json):
    popRanked = rankOrders(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    # print([item.to_point.id for item in matingpool[0].productOrders])
    children = breedPopulation(matingpool, eliteSize, points_json, routes_json)
    nextGeneration = mutatePopulation(children, mutationRate)
    nextGeneration = children
    return nextGeneration


def geneticAlgorithm(clientIds, storageIds, popSize, eliteSize, mutationRate, generations, points_json, routes_json,
                    numProductOrders=10, numProducts=10, productIds=[]):
    pop = initialPopulation(popSize, productIds, clientIds, storageIds, points_json, routes_json, numProductOrders=numProductOrders)
    progress = []
    progress.append(1 / rankOrders(pop)[0][1])
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate, points_json, routes_json)
        progress.append(1 / rankOrders(pop)[0][1])
        if i % 10 == 0:
            bestRouteIndex = rankOrders(pop)[0][0]
            bestRoute = pop[bestRouteIndex]
            route = [(item.to_point.coords[0], item.to_point.coords[1]) for item in bestRoute.productOrders]
    bestRouteIndex = rankOrders(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute


def cluster_points(points, num_clusters):
    # Извлечение координат точек
    coordinates = [point[1] for point in points]

    # Создание модели KMeans
    kmeans = KMeans(n_clusters=num_clusters)

    # Проведение кластеризации
    kmeans.fit(coordinates)

    # Получение меток кластеров для каждой точки
    labels = kmeans.labels_

    # Создание словаря для хранения точек по кластерам
    clusters = {i: [] for i in range(num_clusters)}

    # Добавление точек в соответствующие кластеры
    for i, label in enumerate(labels):
        point_id, (x, y) = points[i]
        clusters[label].append(point_id)

    return clusters

async def get_routes(from_point_id, point_ids, points_json, routes_json, num_trucks=1):
    points = [Point(id, points_json, routes_json) for id in point_ids]
    points = [(point.id, (point.coords[0], point.coords[1])) for point in points]
    clustered_points = cluster_points(points, num_trucks)

    ans = []
    for cluster, clients in clustered_points.items():
        n = len(clients)
        popSize = int(15 + 15*(n/20))
        eliteSize = popSize // 3
        generations = int(50 * (n/20) + 10)
        best_gen = geneticAlgorithm(clients,
                            [from_point_id],
                            popSize=popSize, eliteSize=eliteSize, mutationRate=0.05,
                            generations=generations,
                            numProductOrders=n,
                            points_json=points_json,
                            routes_json=routes_json)
        ans.append([from_point_id] + [item.to_point.id for item in best_gen.productOrders] + [from_point_id])
    return ans



