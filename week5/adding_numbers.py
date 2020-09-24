import sys

def add_them_all(filename):
    sum = 0
    ### Your code here
    afile = open("a.txt", "r")
    for line in afile:
        sum += int(line)
    afile.close    
    ### End of your code
    print(sum)

if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))
