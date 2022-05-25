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


def logic(x, y, matrix):
    pass
field = solution.Field(10, 10)
# field.create_cell(5, 7)
# field.create_cell(5, 8)
# field.create_cell(6, 7)
# print(field.near(5, 9))
# matrix_print(refactor(field.get_field()))