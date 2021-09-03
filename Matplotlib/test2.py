import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title-1')

left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(y, x, 'b')
ax1.set_xlabel('y')
ax1.set_ylabel('x')
ax1.set_title('title-1 inside')
plt.show()