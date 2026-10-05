import numpy as np
import matplotlib  
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


def format_axis(axs, axs_label=None, xlabelpad=-5):
	i = 0
	if axs_label is None:
		axs_label = ["Отсчеты", "Амплитуда"]

	if len(axs_label)==1:
		axs_label.append("Амплитуда")		
		
	for ax in axs:
		ax.grid(True) 
		ax.spines['left'].set_position(('data', 0))
		ax.spines['bottom'].set_position(('data', 0))
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		ax.xaxis.set_ticks_position('bottom')
		ax.yaxis.set_ticks_position('left')
		
		ax.set_xlabel(axs_label[0], labelpad=xlabelpad)
		ax.set_ylabel(axs_label[1], labelpad=10)
		
		#Отрисовка подписей по оси x
		for tick in ax.get_xticklabels():
			tick.set_bbox(dict(facecolor='white', edgecolor='none', pad=1))
			
		#Отрисовка подписей по оси y
		for tick in ax.get_yticklabels():
			tick.set_bbox(dict(facecolor='white', edgecolor='none', pad=1))
		i += 1

y = [ 2, 4, 8, 6, 2, -1, -2, 0]

Y = fftshift(fft(y, 512))

#Дискретная последовательность и спектры
plt.figure('Спектр дискретной последовательности')
format_axis([plt.subplot(2, 2, 1)], xlabelpad=10)
plt.title('Сигнал')
plt.stem(y)

Y_abs = np.abs(Y)
Y_angle = np.angle(Y)

format_axis([plt.subplot(2, 2, 2)], xlabelpad=-35)
plt.title('Амплитудный спектр')
plt.plot(Y_abs)

format_axis([plt.subplot(2, 2, 3)],  xlabelpad=25)
plt.title('Фазовый спектр')
plt.plot(Y_angle)

Y_r = np.real(Y)
Y_i = np.imag(Y)

format_axis([plt.subplot(2, 2, 4)], xlabelpad=45)
plt.title('Действительная и Мнимая часть спектра')
plt.plot(Y_r)
plt.plot(Y_i)

#Спектр гармонического сигнала
col = 3
line = 4
def harmonic_plot(Ampl, cell, level, symmetry=0, title_en=0, axs_label_en = 0):
	X = [0]*64
	j = 0
	for i in Ampl: 
		X[i] = level[j]
		if(symmetry):
			X[i] = level[j]/2.0
			X[-i] = level[j]/2.0
		j+=1
		
	x = [s*64 for s in ifft(X)]
    
	X_r_min = min(np.real(X))
	X_r_max = max(np.real(X))

	x_label = ''
	if(axs_label_en):
		x_label = 'Отсчеты'
	
	format_axis([plt.subplot(line, col, cell)], [x_label, 'Амплитуда'], xlabelpad=10)
	if(title_en):
		plt.title('Спектр')
	plt.stem(X)
	plt.legend(['Част.='+str(X.index(X_r_max))])

	x_r = np.real(x)
	x_i = np.imag(x)
	#print(x_i)

	format_axis([plt.subplot(line, col, cell+1)], [x_label, ''], xlabelpad=35)
	if(title_en):
		plt.title('Действительная часть (cos)')
	plt.plot(x_r, marker='o', linestyle='-')

	format_axis([plt.subplot(line, col, cell+2)], [x_label, ''], xlabelpad=35)
	plt.subplot(line, col, cell+2).set_ylim(-1.1, 1.1)
	if(title_en):
		plt.title('Мнимая часть (sin)')
		
	plt.plot(x_i, marker='o', linestyle='-')
	
plt.figure('Гармоники')
harmonic_plot([0], 1, [1], title_en=1)
harmonic_plot([2], 4, [1])
harmonic_plot([6], 7, [1])
harmonic_plot([10], 10, [1], axs_label_en=1)

plt.figure('Гармоники симметричные')
harmonic_plot([0], 1, [1], symmetry=1, title_en=1)
harmonic_plot([2], 4, [1], symmetry=1)
harmonic_plot([6], 7, [1], symmetry=1)
harmonic_plot([10], 10, [1], symmetry=1, axs_label_en=1)


#Спектр суммы гармонических сигналов
y = []
N = 128
for i in range(0, N, 1):
	y.append(1+4*np.cos(2*math.pi*i/N)+7*np.cos(2*math.pi*i*6/N)+2*np.cos(2*math.pi*i*10/N))
	
plt.figure('Сумма гармоник')
format_axis([plt.subplot(2, 1, 1)])
plt.title('Сигнал')
plt.stem(y)

Y = [s/N for s in fft(y)]
Y_abs = np.abs(Y)

format_axis([plt.subplot(2, 1, 2)])
plt.title('Спектр')
plt.stem(Y_abs)

#Спектр суммы гармонических сигналов не целое число периодов гармоник
y.append(0)
plt.figure('Сумма гармоник, не целое')
format_axis([plt.subplot(2, 1, 1)])
plt.title('Сигнал')
plt.stem(y)

Y = [s/N for s in fft(y)]
Y_abs = np.abs(Y)

format_axis([plt.subplot(2, 1, 2)])
plt.title('Спектр')
plt.stem(Y_abs)

#вывод графиков
plt.show()