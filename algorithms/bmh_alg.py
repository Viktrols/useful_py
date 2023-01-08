def get_offset_table(substring: str):
    substring_len = len(substring)
    unique_symbols = set()                                    # уникальные символы в образе
    offset_dict = {}                                          # словарь смещений

    for i in range(substring_len-2, -1, -1):                  # итерации с предпоследнего символа
        if substring[i] not in unique_symbols:                # если символ еще не добавлен в множество уникальных символов
            offset_dict[substring[i]] = substring_len-i-1     # добавляем его в словарь смещений
            unique_symbols.add(substring[i])                  # и в множество уникальных символов

    if substring[substring_len-1] not in unique_symbols:      # отдельно формируем последний символ равный длине строки
        offset_dict[substring[substring_len-1]] = substring_len

    offset_dict['another'] = substring_len                    # смещения для прочих символов

    return offset_dict


def bmh_substring_search(string: str, substring: str):
    '''
        Алгоритм поиска подстроки Бойера-Мура-Хорспула.
        Сначала строится таблица смещений для каждого символа.
        Затем исходная строка и шаблон совмещаются по началу, сравнение ведется по последнему символу.
        Если последние символы совпадают, то сравнение идет по предпоследнему символу и так далее.
        Если же символы не совпали, то шаблон смещается вправо,
        на число позиций взятое из таблицы смещений для символа из исходной строки,
        и тогда снова сравниваются последние символы исходной строки и шаблона и так далее.
    '''
    if not isinstance(string, str) or not isinstance(substring, str):
        return 'Строка и подстрока должны относиться к типу данных String'

    string_len = len(string)
    substring_len = len(substring)

    if substring_len > string_len or string_len == 0 or substring_len == 0:
        return 'Совпадений нет'

    offset_dict = get_offset_table(substring)     # формирование таблицы смещений
    i = substring_len-1                           # счетчик проверяемого символа в строке
    while i < string_len:
        k = 0
        flBreak = False
        for j in range(substring_len-1, -1, -1):
            if string[i-k] != substring[j]:
                if j == substring_len-1:
                    offset = offset_dict[string[i]] if offset_dict.get(string[i], False) else offset_dict['another']  # смещение, если не равен последний символ образа
                else:
                    offset = offset_dict[substring[j]]   # смещение, если не равен не последний символ образа

                i += offset      # смещение счетчика строки
                flBreak = True
                break

            k += 1          # смещение для сравниваемого символа в строке

        if not flBreak:          # если дошли до начала образа, значит все его символы совпали
            return f'Подстрока найдена, вхождение начинается с индекса {i-k+1}'
    else:
        return 'Совпадений нет'


print(bmh_substring_search('somelonglong&$strinGstring', 'string'))  # Подстрока найдена, вхождение начинается с индекса 20
print(bmh_substring_search('', 'string'))  # Совпадений нет
print(bmh_substring_search('hh', ''))  # Совпадений нет
print(bmh_substring_search('somelonglong&$strinGstring', 'abc'))  # Совпадений нет
print(bmh_substring_search('123456789', '78'))  # Подстрока найдена, вхождение начинается с индекса 6

# flake8 --max-line-length 170  algorithms/bmh_alg.py
