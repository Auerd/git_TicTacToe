# крестики нолики

import random


# Функция для прорисовки игрового поля

def draw_board(board):
    # Эта функция выводит на экран игровое поле, клетки которго будт заполняться
    # "board" - это список из 10 строк, для прорисовки игрового поля(индекс интегрируется)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# Функция предоставления выбора игроку
def input_player_letter():
    # Разрешение игроку ввести букву, которую он выбирает.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы вибираете X или O?')
        letter = input().upper()
    # Первым элементом списка является буква игрока, вторым - буква компьютера
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return "Человек"


# Функция размещения меток на игровом поле
def make_move(board, letter, move):
    board[move] = letter


# Проверка - победил ли игрок
def is_winner(bo, le):
    # Учитывая заполнение игрового поля и буквы игрока, эта функция возвращет True, если игрок выиграл.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # через верх
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # через центр
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # через низ
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # вниз по левой стороне
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # вниз по центру
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # вниз по правой стороне
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # диагональ с левого верха до правого низа
            (bo[9] == le and bo[5] == le and bo[1] == le))  # диагональ с правого верха до левого низа
