Num_Attributes = 0
running = True
normal = True
Array = list

def Inputing():  # Функция ввода размерности массива и создания массива введенной размерности
    global Array
    print('Введите количество сравниетельных признаков: ', end='')
    Size_Attributes = int(input())
    Array = [[1.0] * Size_Attributes for i in range(Size_Attributes)]
    return Size_Attributes


def Printing(): # Функция вывода массива
    for lists in Array:
        print(lists)


def Completion(x, y): # Функция ввода коэфицентов в таблицу и ее заполнение ими
    global Array
    print('Введите сравнительное число для ', x + 1, ' и ', y + 1, ' признаков')
    Array[x][y] = float(input())
    Array[y][x] = round(1 / Array[x][y], 2)


if __name__ == '__main__': # Основной цикл программы
    while running:
        try:
            Num = Inputing()
        except BaseException:
            continue

        for i in range(0, Num):
            for j in range(i + 1, Num):
                normal = True
                while normal:
                    try:
                        Completion(i, j)

                    except BaseException:
                        normal = True
                        continue
                    normal = False
        Printing()
