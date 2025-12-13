import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax =  fig.add_subplot(111, projection ='3d')
v = np.array([2, 3, 1])

ax.quiver(0, 0, 0, v[0], v[1], v[2])
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])

ax.set_xlabel = ('X')
ax.set_ylabel = ('Y')
ax.set_zlabel = ('Z')
plt.show()