import itertools
import sys
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 2개이상의 iterable의 나열(곱집합)
    iterable1 = 'ABCD'
    iterable2 = 'xy'
    iterable3 = '1234'

    ## not pythonic
    # -> 개별 iterable마다 for를 돌려, 1개씩 접근해야하므로 3중 반복문이 발생한다.
    # for value1 in iterable1:
    #     for value2 in iterable2:
    #         for value3 in iterable3:
    #             print(value1, value2, value3)

    ## pythonic : 2개이상의배열의 나열(조합, 집합, 자리 상관없이 등장만 요구됨)
    # -> itertools product로 2개이상배열의 곱집합을 뽑을 수 있다.
    # print(itertools.product(iterable1, iterable2, iterable3))
    print(list(itertools.product(iterable1, iterable2, iterable3)))
    # [('A', 'x', '1'), ('A', 'x', '2'), ('A', 'x', '3'), ('A', 'x', '4'), ('A', 'y', '1'), ('A', 'y', '2'), ('A', 'y', '3'), ('A', 'y', '4'), ('B', 'x', '1'), ('B', 'x', '2'), ('B', 'x', '3'), ('B', 'x', '4'), ('B', 'y', '1'), ('B', 'y', '2'), ('B', 'y', '3'), ('B', 'y', '4'), ('C', 'x', '1'), ('C', 'x', '2'), ('C', 'x', '3'), ('C', 'x', '4'), ('C', 'y', '1'), ('C', 'y', '2'), ('C', 'y', '3'), ('C', 'y', '4'), ('D', 'x', '1'), ('D', 'x', '2'), ('D', 'x', '3'), ('D', 'x', '4'), ('D', 'y', '1'), ('D', 'y', '2'), ('D', 'y', '3'), ('D', 'y', '4')]
    # => 결과는 list(zip())처럼 튜플 리스트로 나온다.



