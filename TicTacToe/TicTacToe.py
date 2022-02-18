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
