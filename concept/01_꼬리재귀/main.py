def fibonacci_loop(n):
    if n < 0:
        raise ValueError("0이하를 입력할 수 없습니다.")

    if n <= 1:
        return n

    a, b = 0, 1  # 1 2  3 5

    for _ in range(2, n + 1):
        a, b = b, (a + b)

    return b


def fibonacci_tail_recursive(n):
    return helper(n, 0, 1)


def helper(n, a, b):
    if n < 0:
        raise ValueError("0이하를 입력할 수 없습니다.")

    if n == 0:
        return 0

    if n == 1:
        return b

    return helper(n - 1, b, a + b)


#### 꼬리재귀 to 반복문
# 05 파라미터-다음인자의 업데이트로직을 다 챙겼으면,
#    꼬리재귀함수의 시그니쳐를 n만 인자로 받도록 메서드를 정의한다.
def recur_to_loop(n):
    # 06. loop를 쓰는 메서드에서도 종착역개념의 early return 존재하므로 대응하낟.
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return b
    if n <= 1:
        return n

    # 01. n을 제외한 꼬리재귀 최초호출로 넘어간 인자값들을 loop위 업뎃변수 초기값으로 가져온다
    # -> 누적결과값변수 + @
    #  a자리 0, b자리 1
    a, b = 0, 1
    # 02. n부터 [종착역 직전]까지 반복문을 돌린다.
    #     만약, 종착역이 결과값반환 전, 계산을 하는 로직이라면 종착역까지 돌린다?
    for i in range(2, n + 1):
        # 03. 파라미터 -> 다음 꼬리재귀의 인자가 어떻게 업데이트 되는지 확인해서
        #     반복문내부에서 업데이트 시킨다.
        #     이 때, 결과값만드는 부분이 먼저고, 그다음에 기타 변수 업데이트다.
        #     b <- a + b, a <- b,
        #     -> 동시성 잇슈가 있기 때문에, 튜플형태로 동시에 재할당하는 업데이트를 한다.
        a, b = b, a + b
    # 04. 재귀만큼 반복했으면 누적 결과값 변수를 반환한다.
    return b



##################
def cumulative_sum_loop(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def cumulative_sum_tail(n, result):
    if n == 0:
        return result

    return cumulative_sum_tail(n-1, result + n)


if __name__ == "__main__":
    print(fibonacci_loop(10))
    print(fibonacci_tail_recursive(1))

    print(recur_to_loop(10)) # 55

    print(cumulative_sum_loop(5))
    print(cumulative_sum_tail(5, 0))

