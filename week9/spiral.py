import sys

size = 5

def print_square(square):
    print("-"*(2*size))
    for y in range(len(square)):
        for x in range(len(square[y])):
            print("{:6}".format(square[x][y]), end="")
        print()
    print("-"*(2*size))

square = [[f"{x}.{y}" for x in range(size)] for y in range(size)]

print_square(square)