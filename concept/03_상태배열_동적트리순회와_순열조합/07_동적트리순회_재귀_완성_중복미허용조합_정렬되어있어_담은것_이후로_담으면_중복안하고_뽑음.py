def combination(arr, r):
    arr = sorted(arr)
    result = []

    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            result.append(chosen[:])
            return

        # 1. depth가 깊어짐에 따라
        #   [ 어차피 정렬된 arr순서대로 순회를 할 것이므로 ]
        #   [ chosen된 직전인자 chosen[-1]이후부터 돌아야한다 ]
        #   [ chosen[-1]의 index를 찾고 -> 그 이후인 +1 한 것을 start_index로]
        #   [ 자식들을 순회하게 하면 된다 ]
        #   [ 직전을 찾는다면, 최초의 것에 대해 예외처리를 해줘야한다 ]
        #   [ 삼항연산자를 활용해서, 최초의 순회 == chosen이 빈상태]면 0이 start_index가 되도록 한다.

        #for index in range(len(arr)):
        #start_index = arr.index(chosen[-1]) + 1
        start_index = arr.index(chosen[-1]) + 1 if chosen else 0
        for index in range(start_index, len(arr)):
            chosen.append(arr[index])
            generate(chosen)
            chosen.pop()

    generate([])

    return result


def solution():
    print(combination([1, 2, 3,4 ], 3))
    pass


if __name__ == "__main__":
    solution()
