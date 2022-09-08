import itertools
import sys

input = sys.stdin.readline

def permutation(lst, count=None,
                select_count=0, used_bit=0, result=[]):
    # 외부에서 kargs로 순열 구성 갯수가 주어지면 그값을, 아니라면 len(lst)를 stack결정 변수 count로 사용한다.
    count = count if count else len(lst)
    # 중복허용 안하려면, set() -> sorted() 해주면 된다.
    if select_count == 0:
        lst = sorted(lst)

    # (1) 종착역에서는 선택한 요소들을 모은, 누적결과값 변수를 반환한다.
    # -> 종착역이라도, back하면 해당node는 여러자식으로부터 []를 받게 된다.
    if select_count == count:
        return result

    total_result = []
    # (2) used_bit와 매핑관계이므로 index를 통해 구성요소를 선택한다.
    for index in range(len(lst)):
        # (3) 사용 체킹
        if used_bit & 1 << index: continue
        # (4) 사용한 것을 제외한 요소들로 N개의 node를 뻗고 반환되는 lst를 모아야한다.
        # -> 종착역에서 return하면 일반  result지만, 그 이전으로 back하면, result들이 append되어 2차원 배열이 return될 것이다.
        result_lst = permutation(lst, count,
                                 select_count + 1, used_bit | 1 << index, list(result + [lst[index]]))
        # (5) 1차원 lst가 반환된다면, 그냥 append한다.
        # -> 개별 요소롤 인덱싱이 아닌 for문으로 돌면서 개발요소가 2차원 속 1차원lst가 아닌지 판단한다.
        is_1d = all(not isinstance(x, list) for x in result_lst)
        if is_1d:
            total_result.append(result_lst)
        # (6)2차원 집계된 lst가 반환된다면, 개별요소(lst)마다 돌면서 개별append해야한다.
        # -> 최종 total_result에는, 1차 or 2차 result들이 반환되어도 -> 최종 2차로 append되게 해야한다.
        else:
            for e_lst in result_lst:
                total_result.append(e_lst)
    return total_result


if __name__ == '__main__':
    ## 순열과 조합
    # -> N개의 요소가 lst에 존재하며, 요구사항에 따라 교환법칙 성립안하면 순열 / 성립하는 경우, 조합으로 경우의 수를 나열한다.
    lst = [3, 2, 1]
    ## not pythonic -> dfs + used_bit를 사용해서, 탐색한다.
    # -> 첫 재귀호출이 root node가 아니라, 내부에서 N의 재귀호출로 N개의 node가 출발한다.

    # 1. 순열 by 재귀
    # -> 요소N개만큼의 root node로 시작하기 위해, 첫 호출은 오버로딩용 helper함수이다.
    # -> (1) 종착열을 결정짓는 변수는 선택한 요소 갯수 count=이나, 주어지지 않을 시 lst의 갯수만큼만 차지하기 위해
    #    default값으로서 숨겨져있다.
    # -> (2) used_bit도 각 탐색마다 들고다니면서 업뎃하는 필수 변수이며, 기본값 0으로 시작하므로 오버로딩 개념으로 숨겼다.
    # -> (3) global 변수 사용을 막기 위해, data인 lst를 첫번째 인자로 받는다.
    print(permutation(['ㅋ', 'ㅇ']))
    print(permutation(lst, count=2))
    print(permutation("조조조", count=3))


    ## pythonic -> permutations를 이용한다.
    print(list(itertools.permutations(lst, 2)))

    # -> 문자열은 튜플list보다는 문자열들을 join하여 1차원 문자열lst로 만든다.
    print(list(itertools.permutations('ABC', 2)))
    # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    print(list(map(''.join, itertools.permutations('ABC', 2))))





