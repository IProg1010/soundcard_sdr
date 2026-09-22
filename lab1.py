import numpy as np
import matplotlib  
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import math

print("Введите шаг дискретизации от (0;1)")
d_step = float(input())


x = np.linspace(0, 1, int(1/d_step))
#x = np.linspace(0, 1, 25)
y = []
for t in x:
	y.append(np.sin(math.pi*t)+np.cos(2*math.pi*t)+np.sin(4*math.pi*t)+np.sin(6*math.pi*t+1))


plt.figure('1')
plt.subplot(1, 3, 1)
plt.title('Аналоговый')
plt.plot(x , y)

plt.subplot(1, 3, 2)
plt.title('Дискретезированный')
plt.stem(x , y, '*')

plt.subplot(1, 3, 3)
plt.title('Квантованный')
plt.step(x , y, '-', where='post')

plt.figure('2')
plt.subplot(1, 1, 1)
plt.title('дискретный')
#plt.stem(x , y, '')

markerline, stemlines, baseline = plt.stem(x, y)

plt.setp(stemlines, visible=False)

plt.step(x , y, ':', where='post')
#plt.show()

def discretization(point_count, plot_number, x, y):
	y_d = []
	x_d = []
	for i in range(0, len(x), int(len(x)/point_count)):
		y_d.append(y[i])
		x_d.append(x[i])
	
	plt.subplot(2, 2, plot_number)
	plt.plot(x , y)
	plt.title('дискретный')
	#plt.stem(x_d , y_d, '')

	markerline, stemlines, baseline = plt.stem(x_d, y_d)

	plt.setp(stemlines, visible=False)

	plt.step(x_d , y_d, '-', where='post')
	plt.plot(x_d , y_d)
	return x_d, y_d;

plt.figure('3')
plt.subplot(2, 2, 1)
plt.title('Точек')
discretization(2, 1, x, y)
discretization(5, 2, x, y)
discretization(6, 3, x, y)
discretization(15, 4, x, y)

plt.show()