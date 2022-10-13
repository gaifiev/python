# Создайте программу для игры в ""Крестики-нолики"".

# def check(arr):
#     pass


# arr = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# for i in range(9):
#     if i % 2 == 0:
#         step = 'X'
#         print('Ход крестика')
#     else:
#         step = '0'
#         print('Ход нолика')
#     row = int(input('Введите номер строки: '))
#     columns = int(input('Введите номер столбца: '))
#     if arr[row - 1][columns - 1] == '*':
#         print('Закрашено')
#     else:
#         arr[row - 1][columns - 1] = step
#     result = check(arr)
#     if result == 'X':
#         print('XXX')
#     elif result == '0':
#         print('000')
#     elif i == 9 or result == '-':
#         print('---')
board = list(range(1, 10))


def plank(board):

    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")


def tactic(hod):
    valid = False
    while not valid:
        otvet = input(
            "Выберите число: " + hod+"? ")
        otv = int(otvet)
        if otv >= 1 and otv <= 9:
            if (str(board[otv-1]) not in "XO"):
                board[otv-1] = hod
                valid = True
            else:
                print("Как ты смеешь?")


def question(board):
    pobeda = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
              (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for x in pobeda:
        if board[x[0]] == board[x[1]] == board[x[2]]:
            return board[x[0]]
    return False


def game(board):
    count = 0
    win = False
    while not win:
        plank(board)
        if count % 2 == 0:
            tactic("X - ")
        else:
            tactic("O - ")
        count += 1
        if count > 4:
            m = question(board)
            if m:
                print(m, "win")
                win = True
                break
        if count == 9:
            print("draw")
            break
    plank(board)


game(board)
