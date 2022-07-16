def fibonacci_loop(n):
    assert n > 0, "0이하를 입력할 수 없습니다."

    if n <= 1:
        return n

    a, b = 0, 1  # 1 2  3 5

    for _ in range(2, n + 1):
        a, b = b, (a + b)

    return b


def fibonacci_tail_recursive(n):
    return helper(n, 0, 1)


def helper(n, a, b):
    assert n > 0, "0이하를 입력할 수 없습니다."
    if n == 0:
        return 0

    if n == 1:
        return b

    return helper(n - 1, b, a + b)


##################
def cumulative_sum_loop(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


if __name__ == "__main__":
    print(fibonacci_loop(5))
    print(fibonacci_tail_recursive(1))

    print(cumulative_sum_loop(5))
