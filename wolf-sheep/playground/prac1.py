"""
reference:

Animation of Elastic collisions with Gravity

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-3, 3), ylim=(-3, 3))
particles, = ax.plot([], [], 'bo', ms=6)
points = np.array([
    [0.5, 0.5],
    [-0.5, 0.5],
    [-0.2, 0.2]
])


def init():
    particles.set_data([], [])
    return particles,


def animate(i):
    global points
    points = points + 0.02
    particles.set_data(points.T)
    particles.set_markersize(4)
    return particles,


ani = animation.FuncAnimation(fig, animate, frames=600,repeat=False,
                              interval=500, blit=True, init_func=init)
plt.show()
