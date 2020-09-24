import sys

def add_them_all(filename):
    sum = 0
    ### Your code here
    with open("a.txt", "r") as afile, open("b.txt","r") as bfile, open("c.txt", "r") as cfile, open("d.txt", "r") as dfile, open("e.txt", "r") as efile:
        contents = afile.readlines()
    for line in afile, bfile, cfile, dfile, efile:
        sum += int(line)
    ### End of your code
    return sum

if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))
