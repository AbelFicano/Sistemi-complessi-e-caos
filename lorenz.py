import numpy as np
import matplotlib.pyplot as plt

def lorenz(x, y, z, s, r, b, dt):
     dx = s*(y - x) * dt            #Calcoliamo variazioni infinitesime
     dy = (r*x - y - x*z) * dt
     dz = (x*y - b*z) * dt
     return x + dx, y + dy, z + dz  #Restituiamo nuovi valori di x, y, z

def points(xi=0., yi=10., zi=10.05, s=10, r=28, b=2.667, dt=0.01, num_steps=1000):
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    xs[0], ys[0], zs[0] = (xi, yi, zi)

    for i in range(num_steps):
        xs[i + 1], ys[i + 1], zs[i + 1] = lorenz(xs[i], ys[i], zs[i], s, r, b, dt)

    return xs, ys, zs

'''def plot():
    coords = points()
    plot = plt.figure().add_subplot(projection='3d')
    plot.plot(coords[0], coords[1], coords[2], 'k-', lw=0.5)'''

coords1 = points()
coords2 = points(0.01)

"""graph = plt.figure().add_subplot(projection='3d')
graph.plot(coords1[0], coords1[1], coords1[2], 'k-', lw=0.5)
#graph.plot(coords2[0], coords2[1], coords2[2], 'r-', lw=0.5)
plt.show()"""

diff = np.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2 + (coords1[2] - coords2[2])**2)


plt.plot([i for i in range(1001)], diff)
plt.show()
