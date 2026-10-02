import numpy as np
import matplotlib  
import scipy.fft
from scipy.fft import fft, fftfreq, fftshift, ifft
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import math


#Длина делений
plt.rcParams['ytick.major.width'] = 2.0  #Толщина основных делений оси Y
plt.rcParams['xtick.major.width'] = 2.0  #Толщина основных делений оси X

#Длина делений
plt.rcParams['ytick.major.size'] = 6.0   #Длина делений оси Y
plt.rcParams['xtick.major.size'] = 6.0   #Длина делений оси X

#Толщина линий осей
plt.rcParams['axes.linewidth'] = 2.0 
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'

y = [ 2, 4, 8, 6, 2, -1, -2, 0]

Y = fftshift(fft(y, 512))

#Дискретная последовательность и спектры
plt.figure('Спектр дискретной последовательности')
plt.subplot(2, 2, 1)
plt.title('Сигнал')
plt.stem(y)

Y_abs = np.abs(Y)
Y_angle = np.angle(Y)

plt.subplot(2, 2, 2)
plt.title('Спектр амплитуды')
plt.plot(Y_abs)

plt.subplot(2, 2, 3)
plt.title('Фазовый спектр')
plt.plot(Y_angle)

Y_r = np.real(Y)
Y_i = np.imag(Y)

plt.subplot(2, 2, 4)
plt.title('Действительная и Мнимая часть')
plt.plot(Y_r)
plt.plot(Y_i)

def format_axis(axs, x_step=None, y_step=None, axs_label=None, limits=[0,1,0,1]):
	i = 0
	if x_step is None:
		x_step = [0.1]*len(axs)
	if y_step is None:
		y_step = [0.5]*len(axs)		
		
	if len(x_step) < len(axs):
		x_step = x_step+[x_step[0]]*(len(axs)-len(x_step))
	if len(y_step) < len(axs):
		y_step = y_step+[y_step[0]]*(len(axs)-len(y_step))
	
	if axs_label is None:
		axs_label = ["Время", "Амплитуда"]

	if len(axs_label)==1:
		axs_label.append("Амплитуда")		
		
	for ax in axs:
		ax.grid(True) 
		ax.spines['bottom'].set_position('zero')
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		ax.xaxis.set_ticks_position('bottom')
		ax.yaxis.set_ticks_position('left')
		
		ax.set_xlim(limits[0], limits[1])
		ax.set_xlabel(axs_label[0], x=1.0, ha='right', labelpad=15)
		#Установка шага для оси Y (например, линии сетки через каждые x_step[i])
		ax.xaxis.set_major_locator(ticker.MultipleLocator(x_step[i]))
		
		
		#ax.set_ylabel(axs_label[1],  y=1.02, ha='center', rotation=90)
		ax.set_ylim(limits[2], limits[3])
		ax.set_ylabel(axs_label[1], labelpad=10)
		#Установка шага для оси Y (например, линии сетки через каждые y_step[i])
		ax.yaxis.set_major_locator(ticker.MultipleLocator(y_step[i]))
		
		#Отрисовка подписей по оси x
		for tick in ax.get_xticklabels():
			tick.set_bbox(dict(facecolor='white', edgecolor='none', pad=1))
			
		#Отрисовка подписей по оси y
		for tick in ax.get_yticklabels():
			tick.set_bbox(dict(facecolor='white', edgecolor='none', pad=1))
		i += 1

axs = plt.gcf().axes
format_axis([axs[1], axs[2], axs[3]], [30], [5], limits=[0, len(Y)+0.6, min(Y)-0.1, max(Y)+0.1]) #форматирование осей

#Спектр гармонического сигнала
#Функция вывода

col = 3
line = 4
def sri(k, cell, level):
	X = np.zeros(64)
	j = 0
	for i in k: 
		X[i] = level[j]
		X[-i] = level[j]
		j+=1
	x = [s*64 for s in ifft(X)]
    
	plt.subplot(line, col, cell)
	plt.title('Спектр')
	plt.stem(X)
	plt.xlabel("Отсчеты")
	plt.legend('Частота='+str(max(X)), fontsize = 'x-small', ncol=3, loc='upper center', frameon=False)

	x_r = np.real(x)
	x_i = np.imag(x)
	print(x_i)

	plt.subplot(line, col, cell+1)
	plt.title('Действительная часть')
	plt.plot(x_r, marker='o', linestyle='-')
	plt.xlabel("отсчеты")

	plt.subplot(line, col, cell+2)
	plt.title('Мнимая часть')
	plt.plot(x_i, marker='o', linestyle='-')
	plt.ylim(-1, 1)
	plt.xlabel("отсчеты")


plt.figure('Гармоники')
sri([0], 1, [1])
sri([2], 4, [1])
sri([6], 7, [1])
sri([10], 10, [1])



col = 3
line = 1
plt.figure('Сумма гармоник')
sri([0, 2, 6, 10], 1, [1, 4, 7, 2])


#Спектр суммы гармонических сигналов
y = []
N = 128
for i in range(0, N, 1):
	y.append(1+4*np.cos(2*math.pi*i/N)+7*np.cos(2*math.pi*i*6/N)+2*np.cos(2*math.pi*i*10/N))
	
plt.figure('Сумма гармоник2')
plt.subplot(2, 1, 1)
plt.title('Спектр')
plt.stem(y)
plt.xlabel("Отсчеты")
#plt.legend('Частота='+str(max(y)), fontsize = 'x-small', ncol=3, loc='upper center', frameon=False)

#Y = fftshift(fft(y))
Y = fft(y)
Y_abs = np.abs(Y)

plt.subplot(2, 1, 2)
plt.title('Спектр амплитуды')
plt.stem(Y_abs)


#вывод графиков
plt.show()