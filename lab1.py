import numpy as np
import matplotlib  
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import math
import matplotlib.ticker as ticker

plt.rcParams['ytick.major.width'] = 2.0  # Толщина основных делений оси Y
plt.rcParams['xtick.major.width'] = 2.0  # Толщина основных делений оси X

# Длина черточек (делений), чтобы они не казались короткими при большой толщине
plt.rcParams['ytick.major.size'] = 6.0   # Длина делений оси Y
plt.rcParams['xtick.major.size'] = 6.0   # Длина делений оси X

# Толщина самой рамки графика (линий осей)
plt.rcParams['axes.linewidth'] = 2.0 
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'

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

axs = [] #список хранит оси для задания стиля
#Построение аналового, дискретного, квантованного сигнала
plt.figure('3 типа сигналов')
ax1 = plt.subplot(1, 3, 1)
axs.append(ax1)
plt.title('Аналоговый')
plt.xlabel('Время')
plt.ylabel('Амлитуда')
plt.tight_layout(pad=0.1)
plt.subplots_adjust(left=0.02) 
plt.plot(x , y)
plt.grid(True)
plt.xlim(left=0)
#plt.tight_layout(pad=0.0) 

ax1 = plt.subplot(1, 3, 2)
axs.append(ax1)
plt.title('Дискретный')
plt.xlabel('Время')
plt.ylabel('Амлитуда')
plt.tight_layout(pad=0.1)
#plt.stem(x , y, '*')
s = [x, y]
plt_str(s, 0, 2, -3, 3)
#plt.tight_layout(pad=0.0) 

ax1 = plt.subplot(1, 3, 3)
axs.append(ax1)
plt.title('Квантованный')
plt.xlabel('Время')
plt.ylabel('Амлитуда')
plt.tight_layout(pad=0.1)
plt.step(x , y, '-', where='post')
plt.grid(True)
plt.xlim(left=0)
#plt.tight_layout(pad=0.0) 

def format_axis(axs):
	for ax in axs:
		ax.spines['left'].set_position('zero')
		ax.spines['bottom'].set_position('zero')
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		ax.xaxis.set_ticks_position('bottom')
		ax.yaxis.set_ticks_position('left')
			
		# 1. Задаем шаг для оси X (например, линии сетки через каждые 0.1)
		ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
		
		# 2. Задаем шаг для оси Y (например, линии сетки через каждые 0.5)
		ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
		
		for tick in ax.get_xticklabels():
			tick.set_bbox(dict(facecolor='white', edgecolor='none', pad=1))
			
		# 2. На всякий случай делаем то же самое для оси Y
		for tick in ax.get_yticklabels():
			tick.set_bbox(dict(facecolor='white', edgecolor='none', pad=1))
format_axis(axs)
axs.clear()

#Построение цифрового сигнала
plt.figure('Цифровой сигнал')
plt.title('Цифровой')
plt.xlabel('Время')
plt.ylabel('Амлитуда')
#plt.stem(x , y, '')

plt.stem(x, y)
plt.step(x , y, where='post')

plt.xlim(left=0)
#plt.tight_layout(pad=0.0) 
plt.grid(True)
#plt.show()
format_axis([plt.subplot()])


x, y = sig_generate(d_step, 0, 1)
def discretization(point_count, plot_number, x, y):
	y_d = []
	x_d = []
	x_d, y_d = sig_generate(1.0/point_count, 0, 1)
	#for i in range(0, len(x), point_count):
	#	y_d.append(y[i])
	#	x_d.append(x[i])
	
	axs.append(plt.subplot(col, line, plot_number))
	plt.plot(x , y)
	
	plt.title('Колич. точек:'+str(point_count))
	#plt.stem(x_d , y_d, '')

	markerline, stemlines, baseline = plt.stem(x_d, y_d)
	plt.setp(stemlines, visible=False)

	plt.step(x_d , y_d, '-', where='post')
	plt.plot(x_d , y_d)
	
	plt.xlabel('Время')
	plt.ylabel('Амлитуда')
	
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

format_axis(axs)

#plt.tight_layout(pad=0.0) 


#Построение 13 точек на секунду согласно теореме Котельникова
plt.figure('Количество точек дискретизации равно 13')
col = 1 
line = 1
discretization(13, 1, x, y)

plt.title("Оптимальное количество точек по т. Котельникова")
plt.xlabel('Время')
plt.ylabel('Амлитуда')
#plt.tight_layout(pad=0.0) 
format_axis([plt.subplot()])
plt.grid(True)

#Построение дискретной последовательности
plt.figure('Дискретная последовательность')
y = y +[0]*50

plt.title("Дискретная последовательность")
plt.xlabel('Отсчеты')
plt.ylabel('Амлитуда')
plt.stem(y)
#plt.tight_layout(pad=0.0) 
format_axis([plt.subplot()])
plt.grid(True)


#Построение единичного импульса и скачка
axs.clear()
plt.figure('Единичный импульс и скачок')
point_count = 16
dirak_func = np.zeros(point_count)
dirak_arg = range(int(-(point_count/2)), int((point_count/2)), 1)
dirak_func[int(point_count/2)] = 1

axs.append(plt.subplot(1, 2, 1))
plt.title("Единичный импульс")
plt.xlabel('Отсчеты')
plt.ylabel('Амлитуда')
plt.stem(dirak_arg, dirak_func, markerfmt='rD')
#plt.tight_layout(pad=0.0) 
plt.grid(True)


heaviside_func = np.heaviside(range(int(-(point_count/2)), int((point_count/2)), 1), 1)
heaviside_arg = range(int(-(point_count/2)), int((point_count/2)), 1)

axs.append(plt.subplot(1, 2, 2))
plt.title("Единичный скачок")
plt.xlabel('Отсчеты')
plt.ylabel('Амлитуда')
plt.stem(heaviside_arg, heaviside_func, markerfmt='rD')
#plt.tight_layout(pad=0.0) 
plt.grid(True)

format_axis(axs)

plt.show()

