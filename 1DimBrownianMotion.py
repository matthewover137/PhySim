#guided by https://www.quantstart.com/articles/brownian-motion-simulation-with-python/
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

overlay = True
paths = 10
points = 1000

mu, sigma = 0.0, 1.0 #drift, std dev

Z = rng.normal(mu, sigma, (paths, points)) #creates a matrix of probabilities 

interval = [0, 1]
dt = (interval[1] - interval[0]) / (points - 1)

t_axis = np.linspace(interval[0], interval[1], points)

W = np.zeros((paths, points))
for idx in range(points - 1): #idx is the current time. 
    real_idx = idx + 1
    W[:, real_idx] = W[:, real_idx - 1] + np.sqrt(dt) * Z[:, idx] #W[:, real_idx] calls all paths (a whole column) at column number of next idx

#plotting
final_values = pd.DataFrame({'final_values': W[:, -1]}) # -1 is the same as the last index of array
if overlay:
    fig, ax = plt.subplots(1, 1, figsize=(12,8))
    for path in range(paths):
        ax.plot(t_axis, W[path, :])
    sns.kdeplot(data=final_values, y='final_values', fill=True, ax=ax, label = 'KDE') #uses kernel density estimate to make cont. dist over finite data points

    ax.set_title("Standard Brownian Motion sample paths")
    ax.set_xlabel("Time")
    ax.set_ylabel("Asset Value")
else:
    fig, ax = plt.subplots(2, 1, figsize=(12,8))
    for path in range(paths):
        ax[0].plot(t_axis, W[path, :])
    ax[0].set_title("Standard Brownian Motion sample paths")
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("Asset Value")

    sns.kdeplot(data=final_values, x='final_values', fill=True, ax=ax[1]) #uses kernel density estimate to make cont. dist over finite data points
    ax[1].set_title("Kernel Density Estimate of asset path final value distribution")
    ax[1].set_ylim(0.0, 0.325)
    ax[1].set_xlabel('Final Values of Asset Paths')

#Printing mean and std
Mean = round(float(final_values.mean()), 2)
std = round(float(final_values.std()), 2)
message = "Mean: " + str(Mean) + "\nstd: " + str(std)
plt.text(.9472, 3.91, message, fontsize=12, ha='center', va='center', color='blue')

plt.show()
