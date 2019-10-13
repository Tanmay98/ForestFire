import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import cv2

img = plt.imread('gg.png')

x = np.array([620])
y = np.array([275])

# Create a figure. Equal aspect so circles look circular
fig,ax = plt.subplots(1)
ax.set_aspect('equal')

# Show the image
ax.imshow(img)

# Now, loop through coord arrays, and create a circle at each x,y pair
for xx,yy in zip(x,y):
    circ = Circle((xx,yy),145, fill=False)
    ax.add_patch(circ)

# Show the image

plt.show()

