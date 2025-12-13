import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# allows us to choose what operation we want to preform
SHOW_ADDITION = False
SHOW_SCALING = False
SHOW_CROSS = True
SHOW_TRANSFORM = False

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Base vectors
v = np.array([2, 3, 1])
u = np.array([-1, 0, 2])
w = v + u

# Original vectors
ax.quiver(0, 0, 0, *v, color='red', alpha=0.4, linewidth=2, label='v')
ax.quiver(0, 0, 0, *u, color='blue', alpha=0.4, linewidth=2, label='u')

# Vector addition 
if SHOW_ADDITION:
    ax.quiver(*v, *u, color='purple', alpha=0.4, linewidth=2)
    ax.quiver(0, 0, 0, *w, color='green', linewidth=3, label='v + u')

# Scalar scaling 
if SHOW_SCALING:
    ax.quiver(0, 0, 0, *(2*v), color='orange', alpha=0.4, label='2v')

# Cross product
if SHOW_CROSS:
    cross = np.cross(v, u)
    ax.quiver(0, 0, 0, *cross, color='cyan', linewidth=3, label='v × u')

# Linear transformation
if SHOW_TRANSFORM:
    A = np.array([[1, 0.5, 0],
                  [0, 1, 0],
                  [0, 0, 1]])
    tv = A @ v
    ax.quiver(0, 0, 0, *tv, color='magenta', linewidth=3, label='A·v')

#axes
ax.set_xlim([-2, 4])
ax.set_ylim([-2, 4])
ax.set_zlim([-2, 4])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.legend()
ax.set_title("Linear Algebra visualizer")
plt.show()


