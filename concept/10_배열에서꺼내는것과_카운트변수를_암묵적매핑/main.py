import sys

input = sys.stdin.readline

if __name__ == '__main__':
    fold_methods = ["R", "D", "D", "R"]
    count: int = 0
    while count < 4:
        print(fold_methods[count])
        count += 1
    pass
