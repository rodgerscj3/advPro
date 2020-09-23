import sys

def add_them_all(filename):
    sum = 0
    ### Your code here
    f = open("a.txt", "r")
    contents = a.readlines()
    for line in content:
        for j in line:
            if j.isdigit() == True:
                sum += int(j)
    ### End of your code
    return sum

if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))