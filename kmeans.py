#Author: Daniel Nicholson-Gardner #
#Name: template.py #
#Created On: 27/11/2019 #
#Modified by: Daniel Nicholson-Gardner #
#Last Modified: 13/12/2019 #

import numpy as np
def process_file(filename):
    with open(filename) as f:
        matrix = []
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                k, _ = line.split()
            else:
                rowData = np.array(line.split()).astype(np.float64)
                matrix.append(rowData)
    return int(k), np.array(matrix)


def distance(a, b):
    return np.sqrt(np.sum(np.square(a-b), axis=1))

def k_means(k, points):
    centers = np.copy(points[:k])
    n, m = points.shape
    new_centers = np.zeros((k, m))
    dist = np.zeros((k, n))
    
    while True:
        ## center to cluster
        # compute distance for each ith center
        for i in range(k):
            dist[i] = distance(points, centers[i])
        # find for cluster
        cluster = np.argmin(dist, axis=0)
        ## cluster to center
        for i in range(k):
            mask = [cluster == i]
            new_centers[i] = np.mean(points[mask], axis=0)
        
        # check converge
        if np.allclose(new_centers, centers):
           return new_centers
        centers, new_centers = new_centers, centers    

def printOut(num):
    n, m = num.shape
    for i in range(n):
        print (' '.join('{0:0.3f}'.format(ans[i, j]) for j in range(m)))

k, points = process_file("./datasets/rosalind_ba8c.txt")
ans = k_means(k, points)
printOut(ans)
