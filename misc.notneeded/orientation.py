import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import serial.tools.list_ports
import serial







# Quaternion values
w = 1
x = 0.04
y = 0.95    
z = -0.10

# Create rotation matrix from quaternion values
rotation_matrix = np.array([[1-2*y*y-2*z*z, 2*x*y-2*w*z, 2*x*z+2*w*y],
                         [2*x*y+2*w*z, 1-2*x*x-2*z*z, 2*y*z-2*w*x],
                         [2*x*z-2*w*y, 2*y*z+2*w*x, 1-2*x*x-2*y*y]])

# Define initial position and orientation of the model
position = np.array([0, 0, 0])
orientation = np.array([1, 0, 0])

# Apply rotation to the model
rotated_orientation = np.dot(rotation_matrix, orientation)

# Apply translation to the model
new_position = position + rotated_orientation

# Plot the model
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(position[0], position[1], position[2], rotated_orientation[0], rotated_orientation[1], rotated_orientation[2], color='r')
plt.show()