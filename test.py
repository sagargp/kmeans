import time
import random
import matplotlib.pyplot as plt

#plt.figure()
#plt.ion()
#plt.show()
#
#colors = ['r']*500 + ['b']*500
#while 1:
#  xvals = [random.randint(0, 1000) for k in range(0, 1000)]
#  yvals = [random.randint(0, 1000) for k in range(0, 1000)]
#
#  plt.clf()
#  plt.scatter(xvals[0:500],    yvals[0:500],    c=colors[0:500], marker='o')
#  plt.scatter(xvals[500:1000], yvals[500:1000], c=colors[500:1000], marker='s')
#  plt.draw()
#  time.sleep(0.01)

plt.figure()

k = 9 
size = 1000
centroids = []

for x in range(0, int(k**.5)):
  for y in range(0, int(k**.5)):
    centroids.append((x, y))

plt.scatter(zip(*centroids)[0], zip(*centroids)[1])
plt.show()
