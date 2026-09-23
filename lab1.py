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

#Построение аналового, дискретного, квантованного сигнала
plt.figure('3 типа сигналов')
plt.subplot(1, 3, 1)
plt.title('Аналоговый')
plt.plot(x , y)

plt.subplot(1, 3, 2)
plt.title('Дискретный')
plt.stem(x , y, '*')

plt.subplot(1, 3, 3)
plt.title('Квантованный')
plt.step(x , y, '-', where='post')


#Построение цифрового сигнала
plt.figure('Цифровой сигнал')
plt.subplot(1, 1, 1)
plt.title('Цифровой')
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
	
	plt.title('Колич. точек:'+str(point_count))
	#plt.stem(x_d , y_d, '')

	markerline, stemlines, baseline = plt.stem(x_d, y_d)
	plt.setp(stemlines, visible=False)

	plt.step(x_d , y_d, '-', where='post')
	plt.plot(x_d , y_d)
	return x_d, y_d;

#Построение различных точек дискретизации
plt.figure('Количество точек дискретизации')

discretization(2, 1, x, y)
discretization(10, 2, x, y)
discretization(16, 3, x, y)
discretization(56, 4, x, y)

#Построение дискретной последовательности
plt.figure('дискретная последовательность')
plt.subplot(1, 1, 1)
plt.stem(y)

#Построение единичного импульса и скачка
plt.figure('Единичный импульс и скачок')
point_count = 16
dirak_func = np.zeros(point_count)
dirak_arg = range(int(-(point_count/2)), int((point_count/2)), 1)

plt.subplot(1, 2, 1)
plt.stem(dirak_arg, dirak_func)

heaviside_func = np.zeros(15)
heaviside_func = np.heaviside(heaviside_func, 2)
plt.subplot(1, 2, 2)
plt.stem(heaviside_func)


plt.show()

