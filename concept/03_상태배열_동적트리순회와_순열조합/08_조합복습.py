def combination(arr, r):
    arr = sorted(arr)
    result = []

    def helper(chosen):
        if len(chosen) == r:
            print(chosen)
            result.append(chosen[:])
            return

        start_index = arr.index(chosen[-1]) + 1 if chosen else 0
        end_index = len(arr)
        for index in range(start_index, end_index):
            chosen.append(arr[index])
            helper(chosen)
            chosen.pop()

    helper([])

    return result


def solution():
    combination([1, 2, 3], 2)


if __name__ == '__main__':
    solution()
