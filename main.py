import solution


def matrix_print(matrix):
    for line in matrix:
        print(line)


def refactor(field):
    matrix = [[] for i in range(len(field))]
    for i in range(len(field)):
        for j in range(len(field[i])):
            matrix[i].append(field[i][j].char())
    return matrix


inp = ''
field = solution.Field(10, 10)

while True:
    field.logic()
    inp = input('Write command: ')

    if inp == 'add':
        q = int(input('How much cells do u want do add?: '))
        for i in range(q):
            x = int(input("Enter the x coord: "))-1
            y = int(input("Enter the y coord: "))-1
            field.create_cell(x, y)
    if inp == 'exit':
        break

    matrix_print(refactor(field.get_field()))