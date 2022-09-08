import collections
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## for/while if 발견시 [flag] break -> 이후 flag로 if [발견처리] else [미발견처리]
    # for/while if 발견시 [바로 처리] break else로 [미발견처리]
    lst = [2, 4, 2, 5, 1]

    ## not python
    # => 누적곱 -> 지역변수 가변변수를 1로 초기화해놓고 누적곱하기
    #    or 첫번재원소부터 누적곲하기 with reduce

    # => 제곱수 판단:  루트씌운 것 vs int(루트씌운 것) 같으면 제곱수
    #    -> 나머지가 있냐/없냐, 정수냐아니냐가 를 직접 따지는 게 아니라
    #       [int 씌운것과 그냥 값이 같]으면 정수다.

    # has_squared = False
    #
    # result = 1
    # for x in lst:
    #     result *= x
    #     # 제곱수 판단(루트씌워놓고 나머지 있냐 없냐)
    #     sqrt_result = result ** (1 / 2)
    #     if sqrt_result == int(sqrt_result):
    #         has_squared = not has_squared
    #         break
    #
    # print('found' if has_squared else 'not found')

    ## pythonic
    queue = collections.deque(lst)

    product = 1
    while queue:
        curr = queue.popleft()
        product *= curr
        if product**(1/2) == int(product**(1/2)):
            ## flag처리할 곳인데 바로 처리
            print('found')
            break
    else:
        ## flag미발견시 처리
        print('not found')



