import numpy as np
import matplotlib.pyplot as plt

time = 2000

state = np.zeros(2)
orbit = np.zeros(2)
for i in range(time):
	speed = 1
	randomvec = np.random.random(2) - 0.5
	randomvec += speed/np.linalg.norm(randomvec)
	state += randomvec
	orbit = np.vstack([orbit, state])


orbit = orbit.T

plt.scatter(0, 0, color="r")
plt.plot(*orbit, lw=0.5)
plt.scatter(*state, color="r")
plt.axis("equal")
plt.show()