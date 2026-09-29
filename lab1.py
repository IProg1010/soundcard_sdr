import numpy as np
import matplotlib  
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import math


def plt_str(s, *args, **kwargs):
	plt.stem(s[0], s[1], **kwargs)
	plt.grid(True)
	plt.xlim(args[0], args[1])   # Ось X от 0 до 6
	plt.ylim(args[2], args[3])  # Ось Y от 0 до 40

	

print("Введите шаг дискретизации от (0;1)")
d_step = float(input())

def sig_generate(d_step, min, max):
	x = np.linspace(min, max, int((max-min)/d_step))
	#x = np.linspace(0, 1, 25)
	y = []
	for t in x:
		y.append(np.sin(math.pi*t)+np.cos(2*math.pi*t)+np.sin(4*math.pi*t)+np.sin(6*math.pi*t+1))

	return x, y

x, y = sig_generate(d_step, 0, 2)
#Построение аналового, дискретного, квантованного сигнала
plt.figure('3 типа сигналов')
plt.subplot(1, 3, 1)
plt.title('Аналоговый')
plt.plot(x , y)
plt.grid(True)

plt.subplot(1, 3, 2)
plt.title('Дискретный')
#plt.stem(x , y, '*')
s = [x, y]
plt_str(s, 0, 2, -3, 3)

plt.subplot(1, 3, 3)
plt.title('Квантованный')
plt.step(x , y, '-', where='post')
plt.grid(True)

plt.subplots_adjust(left=0.06, right=0.99, wspace=0.1)

#Построение цифрового сигнала
plt.figure('Цифровой сигнал')
plt.subplot(1, 1, 1)
plt.title('Цифровой')
#plt.stem(x , y, '')
plt.stem(x, y)
plt.step(x , y, where='post')

plt.grid(True)
#plt.show()

x, y = sig_generate(d_step, 0, 1)
def discretization(point_count, plot_number, x, y):
	y_d = []
	x_d = []
	for i in range(0, len(x), int(len(x)/point_count)):
		y_d.append(y[i])
		x_d.append(x[i])
	
	plt.subplot(col, line, plot_number)
	plt.plot(x , y)
	
	plt.title('Колич. точек:'+str(point_count))
	#plt.stem(x_d , y_d, '')

	markerline, stemlines, baseline = plt.stem(x_d, y_d)
	plt.setp(stemlines, visible=False)

	plt.step(x_d , y_d, '-', where='post')
	plt.plot(x_d , y_d)
	
	plt.grid(True)

	return x_d, y_d;

#Построение различных точек дискретизации
plt.figure('Количество точек дискретизации')
col = 2 
line = 2

discretization(2, 1, x, y)
discretization(10, 2, x, y)
discretization(16, 3, x, y)
discretization(56, 4, x, y)
plt.subplots_adjust(left=0.06, right=0.99, wspace=0.1)

plt.figure('Количество точек дискретизации равно 13')
col = 1 
line = 1
discretization(13, 1, x, y)
plt.grid(True)
plt.subplots_adjust(left=0.06, right=0.99, wspace=0.1)

#Построение дискретной последовательности
plt.figure('дискретная последовательность')
y = y +[0]*5
plt.subplot(1, 1, 1)
plt.stem(y)
plt.grid(True)


#Построение единичного импульса и скачка
plt.figure('Единичный импульс и скачок')
point_count = 16
dirak_func = np.zeros(point_count)
dirak_arg = range(int(-(point_count/2)), int((point_count/2)), 1)
dirak_func[int(point_count/2)] = 1

plt.subplot(1, 2, 1)
plt.stem(dirak_arg, dirak_func, markerfmt='rD')
plt.grid(True)


heaviside_func = np.heaviside(range(int(-(point_count/2)), int((point_count/2)), 1), 1)
heaviside_arg = range(int(-(point_count/2)), int((point_count/2)), 1)

plt.subplot(1, 2, 2)
plt.stem(heaviside_arg, heaviside_func, markerfmt='rD')
plt.grid(True)

plt.subplots_adjust(left=0.06, right=0.99, wspace=0.1)


plt.show()

