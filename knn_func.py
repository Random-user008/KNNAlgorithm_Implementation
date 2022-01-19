
import math
import matplotlib.pyplot as plt
#import numpy as np


def knn(data, query, k, distance_fn, choice_fn):
    neighbor_distances_and_indices = []
    for index, data1 in enumerate(data):
        #print(index,data1)
        distance = distance_fn(data1[1:], query)
      
        neighbor_distances_and_indices.append((distance, index))
       
   
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    ypoints = []
    xpoints = []
    for dist,index in sorted_neighbor_distances_and_indices:
        ypoints.append(dist)
        xpoints.append(index)
        label = "{:.2f}".format(dist)
        plt.annotate(label,(index,dist),ha='left')
    plt.plot(xpoints,ypoints,'o')
    plt.show()
    #print(sorted_neighbor_distances_and_indices)
   
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
   
    k_nearest_labels = [data[i][0] for distance, i in k_nearest_distances_and_indices]
    return k_nearest_distances_and_indices , choice_fn(k_nearest_labels)

def mean(nums):
    #print(sum(nums))
    return sum(nums) / len(nums)


def euclidean_distance(point1, point2):
    sum1 = 0
    for i in range(len(point1)):
        sum1 += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum1)

