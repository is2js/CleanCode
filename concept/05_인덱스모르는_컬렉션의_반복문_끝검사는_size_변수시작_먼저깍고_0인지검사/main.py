def solution():
    sets = [1, 2, 3, 4, 5]

    i = len(sets)
    for element in sets:
        i -= 1
        if i == 0:
            print(f"끝 > {element}")


if __name__ == '__main__':
    solution()
