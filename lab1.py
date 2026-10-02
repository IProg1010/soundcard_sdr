import numpy as np
import matplotlib  
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import math
import matplotlib.ticker as ticker


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

def plt_str(s, *args, **kwargs):
	markerline, stemlines, baseline = plt.stem(s[0], s[1], **kwargs)
	plt.grid(True)
	plt.xlim(args[0], args[1])  # Лимииты по оси X
	plt.ylim(args[2], args[3])  # Лимииты по оси Y
	if args[4] != 0:
		plt.setp(stemlines, color=args[5], visible=True)
	else:
		plt.setp(stemlines, visible=False)

	

print("Введите шаг дискретизации от (0;1)")
d_step = float(input())

#Функция получения сигнала по заданной формуле
#возвращает 2 списка (значения времени и сигнала) 
#аргументы 	d_step - шаг изменения времени, 
#			start_time - начало отсчета времени, 
#			stop_time - конец отсчета времени
def sig_generate(d_step, start_time, stop_time):
	x = np.linspace(start_time, stop_time, int((stop_time-start_time)/d_step))
	y = []
	for t in x:
		y.append(np.sin(math.pi*t)+np.cos(2*math.pi*t)+np.sin(4*math.pi*t)+np.sin(6*math.pi*t+1))

	return x, y

x, y = sig_generate(d_step, 0, 2)

#Построение аналового, дискретного, квантованного сигнала
plt.figure('3 типа сигналов')

plt.subplot(1, 3, 1) 
plt.title('Аналоговый')
plt.plot(x, y)
plt.tight_layout(pad=0.0) 

plt.subplot(1, 3, 2)
plt.title('Дискретный')
plt.tight_layout(pad=0.1)
s = [x, y]
plt_str(s, 0, 2, -3, 3, 1, 'blue')

plt.subplot(1, 3, 3)
plt.title('Квантованный')
plt.tight_layout(pad=0.1)
plt.step(x , y, '-', where='post')

#функция форматирования осей графиков
#аргументы: 		axs - список осей,
#			(необ.)	x_step - список шаг сетки по оси x. (по умолчанию 0.1)
#			(необ.)	y_step - список шаг сетки по оси y (по умолчанию 0.5).
#			(необ.)	axs_label - список подписей осей.
#			(необ.)	limits - список пределов по осям [xmin, xmax, ymin, ymax].
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

format_axis(plt.gcf().axes, [0.3], [0.5], limits=[0, max(x)+0.6, min(y)-0.1, max(y)+0.1]) #форматирование осей

#Построение цифрового сигнала
plt.figure('Цифровой сигнал')
plt.title('Цифровой')

plt.stem(x, y)
plt.step(x , y, where='post')

format_axis(plt.gcf().axes, [0.2], [0.5], limits=[0, max(x)+0.6, min(y)-0.1, max(y)+0.1])#форматирование осей


x, y = sig_generate(d_step, 0, 1)

#функция формирования значений и графиков при различных точках дискрет.
#аргументы: 	point_count - количество точек
# 				max_time - 
# 				plot_number - номер графика
#				s - список из 2-х списков (время и сигнал) 
def discretization(point_count, max_time, plot_number, s):
	y_d = []
	x_d = []
	
	x_d, y_d = sig_generate(max_time/point_count, 0, max_time)

	
	plt.subplot(col, line, plot_number)
	
	plt.title('Колич. точек:'+str(point_count))
	
	plt.plot(s[0] , s[1])
	
	plt_str([x_d,y_d], 0, 2, -3, 3, 0, 'blue', markerfmt='rD')
	plt.step(x_d , y_d, '-', where='post')
	plt.plot(x_d , y_d)

	return x_d, y_d;

#Построение различных шагов дискретизации
plt.figure('Разлиные шаги дискретизации')
col = 2 
line = 2

discretization(2, 1, 1, [x, y])
discretization(10, 1, 2, [x, y])
discretization(16, 1, 3, [x, y])
discretization(56, 1, 4, [x, y])

format_axis(plt.gcf().axes, [0.2], [0.5], limits=[0, max(x)+0.1, min(y)-0.1, max(y)+0.1])#форматирование осей

#Построение 13 точек на секунду согласно теореме Котельникова
plt.figure('Количество точек дискретизации равно 13')
col = 1 
line = 1
discretization(13, 1, 1, [x, y])

plt.title("Оптимальное количество точек по т. Котельникова")
format_axis([plt.subplot()], limits=[0, max(x)+0.1, min(y)-0.1, max(y)+0.1])#форматирование осей

#Построение дискретной последовательности
plt.figure('Дискретная последовательность')
y = y +[0]*50

plt.title("Дискретная последовательность")
plt.stem(y)
format_axis([plt.subplot()], [10], [0.5], ["Отcчеты"], limits=[0, len(y), min(y)-0.1, max(y)+0.1])#форматирование осей

#Построение единичного импульса и скачка

plt.figure('Единичный импульс и скачок')
point_count = 16
dirak_func = np.zeros(point_count)
dirak_arg = range(int(-(point_count/2)), int((point_count/2)), 1)
dirak_func[int(point_count/2)] = 1

plt.subplot(1, 2, 1)
plt.title("Единичный импульс")
plt.stem(dirak_arg, dirak_func, markerfmt='rD')

heaviside_func = np.heaviside(range(int(-(point_count/2)), int((point_count/2)), 1), 1)
heaviside_arg = range(int(-(point_count/2)), int((point_count/2)), 1)

plt.subplot(1, 2, 2)
plt.title("Единичный скачок")
plt.stem(heaviside_arg, heaviside_func, markerfmt='rD')

format_axis(plt.gcf().axes, [1], [0.5], ["Отcчеты"], limits=[-point_count/2, point_count/2, -0.1, 1.5])#форматирование осей

plt.show()

