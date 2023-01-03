def prefix(string: str):
    '''
    Префикс-функция строки - это массив чисел длиной n (длина строки string),
    в котором каждый элемент - это наибольшая длина наибольшего собственного суффикса подстроки string,
    совпадающего с её префиксом.
    '''
    if not isinstance(string, str):
        return
    array = [0]*len(string)                  # формируем массив нулей с длиной string
    j = 0                                    # первый элемент
    i = 1                                    # второй элемент
    while i < len(string):
        if string[j] == string[i]:           # если элементы строки равны
            array[i] = j+1                   # присваеваем элементу массива с индексом i  знач. текущего J+1
            i += 1                           # идем на следующий эл. (второй и тд)
            j += 1                           # идем на следующий эл. (третий и тд)
        else:                                # если элементы не равны
            if j == 0:                       # и сравнение идет с первым эл.
                array[i] = 0                 # присваеваем элементу массива с индексом i знач. 0
                i += 1                       # идем на следующий эл.
            else:                            # если сраниваем не с первым эл.
                j = array[j-1]               # берем предыдуший и сравниваем заново
    return array


def kmp_substring_search(string: str, substring: str):
    ''' Алгоритм Кнута - Морриса - Пратта, осуществляющий поиск подстроки в строке, используя префикс-функцию.
        О(длина строки + длина подстроки)
    '''
    if not isinstance(string, str) or not isinstance(substring, str):
        return 'Строка и подстрока должны относиться к типу данных String'

    string_len = len(string)
    substring_len = len(substring)

    if substring_len > string_len or string_len == 0 or substring_len == 0:
        return 'Совпадений нет'

    array = prefix(substring)                    # получаем массив
    i = 0                                        # элемент строки
    j = 0                                        # элемент подстроки

    while i < string_len:                        # пока не дошли до конца строки
        if string[i] == substring[j]:            # если символы строки и подстроки равны
            i += 1                               # берем следующие символы
            j += 1
            if j == substring_len:               # если нашли все символы подстроки ОК
                index = i - substring_len
                return f'Совпадение найдено, вхождение начинается с индекса {index}'
        else:                                    # если символы строки и подстроки не равны
            if j > 0:                            # и мы находимся не на первом элементе подстроки
                j = array[j-1]                   # смещаемся на элемент подстроки с индесом, равным значению предыдушего элемента префикс-массива
            else:                                # а если находимся на первом элементе подстроки
                i += 1                           # идем дальше по строке

    return 'Совпадений нет'


print(kmp_substring_search(string='ggabc', substring='abc'))  # Совпадение найдено, вхождение начинается с индекса 2
print(kmp_substring_search(string='', substring=''))  # Совпадений нет
print(kmp_substring_search(string=8, substring=''))   # Строка и подстрока должны относиться к типу данных String
print(kmp_substring_search(string='kkllggsfdhfjhjhhhhhfj', substring='abc'))  # Совпадений нет
print(kmp_substring_search(string='knut morris pratt algorithm', substring=' algor'))  # Совпадение найдено, вхождение начинается с индекса 17

# flake8 --max-line-length 150  algorithms/kmp_alg.py
