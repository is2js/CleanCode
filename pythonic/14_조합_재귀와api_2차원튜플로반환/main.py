import itertools
import sys

input = sys.stdin.readline


def combination(lst, count=None,
                select_count=0, position=0, result=()):
    # 초기 설정
    count = len(lst) if not count else count
    if select_count == 0:
        lst = sorted(lst)

    # (1) 종착역
    if select_count == count:
        return result
    # (2) 종착역2- 조합에만 있으며, 선택X만 타고가서 count를 못채우는 경우
    if position >= len(lst):
        return None

    # (3) root node 2개이며, 매 2개의 case(현재position의 element 선택O/X)로 뻗어간다.
    # (3-1) 현재position의 element를 뽑는 경우 -> result에 반영한다.
    # => (4) 2개의 case마다 종착역에서 올라오는데 None이 아닐 경우만 누적한다.
    total_result = ()
    result_select = \
        combination(lst, count,
                    select_count + 1, position + 1, tuple(result + (lst[position],)))

    # (3-2) 현재position의 element를 안뽑는 경우 -> select_count 및 result에 반영안하고 position만 넘긴다.
    result_unselect = \
        combination(lst, count,
                    select_count, position + 1, tuple(result))

    for temp_result in [result_select, result_unselect]:
        # -> 종착역이 None인 경우에는 아예 집계를 안한다.
        if not temp_result:
            continue
        # -> 넘어온 것이 종착역에서는 1차원 tuple이지만, 그 이후로는 append된 2차원이다.
        #    고려해서 1차원일때는 그냥 append, 2차원일때는, 개별요소들을 append한다.
        is_1d = all(not isinstance(x, tuple) for x in temp_result)
        if is_1d:
            # 2차원튜플append는 += ( , )1개라도 튜플을 만들어서 더하여, 쌓인 튜플이 extends되게 한다
            total_result += (temp_result, )
        else:
            for tuple_ in temp_result:
                total_result += (tuple_, )

    return total_result


if __name__ == '__main__':
    ## 조합 재귀
    lst = [1, 2, 3]
    ## not pythonic
    # 1. 조합 재귀
    # -> index(position)로 선택해서 탐색해나가므로 used_bit가 필요없다.
    # -> 첫 재귀가 helper로서 내부에서 index순서대로 선택O / 선택X 재귀 2개의 case로 뻗어나간다
    # -> stack결정변수 뽑힌 갯수 select_count와 position(순열used_bit) 및 뽑는원소를 모으는 result가 필수 default값이다.
    print(combination(lst, count=2))  # select_count=0, position=0, result
    print(combination(lst))
    print(combination("ABC", count=2))
    # (('A', 'B'), ('A', 'C'), ('B', 'C'))
    print(tuple(map(''.join, combination("ABC", count=2))))
    # ('AB', 'AC', 'BC')


    ## pythonic
    print(tuple(map(''.join, itertools.combinations(list('ABC'), 2))))
