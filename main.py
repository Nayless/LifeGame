import solution
import pygame as p
from pygame.locals import *

matrix_print = solution.matrix_print


refactor = solution.refactor


# inp = ''


# while True:
#     field.logic()
#     inp = input('Write command: ')
#
#     if inp == 'add':
#         q = int(input('How much cells do u want do add?: '))
#         for i in range(q):
#             x = int(input("Enter the x coord: "))-1
#             y = int(input("Enter the y coord: "))-1
#             field.create_cell(x, y)
#     if inp == 'exit':
#         break
#
#     matrix_print(refactor(field.get_field()))


# Импорты


# Константы цветов RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Создаем окно
root = p.display.set_mode((1000, 500))
field = solution.Field(root.get_width() // 20, root.get_height() // 20)


field.create_cell(3, 3)
field.create_cell(4, 4)
field.create_cell(4, 5)
field.create_cell(3, 5)
field.create_cell(2, 5)
# Основной цикл
while 1:
    # Заполняем экран белым цветом
    root.fill(WHITE)

    # Рисуем сетку
    for i in range(0 , root.get_height() // 20):
        p.draw.line(root , BLACK , (0 , i * 20) , (root.get_width() , i * 20))
    for j in range(0 , root.get_width() // 20):
        p.draw.line(root , BLACK , (j * 20 , 0) , (j * 20 , root.get_height()))
   # Нужно чтобы виндовс не думал что программа "не отвечает"
    for i in p.event.get():
        if i.type == QUIT:
            quit()
    # Проходимся по всем клеткам

    for i in range(0 , len(refactor(field.get_field()))):
        for j in range(0 , len(refactor(field.get_field())[i])):
            # print(refactor(field.get_field())[i][j],i,j)
            p.draw.rect(root, (255 * refactor(field.get_field())[i][j] % 256, 0, 0), [i * 20, j * 20, 20, 20])
    p.display.update()
    field.logic()