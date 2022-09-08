import itertools
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## map으로 iterable 요소들 개별convert
    # 형변환
    lst = ['1', '100', '33']
    print(list(map(int, lst)))

    # 데이터 조작: 개별원소 -> len으로 바꾸기
    lst = [[1, 2], [3, 4], [5]]
    print(list(map(len, lst)))

    # 문자열 2차원 list라면, 각 row별로 ''.join시킨 1차원 배열로 만들 수 있다.
    print(list(itertools.permutations('조재성', 3)))
    # [('조', '재', '성'), ('조', '성', '재'), ('재', '조', '성'), ('재', '성', '조'), ('성', '조', '재'), ('성', '재', '조')]
    print(list((map(''.join, itertools.permutations('조재성', 3)))))
    # ['조재성', '조성재', '재조성', '재성조', '성조재', '성재조']

