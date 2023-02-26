import numpy as np
import matplotlib.pyplot as plt

## Example 1: Plot a bunch of points 
## along the line y = x

#for i in range(100):
#    plt.scatter(i, i, s=i/10, c='g')

## Example 2: A "random walk"
## I'm going to start at x = 0, y = 0
## And then I'm going to move either
## left/right/up/down

x = 0
y = 0
for it in range(1000):
    plt.scatter(x, y, it/50, c='g')
    # Make a random choice of where to go next
    choice = np.random.randint(4)
    if choice == 0:
        # Move left
        x -= 1
    elif choice == 1:
        # Move right
        x += 1
    elif choice == 2:
        # Move down
        y -= 1
    else:
        # Move up
        y += 1