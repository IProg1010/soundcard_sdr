import numpy as np
import matplotlib.pyplot as plt
import math

print("Введите шаг дискретизации от (0;1)")
d_step = float(input())


x = np.linspace(0, 1, 1/d_step)
#x = np.linspace(0, 1, 25)
y = []
for t in x:
	y.append(np.sin(math.pi*t)+np.cos(2*math.pi*t)+np.sin(4*math.pi*t)+np.sin(6*math.pi*t+1))

plt.subplot(1, 3, 1)
plt.plot(x , y)

plt.subplot(1, 3, 2)
plt.stem(x , y, '*')

plt.subplot(1, 3, 3)
plt.step(x , y, '-')

plt.show()
plt.grid()