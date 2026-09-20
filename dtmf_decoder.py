import numpy as np
import sounddevice as sd
import scipy.signal

# Константы DTMF
SAMPLE_RATE = 8000  # Для DTMF достаточно 8 кГц (стандарт телефонии)
CHUNK_SIZE = 400    # 400 семплов при 8кГц — это окно в 50 мс (идеально для тонов)
THRESHOLD = 0.05    # Порог громкости (подстройте под свой микрофон)

# Частотные сетки DTMF
ROW_FREQS = [697, 770, 852, 941]
COL_FREQS = [1209, 1336, 1477, 1633]

# Матрица символов
DTMF_MAP = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]
def goertzel(samples, target_freq, sample_rate):
    """
    Правильная и чистая реализация алгоритма Гёрцеля на NumPy.
    Возвращает квадрат амплитуды (энергию) целевой частоты.
    """
    N = len(samples)
    
    # Вычисляем коэффициент фильтра
    k = int(0.5 + (N * target_freq) / sample_rate)
    w = (2 * np.pi / N) * k
    cosine = np.cos(w)
    coeff = 2 * cosine
    
    # Рекурсивный фильтр (БИХ)
    s_prev = 0.0
    s_prev2 = 0.0
    
    for x in samples:
        s = x + coeff * s_prev - s_prev2
        s_prev2 = s_prev
        s_prev = s
        
    # Вычисляем финальную энергию частоты
    power = s_prev2**2 + s_prev**2 - coeff * s_prev * s_prev2
    return power


def get_dtmf_char(audio_chunk):
    # Проверяем, есть ли вообще звук (чтобы не обрабатывать тишину)
    if np.max(np.abs(audio_chunk)) < THRESHOLD:
        return None

    # Ищем доминирующую частоту в строках
    row_energies = [goertzel(audio_chunk, f, SAMPLE_RATE) for f in ROW_FREQS]
    # Ищем доминирующую частоту в столбцах
    col_energies = [goertzel(audio_chunk, f, SAMPLE_RATE) for f in COL_FREQS]

    best_row = np.argmax(row_energies)
    best_col = np.argmax(col_energies)

    # Простая валидация: энергия сигнала на этих частотах должна быть выраженной
    if row_energies[best_row] > 1.0 and col_energies[best_col] > 1.0:
        return DTMF_MAP[best_row][best_col]
    return None

# Переменные для защиты от дребезга (чтобы одна кнопка не печаталась сто раз)
last_char = None
char_counter = 0

def audio_callback(indata, frames, time, status):
    global last_char, char_counter
    if status:
        print(status)
        
    # Извлекаем одномерный массив из аудио-потока
    signal = indata[:, 0]
    
    current_char = get_dtmf_char(signal)
    
    if current_char and current_char == last_char:
        char_counter += 1
        # Если тон удерживается стабильно (например, 2 чанка подряд)
        if char_counter == 2: 
            print(current_char, end='', flush=True)
    elif current_char != last_char:
        last_char = current_char
        char_counter = 0

# Запуск потока захвата
with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, 
                     blocksize=CHUNK_SIZE, callback=audio_callback):
    print("Декодер DTMF запущен. Включите звук тонового набора в микрофон...")
    print("Нажмите Ctrl+C для выхода.")
    try:
        while True:
            sd.sleep(1000)
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")