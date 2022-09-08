import itertools
import sys

input = sys.stdin.readline

if __name__ == '__main__':

    ## 2차원 list 평탄화
    lst = [[1, 2], [3, 4], [5, 6]]

    ## not pythonic
    # 1. row별로 돌면서, 각 row list들을 [빈 list] + 로 extends한다.
    # => row들을 빈행렬에 누적합(2중반복문으로 개별요소에 접근할 필요까지 없다)
    result = []
    for row in lst:
        result += row
    print(result)

    # 2. sum(, [])으로 누적초기값을 빈행렬로 하고 개별row들이 + 하게 만든다.
    print(sum(lst, [])) # => 평탄화의 sum은 매우 느리다고 한다.

    # 3. reduce + lambda가상인자2개 로 2차배열의 요소인 1차배열을 +로 누적하기
    from functools import reduce

    print(reduce(lambda x, y: x + y, lst))
    # -> lambda 누적인자2개 대신, operator 제공 함수객체 사용하기
    from operator import add
    print(reduce(add, lst))


    ## pythonic
    # 4. itertools.chain.from_iterable()에 2차원배열을 넣어준다.
    print(list(itertools.chain.from_iterable(lst)))

    # 5. itertools.chian()에 1차원 iterable(string포함)을 넣어준다.
    print(list(itertools.chain([1, 2], [3, 4], [5, 6])))
    # -> 2차원도 unpacking해서, 여러개의 1차 iterable을 넣어주면 된다.
    print(list(itertools.chain(*lst)))
    # -> 1차원 iterable 중에 string도 포함이다.
    print(list(itertools.chain('Abc', ['abc', 2, 3], '캬')))
    # ['A', 'b', 'c', 'abc', 2, 3, '캬']


