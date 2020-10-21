import sys

size = 501
def print_square(square):
    print("-"*(4*size))
    for y in range(len(square)):
        for x in range(len(square[y])):
            print("{:6}".format(square[x][y]), end="")
        print()
    print("-"*(4*size))
square = [[f"{x}.{y}" for x in range(size)] for y in range(size)]
###print_square(square)
def equation(j):
    i = (j-1)/2
    n = (3+2*i*(8*i*i+15*i+13))/3
    return n
def answer():
    xrange = equation(501)
    print(xrange)
answer()