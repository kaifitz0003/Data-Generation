"""
The variable shape can be used to generate circles or squares.
"""
import matplotlib.pyplot as plt
import numpy as np


num_of_shapes = 5
xlim = 300
ylim = 150
for i in range (num_of_shapes):
  fig, ax = plt.subplots()
  ax.set_xlim(0, xlim)
  ax.set_ylim(0, ylim)
  ax.set_aspect('equal', 'box')
  center_x = np.random.randint(0, xlim)
  center_y = np.random.randint(0, ylim)
  #shape = plt.Circle((np.random.randint(0, xlim), np.random.randint(0, ylim)), radius=(i+1)*10, color='red', fill=False)
  shape = plt.Rectangle((center_x, center_y),(i+1)*10,(i+1)*10, fill=None, edgecolor =  'r')
  ax.add_patch(shape)
  plt.axis('off') # Turn on and off
  plt.savefig('Data/'+str(i)+'.png',bbox_inches = 'tight' )

