import math
import numpy as np
import random
unlocked = np.zeros((12))
notAll = True
boxesOpened = 0
while(notAll):
    print(unlocked)
    b = input("how many boxes to open: ")
    for i in range(int(b)):
        rand = random.randint(1,12)
        print("box with " + str(rand))

        unlocked[rand - 1] += 1
        boxesOpened += 1

        if np.all(unlocked != 0):
            notAll = False
            break
    print("Boxes so far: " + str(boxesOpened))

print("It took: " + str(boxesOpened) + " boxes")
print(unlocked)
        
    

            
