#guided by https://ipython-books.github.io/133-simulating-a-brownian-motion/
import numpy as np
import matplotlib.pyplot as plt

n = 5000 #number of steps

x = np.cumsum(np.random.randn(n)) #array with cumulative sum for each random step
y = np.cumsum(np.random.randn(n))

k = 10 #number of colors

x2 = np.interp(np.arange(n * k), np.arange(n) * k, x)
y2 = np.interp(np.arange(n * k), np.arange(n) * k, y)

fig, ax = plt.subplots(1, 1, figsize=(8,8))

ax.scatter(x2, y2, c=range(n*k), linewidths = 0,
           marker="o", s=3, cmap=plt.cm.jet,)

ax.axis("equal")

plt.show()
