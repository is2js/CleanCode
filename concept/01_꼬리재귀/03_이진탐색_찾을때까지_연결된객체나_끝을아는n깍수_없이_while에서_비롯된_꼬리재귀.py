def binary_search_loop(some_list, element):
    # 1. 이진탐색은 이미 정렬된 list를 1개씩 도는 것이 아니라
    #    시작/끝 index를 업데이트하면서
    #    일치하는 값의 index 값 1개를 반환한다.
    #    -> list 1개씩 순서대로 도는 것이 아니다 -> while
    #    -> list를 길이만큼 도는 것이 아니라
    #       start는 증가 / end는 감소시키면서 닿을때까지 돈다.
    #       탈출조건이 start > end 이므로
    #       start <= end까지 돈다.

    # 2. 돌면서 바뀌는 값들은 반복문위에 변수로 선언해놓는다.
    start_index = 0
    end_index = len(some_list) - 1
    # 3. 업데이트되는 변수를 바탕으로 돌 수 있는 조건을 while문에 명시한다.
    while start_index <= end_index:
        # 4. 탐색의 조건을 만족하면 바로 탈출해서 반환한다.
        # -> 업데이트된 직전start, end의 중간인덱스에, 원하는 값이 있으면
        #    다음 업데이트할 필요없다.
        #   그 mid인덱스륿 반환한다.
        middle_index = (start_index + end_index) // 2
        # 5. 중간에 있는 값이 내가 찾는 값이면, 그 중간인덱스를 반환한다
        # -> 나는 중간값을 바탕으로 찾으면 반환 / 못찾으면 start를 땡기든지, end를 땡기든지 할 것이다.
        if some_list[middle_index] == element:
            return middle_index

        # 5. 못찾은 상태에서, 업데이트를 작성한다.
        # (1) 찾는 값이 중간값보다 작으면, end를 중간보다 아래를 돌도록 중간으로 옮긴다.
        if element < some_list[middle_index]:
            end_index = middle_index
            continue
        # (2) 크면, start를 middle로 옮긴다. # (같으면 이미 탈출했다)
        start_index = middle_index

    # 6. 못찾았으면 None을 반환한다.
    return None


#     start_index = 0
#     end_index = len(some_list) - 1
#     while start_index <= end_index:
#         middle_index = (start_index + end_index) // 2
#         if some_list[middle_index] == element:
#             return middle_index
#         if element < some_list[middle_index]:
#             end_index = middle_index
#             continue
#         start_index = middle_index
#     return None



# 0. [끝을 아는 주체 없이 from while] 찾을때까지 꼬리재귀 depth를 통해 반복한다.
def binary_search_tail_recursive(some_list, element):
    # 1. 꼬리재귀는 고정된 배열 -> 자식들을 동적트리순회하는 것이 아니라
    #   (1) 1개의 값을 반환을 위해 return안에서 작성되며
    #   (2) 내수용 메서드로 작성된다.
    # return search_index()

    # 2. n -> n-1이라든지, 객체라면 연결된 데코객체라던지, [고정된 some_list, element)
    #    [제한된 갯수로 꼬리재귀의 detth=stack=가상공간제한]을 걸 수도 있지만,
    #    [여기 serarch에선 미리 끝 알 수 있는 제한 주체가 없고, 찾을때까지 재귀]한다.
    #    업데이트되는 모든 값들을 파라미터로 주어야한다.
    #    (0) 사용되는 배열 some_list와 찾는 요소 element는 고정이기 때문에 꼬리재귀 파라미터가 아니다.
    #    (1) start/end커서가 움직이며 초기값은 0, len()-1이다.
    # return search_index(0, len(some_list) - 1)

    # 3. 꼬리재귀함수의 작성은 [끝이 있는 연결객체, 주체]가 없더라도
    #    depth마다 업데이트되는 파라미터로 종착역을 정하고, 찾은 값을 반환한다. 
    def search_index(start_index, end_index):
        #  4. 종착역은 중앙커서의 값 == 찾는 요소일 때, 중앙커서를 반환하여 끝난다.
        middle_index = (start_index + end_index) // 2
        if some_list[middle_index] == element:
            return middle_index

        # 5. 꼬리 재귀내에서 return문에서 파라미터 업데이트와 함께 꼬리재귀를 호출해야한다.
        #  -> 업데이트가 경우의수가 있다면, if + return 꼬리재귀(업데이트 인자)로 작성해야하며
        #  -> 가능한다면 삼항연산자로 경우를 return문 한줄에 다룰 수 도 있다.
        return search_index(start_index, middle_index) if some_list[middle_index] > element \
            else search_index(middle_index + 1, end_index)

    return search_index(0, len(some_list) - 1)


def solution():
    # print(binary_search_loop([1, 2, 3, 4, 5], 4))
    print(binary_search_tail_recursive([1, 2, 3, 4, 5], 4))


if __name__ == '__main__':
    solution()
