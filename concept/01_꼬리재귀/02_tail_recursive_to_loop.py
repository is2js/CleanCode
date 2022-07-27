def helper(n, a, b):
    if n < 0:
        raise ValueError("0이하를 입력할 수 없습니다.")

    if n == 0:
        return 0

    if n == 1:
        return b

    return helper(n - 1, b, a + b)

def loop(n):
    if n < 0:
        raise ValueError("0이하를 입력할 수 없습니다.")

    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b

    return b


#cumulative_sum_tail(5, 0)
def cumulative_sum_tail(n, result):
    if n == 0:
        return result

    return cumulative_sum_tail(n-1, result + n)

#def cumulative_sum_loop(n, result):
def cumulative_sum_loop(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result

    #return cumulative_sum_tail(n-1, result + n)



if __name__ == '__main__':
    print(helper(10, 0, 1))
    print(loop(10))

    print(cumulative_sum_tail(10, 0))
    print(cumulative_sum_loop(10))