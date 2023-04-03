alph_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
alph_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alph_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

def shifr_ru():
    s = []
    t = input('Введите текcт для шиврования: ')
    for i in range(len(list(t))):
        if t[i] in alph_ru:
            o = alph_ru.find(t[i])
            s.append(alph_ru[o+int(c)])
        elif t[i] in alph_RU:
            o = alph_RU.find(t[i])
            s.append(alph_RU[o+int(c)])
        else:
            s.append(t[i])
    return ''.join(s)

def de_shifr_ru():
    s = []
    t = input('Введите текcт для дешиврования: ')
    for i in range(len(list(t))):
        if t[i] in alph_ru:
            o = alph_ru.rfind(t[i])
            s.append(alph_ru[o - int(c)])
        elif t[i] in alph_RU:
            o = alph_RU.rfind(t[i])
            s.append(alph_RU[o - int(c)])
        else:
            s.append(t[i])
    return ''.join(s)

def shifr_en():
    s = []
    t = input('Enter the encryption text: ')
    for i in range(len(list(t))):
        if t[i] in alph_en:
            o = alph_en.find(t[i])
            s.append(alph_en[o + int(c)])
        elif t[i] in alph_EN:
            o = alph_EN.find(t[i])
            s.append(alph_EN[o + int(c)])
        else:
            s.append(t[i])
    return ''.join(s)

def de_shifr_en():
    s = []
    t = input('Enter the decryption text: ')
    for i in range(len(list(t))):
        if t[i] in alph_en:
            o = alph_en.rfind(t[i])
            s.append(alph_en[o - int(c)])
        elif t[i] in alph_EN:
            o = alph_EN.rfind(t[i])
            s.append(alph_EN[o - int(c)])
        else:
            s.append(t[i])
    return ''.join(s)

def ceaser_shifr():
    if a == 'ru':
        if b == 'ш':
            return shifr_ru()
        elif b == 'де':
            return de_shifr_ru()
        else:
            print('Невалидные значения!')
    elif a == 'en':
        if b == 'sh':
            return shifr_en()
        elif b == 'de':
            return de_shifr_en()
        else:
            print('Not valid data!')
    else:
        return 'Введите валидные значения при выборе языка!'


while True:
    a = input('Язык алфавита (ru/en): ')
    b = input('Выберите направление (шифрование - ш, sh) или (дешифрование - де, de): ')
    c = input('Шаг сдвига (целое число): ')
    print(ceaser_shifr())
    print('Попробуем ещё?')