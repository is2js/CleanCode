import bisect
import sys

input = sys.stdin.readline


def bisect_recur(lst, target,
                 srt_index=None, end_index=None):
    srt_index = srt_index if srt_index else 0
    end_index = end_index if end_index else len(lst) - 1

    # (1) 탐색은 없는 경우도 따로 처리해줘야한다.
    if srt_index > end_index:
        return -1
    # (2) 이진탐색의 종착역은 mid를 만든 뒤, target의 value와 같은 mid_index를 반환한다.
    mid_index = (srt_index + end_index) // 2  # mid or mid_left
    if lst[mid_index] == target:
        return mid_index

    # (3) 자신의 처리에서, mid를 만들고 범위를 절반으로 좁혀 보낸다.
    #  -> if로 택1하되, 꼬리재귀로서 1개값을 반환하게 한다.
    if target < lst[mid_index]:
        return bisect_recur(lst, target,
                            srt_index, mid_index - 1)

    if target > lst[mid_index]:
        return bisect_recur(lst, target,
                            mid_index + 1, end_index)


def bisect_loop(lst, target,
                srt_index=0, end_index=None):
    if not end_index:
        end_index = len(lst) - 1

    # 재귀는 > 시 index탐색 실패, == 시 종착역으로 반환
    # => 반복문에서는 <= 일때까지 돌고, ==로 break >의 상황은 못찾은 것으로
    while srt_index <= end_index:
        mid_index = (srt_index + end_index) // 2
        # (1) 반복문의 [범위내 중간탐색]은 시작하자마자 if [발견시 처리] break를 건다.
        # -> 못찾으면 flag없이 else로 처리한다.
        if lst[mid_index] == target:
            return mid_index
            # flag X 발견시처리 -> break(return으로 대체)

        # (2) 발견못하면 업데이트하되 2포인터라서 경우를 나눠서한다.
        if target < lst[mid_index]:
            end_index = mid_index - 1
        else:
            srt_index = mid_index + 1
    else:
        # 다 탐색했는데도 중간탐색(구 flag)에 안걸렸다면, [미발견시처리]
        return -1


def bisect_search(lst, target):
    target_index = bisect.bisect_left(lst, target)
    # (1) 커서 index범위를 넘어가는 경우 배제 (2) 작거나 커서 삽입index일 수 도 있으니 값도 직접 확인
    if target_index < len(lst) and lst[target_index] == target:
        return target_index
    return -1


if __name__ == '__main__':
    ## 이진탐색
    # -> 이미정렬된배열을 선형탐색(N, sequence.index(), string.find())이 아닌 lgN의 이진탐색을 해야한다.
    # -> 이진탐색 구현은 lst상 target을 srt,end 투포인터로 한다.
    my_list = [1, 2, 3, 7, 9, 11, 33]
    my_string = '가나다라마바사'

    ## not pythonic
    # 1. index의 선형 탐색 (탐색은 seq의 index를 찾는 것)
    # -> index를 가진 iter(seq)의 선형탐색(seq.index(), str.find())
    print(my_list.index(3))  # 2
    print(my_string.find('다'))  # 2

    # 2. 이진taget index탐색 -> 재귀
    print(bisect_recur(my_list, 3))

    # 3. 이진target index탐색 -> 반복문
    # -> 역시나 투포인터로 한다.
    print(bisect_loop(my_list, 3))

    ## pythonic
    # 4. bisect_left()로 구현
    # -> 반환index는 insert할 제일 왼쪽index로서
    #    (1) 같다면 => 찾는 원소 맨왼쪽 위치 -> 원하는 답
    #    if 못찾았다면,
    #    (2) 작다면 => 찾는 원소 맨왼쪽 위치 -> 같아서 찾은 경우와 중복되니, 실제 같은지 확인해야한다.
    #    (3) 크다면 => 찾는 원소의 +1 오른쪽 위치 --> end_index를 넘어갈 수 있다
    # -> bisect_left(lst, target)으로 찾되, 만약 못찾는 상황에 대한 대비도 해줘야한다.
    # => (1) 더 커서 index범위를 넘어가지 않을 것 && (2)작은 경우가 아니라 실제 같은 경우(value비교)일 것
    print(bisect_search(my_list, 3))  # 2
    print(bisect_search(my_list, 5))  # -1


    def bisect_search(lst, target):
        target_index = bisect.bisect_left(lst, target)
        # (1) 커서 index범위를 넘어가는 경우 배제 (2) 작거나 커서 삽입index일 수 도 있으니 값도 직접 확인
        if target_index < len(lst) and lst[target_index] == target:
            return target_index
        return -1
