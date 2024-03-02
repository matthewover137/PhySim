#seeking to recreate digits of pi collision number in perfectly elastic collisions
import numpy as np
import matplotlib.pyplot as plt
m1 = 1
m2 = 10**4

v1 = 0
v2 = -1

#determines conditions after a collision
def BlockCollision(v1,v2,m1,m2):
    comVel = (v1*m1 + v2*m2) / (m1 + m2)
    v1f = comVel - (v1 - comVel)
    v2f = comVel - (v2 - comVel)
    return v1f, v2f

#counts a number of collisions for initial conditions
def TotalCollisions(m2):
    collNum = 0 #counter for collisions
    v1 = 0
    v2 = -1
    m1 = 1
    while(v2 <= v1):
        v1, v2 = BlockCollision(v1, v2, m1, m2) #collision between blocks
        v1 = -1 * v1 #collision with wall
        collNum += 2
        #print(v1, v2)

    return collNum

n = 1000

fig, ax = plt.subplots(1,1, figsize=(8,8))

massArray = np.linspace(0, m2, n+1)
for m in massArray:
    ax.scatter(m, TotalCollisions(m))

plt.show()
    

    

