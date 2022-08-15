class 당직():
    def __init__(self, 당직, 부당직, 부부당직):
        self.당직 = 당직
        self.부당직 = 부당직
        self.부부당직 = 부부당직

    pass

    def increase_cnt(self, prev_cnt):
        if prev_cnt == 0:
            self.당직 += 1
        if prev_cnt == 1:
            self.부당직 += 1
        if prev_cnt == 2:
            self.부부당직 += 1

    def is_end(self, prev_cnt):
        if prev_cnt == 0 and self.당직 >= 3:
            return True
        if prev_cnt == 1 and self.부당직 >= 3:
            return True
        if prev_cnt == 2 and self.부부당직 >= 3:
            return True
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.당직!r}, {self.부당직!r}, {self.부부당직!r}, )"


def solution():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    pair = []
    # (1) N개씩 묶기 위해, 이미 N개씩 묶인 갯수인 len(data) // N 만큼 index를 돌린다.
    # -> 이 경우, 배열index과 반복문 index가 암묵적1:1매핑이 되진 않는다.
    for index in range(len(data) // 2):
        # (2) data 1 2 3 4 5 ...의 배열에 대해 N으로 나눈 몫으로 돌린 반복문의 index는
        #     for  0   1   ~2~  ... 각 N개씩 묶음구간의 첫번째항을 index로 가지게 된다.
        #     -> data의 갯수가 N의 배수가 아니라서,
        #     ->           몫을 못내는 마지막구간은, for반복문에서 건들 수가 없다.
        # (3) index를 각 구간의 첫번째항이라고 치면, N개라면,
        #     data index 0 1 2 3 4
        #     for  index 0   1   2
        #  -> for  index * N을 하면 구간의 첫째항
        #     for  index * N + 1을 하면, 구간의 2번째항이다.
        #  -> 만약, 구간의 갯수가 3개면... index * N, index * N + 1, index * N + 2로
        #     구간으로 묶인 원소를 바로 접근할 수 있다.
        # print("arr index", 2 * index, 2 * index + 1)
        # print("arr value", data[2 * index], data[2 * index + 1])
        # arr index 0 1
        # arr value 1 2
        # arr index 2 3
        # arr value 3 4
        # arr index 4 5
        # arr value 5 6
        # arr index 6 7
        # arr value 7 8
        # arr index 8 9
        # arr value 9 10
        pass

    # (4) data의 갯수가 N에 나누어 떨어지지 않는 경우, 몫으로 만든 index에서 제외되서
    #     해당하는 쪽으로 반복문이 아예 돌질 않는다.
    #     이럴 경우, [애초에 N개씩 묶음 구간의  마지막-1구간까지]만 돌고
    #     마지막구간 + 나머지 숫자들을 묶어서 한쌍으로 예외처리르 해 주면된다.
    #     예를 들어, 2쌍씩하고, 나머지는 3쌍
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    pair = 2
    pairs = []
    # for section_index in range(len(data)//pair): # 몫만 구하면 나머지를 남기는 구간은 제외된다.
    # 1,2,3,4,5 //2 -> 구간의 index는 0부터 1, 2구간인데, 몫은 2가 나온다.
    # -> 몫 (len(data)//pair)-1까지 구간index를 돌려야한다.
    for section_index in range(len(data) // pair - 1):  # -> 차라리 직전구간까지만 처리하고 + 마지막구간과 나머지 배열들은 합치자.
        # 배열과 몫구간의 매핑은 N(pair) *구간index를 곱한 것이 구간의 첫째항이고
        # 인덱스는 +1씩 증가하며, 끝항은 0, 1, 2...N-1까지다.
        section_values = [data[pair * section_index + i] for i in range(pair)]
        pairs.append(section_values)
    # 마지막 구간과, 나머지는 합쳐서 처리한다. -> 몫 자체값 - 1: 마지막구간 index
    last_section_index = len(data) // pair - 1
    # 마지막구간의 첫째항 : 구간 첫째항index 부터 끝까지
    # -> 만약 나누어떨어지더라도, 마지막항까지 더하니까 상관없다.
    last_section_values = data[pair * last_section_index:]
    pairs.append(last_section_values)
    # print(pairs)
    # [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10, 11]]

    # 3개씩 구간을 묶고, 마지막 구간에 3 + 1명이 남으면 4명이 된다.
    #                             3 + 2명이 남으면 5명이 된다.
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    pair = 3
    pairs = []
    for section_index in range(len(data) // pair - 1):  # -> 차라리 직전구간까지만 처리하고 + 마지막구간과 나머지 배열들은 합치자.
        section_values = [data[pair * section_index + i] for i in range(pair)]
        pairs.append(section_values)
    last_section_index = len(data) // pair - 1
    last_section_values = data[pair * last_section_index:]
    pairs.append(last_section_values)
    # print(pairs)
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11]]

    from itertools import product, combinations, permutations
    persons = ['주현', '현선', '성미', '재성', '석영']
    # -> 5P3  순서(당/부/부부)가 영향을 미치는 3가지 뽑기 -> 120가지가 한꺼번에 나온다...
    # ->      각 사람당 당직n번, 부당직m번, 부부당직l번만 하도록 짜는 방법은?
    # permutation(cnt, used_bit, result)
    answer = []

    def permutation(prev_cnt, used_bit, prev_arr):
        if prev_cnt == 3:
            answer.append(list(prev_arr))
            return

        for index in range(len(persons)):
            if used_bit & 1 << index: continue
            new_arr = prev_arr + [persons[index]]
            permutation(prev_cnt + 1, used_bit | 1 << index, new_arr)

    # permutation(0, 0, [])
    # print(len(answer), answer)  # 풀탐색 60개 5PC


def permutation(prev_cnt, used_bit, prev_arr, prev_cnt_arr):
    global persons, answer, 당직cnt
    if prev_cnt == 3:
        for prev_당직cnt, prev_prev_cnt in prev_cnt_arr:
            print(prev_당직cnt, prev_prev_cnt)
            if prev_당직cnt.is_end(prev_prev_cnt):
                print("멈춰")
                return

        # 다 챙긴상황에서 이전꺼들을 봐보자.
        # for prev_당직cnt, prev_prev_cnt in prev_cnt_arr:
        #     print(prev_당직cnt, prev_prev_cnt)
        answer.append(list(prev_arr))
        print(list(prev_arr))

        # 그냥 다 완성된 부분에서만 카운팅하자
        for prev_당직cnt, prev_prev_cnt in prev_cnt_arr:
            # print(prev_당직cnt, prev_prev_cnt)
            prev_당직cnt.increase_cnt(prev_prev_cnt)
        return


    for index in range(len(persons)):
        if used_bit & 1 << index: continue
        # (2) 이제 사용한 수 뿐만 아니라, 당직횟수도 채워졌으면 넘어감
        # -> 문제는,,, 주현 당직+1하고
        #    노드가 펼쳐지면서 주현 현선/주현 재성 2가지 node 생기면.. x2배가 되어야한다..?
        #    node를 펼칠 때마다, 직전depth의 카운팅을 한번 더해야한다.

        # (5) 카운터도 누적으로하면서, 검사도 누적으로 해야한다.
        # if 당직cnt[index].is_end(prev_cnt): continue
        # if 당직cnt[index].is_end(prev_cnt): continue
        # for prev_당직cnt, prev_prev_cnt in prev_cnt_arr:
        #     # print(prev_당직cnt, prev_prev_cnt)
        #     if prev_당직cnt.is_end(prev_prev_cnt):
        #         # print("멈춰")
        #         continue

        # (1)선택될때마다 arr에 추가하면서, 그 순서에 맞게 카운터도 돌림
        new_arr = prev_arr + [persons[index]]

        # if prev_cnt == 0:
        #     당직cnt[index].당직 += 1
        # if prev_cnt == 1:
        #     당직cnt[index].부당직 +=1
        # if prev_cnt == 2:
        #     당직cnt[index].부부당직 +=1
        # (3) 보수공사.. node를 펼칠 때마다 누적 카운팅 되어야한다...
        #     누적되면서, index + prev_cnt를 기억하거나..
        #     count객체 또한 기억해야한다?
        ## -> arr에 cnt랑 같이 기억해놓고 누적 증가시키기
        # for prev_당직cnt, prev_prev_cnt in prev_cnt_arr:
        #     # print(prev_당직cnt, prev_prev_cnt)
        #     prev_당직cnt.increase_cnt(prev_prev_cnt)

        # 당직cnt[index].increase_cnt(prev_cnt)
        new_cnt_arr = prev_cnt_arr + [(당직cnt[index], prev_cnt)]
        permutation(prev_cnt + 1, used_bit | 1 << index, new_arr, new_cnt_arr)

    # -> 전체탐색할 거면 라이브러리
    # print(list(permutations(persons, 3)))
    # 당직1명 뽑기 ->

    # x = 당직()
    # x.당직
    # x.부당직
    # x.부부당직
    # elements = list(product(persons, class_))
    #
    # combinations(elements, 3)
    #
    # print(list(product(persons, class_)))


def print_당직():
    global 당직
    for 당직 in 당직cnt:
        print(당직)


if __name__ == '__main__':
    # persons = ['주현', '현선', '성미', '재성', '석영']
    persons = ['주현', '현선', '성미', '재성']
    answer = []
    # 당직_cnt = [0, 0, 0, 0, 0]
    # 부당직_cnt = [0, 0, 0, 0, 0]
    # 부부당직_cnt = [0, 0, 0, 0, 0]

    주현당직 = 당직(0, 0, 0)
    현선당직 = 당직(0, 0, 0)
    성미당직 = 당직(0, 0, 0)
    재성당직 = 당직(0, 0, 0)
    석영당직 = 당직(0, 0, 0)

    # 당직cnt = [주현당직, 현선당직, 성미당직, 재성당직, 석영당직]
    당직cnt = [주현당직, 현선당직, 성미당직, 재성당직]
    permutation(0, 0, [], [])
    print(len(answer), answer)  #
    print_당직()

    # solution()
