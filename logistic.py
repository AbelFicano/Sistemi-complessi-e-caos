import numpy as np
import matplotlib.pyplot as plt

'''map() function: plots the logistic map'''
def map():
    acc = 1000    #Accuracy: number of r values
    steps = 500   #Steps: number of iterations of the logistic equation
    rs = np.zeros(acc)
    xs = np.zeros((acc, int(0.1 * steps)))
    for i in range(acc):
        rs[i] = 1 + i * (3 / acc)   #rs are chosen in range (1, 4)
        xs[i] = log(rs[i], steps)
    plt.plot(rs, xs, ',')
    plt.show()

'''log() function: iterates the logistic equation ( x[n+1] = r * x[n] * (1-x[n]) )
    {steps} times for a given r value starting from x[0] = 0.5.
    Returns last 10% of the values.'''
def log(r, steps):
    xs = np.zeros(steps)
    xs[0] = 0.5
    for i in range(steps - 1):
        xs[i + 1] = r * xs[i] * (1 - xs[i])
    return xs[int(0.9 * steps):]

map()
