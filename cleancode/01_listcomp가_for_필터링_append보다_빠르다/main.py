def loop():
    arr = [1, 2, 3, 4]

    result = []
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            result.append(arr[i])

    print(result)


def compl():
    arr = [1, 2, 3, 4]

    print([x for x in arr if x % 2 == 1])


if __name__ == "__main__":
    loop()
    compl()
