from random import randint

print('Добро пожаловать в числовую угадайку!')


def is_valid(count):
    w = 0
    while int(w) != a:
        #print('Введите своё число:')
        w = input('Введите своё число: ')
        if int(w) not in range(1, range_max + 1):
            print(f'А может быть все-таки введем целое число от 1 до {range_max}?')
            count += 1
        elif int(w) < a:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif int(w) > a:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1


    print('Вы угадали, поздравляем!')
    print('попыток потребовалось: ', count)

flag = True
while flag:
    count = 1
    range_max = int(input('Введите максимальный диапазон целых чисел: '))
    a = randint(1, range_max)
    is_valid(count)
    if input(f'Хотите повторить? (yes / no): ') == 'no':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        print( '''
               *   *   *    *     *       *          *
               *   *   *    *    * *      *         * *
               *****   *    *   *   *     *        *   *  
               *   *   *    *   *****     *        *****
               *   *     **     *   *     *****    *   *   
               '''
        )
        flag = False