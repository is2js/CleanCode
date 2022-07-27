import itertools


def permutation(arr, r):
    arr = sorted(arr)
    result = []

    def helper(used, chosen):
        if len(chosen) == r:
            print(chosen)
            # print(used)
            result.append(chosen[:])
            return

        for index in range(len(arr)):
            if used[index]:
                continue
            # 사용상태는 아니지만..
            # 순서상 직전껏과 같은데, 직전께 이미 사용된 경우는 넘겨야한다.
            if index != 0 and arr[index - 1] == arr[index] \
                    and not used[index - 1]:
                # 직전껏을 사용안했다면, 직전꺼부터 사용하라고 건너뛴다.
                # 직전꺼는 사용되고, 건너뛴 것은 안되니
                # 직전꺼 첫번째것만 사용된다.
                continue

            used[index] = 1
            chosen.append(arr[index])
            helper(used, chosen)
            used[index] = 0
            chosen.pop()

    helper([0 for _ in range(len(arr))], [])



def permutation_2(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            # 3.
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)


def solution():
    permutation([1,1,2,3], 2)
    print(">>>>>>>")
    # permutation_2("AABC", 2)
    # print(">>>>>>>")
    print(sorted(list(itertools.permutations([2,1, 1, 3], 2))))
    # lst = itertools.product((range(1, 3+1)), repeat=2)
    # for row in lst:
    #     print(*row)


if __name__ == '__main__':
    solution()
