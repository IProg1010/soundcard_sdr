import numpy as np
import matplotlib  
import scipy.fft
from scipy.fft import fft, fftfreq, fftshift, ifft
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt

import math

y = [ 2, 4, 8, 6, 2, -1, -2, 0]

Y = fftshift(fft(y, 512))

#Дискретная последовательность и спектры
plt.figure('')
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
plt.title('Действ и Мнимая часть')
plt.plot(Y_r)
plt.plot(Y_i)


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