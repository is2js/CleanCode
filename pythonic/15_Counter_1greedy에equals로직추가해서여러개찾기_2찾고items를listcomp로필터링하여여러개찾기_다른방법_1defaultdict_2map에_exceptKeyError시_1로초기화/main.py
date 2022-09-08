import collections
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## Counter : 원소 갯수 세기
    string = 'dfdefdgf'

    ## not pythonic

    # # 1. defaultdict
    # counter = collections.defaultdict(int)
    #
    # for char in string:
    #     counter[char] += 1
    #
    # # print(counter)
    # # -> max value를 찾으려면, (1) collection에서 일단 찾고, (2) 탐색하면서 그 max_count를 가진 것을 append해야한다.
    # # => 동시에 하려면 greedy로 찾으면 되는데,
    # #    max_value에 대한 mapping index(key)가 여러개가 나올 경우,
    # #   > 로 업데이트 ->  == 로 append
    # # => greedy 자체로는 1개값 업데이트만하고 모으는 것은 안되니
    # #    따로, 아래줄에 == 일 때, lst에 append해야한다.
    # max_count = float('-inf')
    # max_value_lst = []
    # for value, count in counter.items():
    #     if count > max_count:
    #         max_count = count
    #         max_value = value
    #         # max_value_lst.append(value)
    #     if count == max_count:
    #         max_value_lst.append(value)
    # print(''.join(sorted(max_value_lst)))

    # # 2. 일반 dict(map)과 Except KeyError시 1로 바로 초기화
    # # -> key가 한번도 등록되지 않은 경우, set += 1 증감시 KeyError가 나니
    # #    그 때, 0초기화 -> +=1 해줘도 되지만, 바로 1로 초기화한다.
    # answer_dict = {}
    # for char in string:
    #     try:
    #         answer_dict[char] += 1
    #         # => if keyError가 아니라 try except KeyError다
    #     except KeyError:
    #         answer_dict[char] = 1

    # print(answer_dict[100])
    # => 최대값을 가지는 key를 알고 싶다면,
    #    .items()로 greedy의 최대값일 때의 index를 저장하는 로직을 쓴다.
    #    이 때, 최대값을 여러개 가질 수 있으면, 업데이트 후  == max_value 시 따로 lst에 append한다.
    # max_count = float('-inf')
    # max_values = []
    # for value, count in answer_dict.items():
    #     if count > max_count:
    #         max_count = count
    #         max_value = value
    #
    #     if count == max_count:
    #         max_values.append(value)
    #
    # print(''.join(sorted(max_values)))

    ## pythonic -> Counter
    count_dict = collections.Counter(string)
    # print(count_dict)

    # max_count = float('-inf')
    # max_values = []
    # for value, count in count_dict.items():
    #     if count > max_count:
    #         max_count = count
    #         max_value = value
    #     if count == max_count:
    #         max_values.append(value)
    #
    # print(''.join(sorted(max_values)))

    ## => counter는 items()대신 빈도순 정렬된 items()인 most_common을 이용할 수 있다?1
    # print(count_dict.most_common())
    # [('d', 3), ('f', 3), ('e', 1), ('g', 1)]
    max_count = float('-inf')
    max_values = []
    for value, count in count_dict.most_common():
        if count > max_count:
            max_count = count
            max_value = value

        if count == max_count:
            max_values.append(value)

    # print(''.join(sorted(max_values)))

    ## (1) values()로 max값만 편하게 찾고 (2) list comp로 필터링해서 바로 모을 수 도 있다.
    max_count = max(count_dict.values())
    print(''.join(sorted([value for value, count in count_dict.items() if count == max_count])))
