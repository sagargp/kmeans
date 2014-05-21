import numpy
import time
import random
import matplotlib.pyplot as plt

def distance(p1, p2):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

class Cluster(object):
  def __init__(self, center):
    self.center = center

  def update(self, points):
    new_center = points[0]
    for x, y in points[1:]:
      new_center = (new_center[0]+x, new_center[1]+y)
    new_center = (new_center[0]/len(points), new_center[1]/len(points))
    moved = distance(new_center, self.center)
    self.center = new_center
    return moved

def kmeans(points, k):
  # initialize k clusters as random points
  clusters = [Cluster(c) for c in random.sample(points, k)]

  while True:
    # keep track of new points for each cluster
    new_cluster_points = [[] for _ in range(k)]

    # assign each point to the nearest cluster
    for p in points:
      closest_cluster = min(enumerate([distance(p, c.center) for c in clusters]), key=lambda x:x[1])[0]
      new_cluster_points[closest_cluster].append(p)

    yield clusters

    cluster_moves = [1]*k
    for i, cluster in enumerate(clusters):
      cluster_moves[i] = cluster.update(new_cluster_points[i])

    if all([m == 0.0 for m in cluster_moves]):
      break

if __name__ == "__main__":
  k = 5
  plt.figure()
  plt.ion()
  plt.show()

  while True:
    points = []
    for num_clusters in range(random.randint(3, 8)):
      p = numpy.random.normal(random.randint(1, 10), random.random()*0.5, (100, 2))
      points.append(p)
    points = numpy.concatenate(points)

    for clusters in kmeans(points, k):
      plt.clf()

      x_coords, y_coords = zip(*points)
      plt.scatter(x_coords, y_coords, c="b", s=1)

      cluster_centers = [c.center for c in clusters]
      c_x_coords, c_y_coords = zip(*cluster_centers)
      plt.scatter(c_x_coords, c_y_coords, c="r", s=100)
      plt.draw()
    
    time.sleep(3.0)
