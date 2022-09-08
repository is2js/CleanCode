import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## * 연산을 통한 문자열 반복
    # -> 같은 문자열의 누적합 대신 * 를활용하자.
    answer = 'abc' * 5
    print(answer)
    # abcabcabcabcabc

    # list의 *연산은 존재하는 원소들 전체를 횟수만큼 append이다
    # -> list부터는 깊은 복사를 해야하므로 해서는 안된다.
    #    listcomp로서 깊은 복사를 해야함.
    lst = [3] * 5
    print(lst)
    # [3, 3, 3, 3, 3]

    lst = [1, 2] * 5
    print(lst)
    # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
