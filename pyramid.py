def get_pyramid_height():
    print("Give me a height: ")
    height = int(input())
    return height

def print_spaces(n):
    for i in range(n):
        print(" ", end="")

def print_asterisks(n):
    for i in range(n):
        print("*", end="")

def print_pyramid_row(row, pyramid_height):
    print_spaces(pyramid_height - row - 1)
    print_asterisks(row + 1)
    print()

real_height = get_pyramid_height()
for i in range(real_height):
    print_pyramid_row(i, real_height)

#   *   row = 0   asterisks = row + 1
#  **   row = 1   spaces = height - row - 1
# ***   row = 2