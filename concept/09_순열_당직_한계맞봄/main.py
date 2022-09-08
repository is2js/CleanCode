import copy
from typing import List


class 당직():
    def __init__(self, name="이름없음"):
        self.당직 = 0
        self.부당직 = 0
        self.부부당직 = 0
        self.name = name

    def increase_cnt(self, prev_cnt):
        if prev_cnt == 0:
            self.당직 += 1
        if prev_cnt == 1:
            self.부당직 += 1
        if prev_cnt == 2:
            self.부부당직 += 1

    def is_end(self, prev_cnt):
        if prev_cnt == 0 and self.당직 >= 3:
            # print(f"{prev_cnt}차례에 {self.당직}이라서 탈락", end=" ")
            return True
        if prev_cnt == 1 and self.부당직 >= 3:
            # print(f"{prev_cnt}차례에 {self.부당직}이라서 탈락", end=" ")
            return True
        if prev_cnt == 2 and self.부부당직 >= 3:
            # print(f"{prev_cnt}차례에 {self.부부당직}이라서 탈락", end=" ")
            return True
        return False

    def is_end_total(self):
        return self.당직 >= 3 and self.부당직 >= 3 and self.부부당직 >= 3

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.당직!r}, {self.부당직!r}, {self.부부당직!r}, )"


def print_당직():
    global 당직
    for 당직 in 당직cnt:
        print(당직)


def permutation(prev_cnt, used_bit, prev_name_arr, prev_당직_arr):
    global persons, answer, 당직cnt
    if prev_cnt == 3:
        # ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ
        # for count, 당직 in prev_당직_arr:
        #     if 당직.is_end(count):
        #         return
        #     당직.increase_cnt(count)
        # 위에코드는, 첫번째가 통과해서 increate했어도, 중간에서 탈락하는 경우
        # 첫번째를 카운팅하고 끝나버린다. -> 다 검사하고 다 증가 시켜야한다.
        # for count, 당직 in prev_당직_arr:
        #     if 당직.is_end(count):
        #         return
        # for count, 당직 in prev_당직_arr:
        #     당직.increase_cnt(count)
        # print_당직()
        answer.append(list(prev_name_arr))
        return
        # person = prev_당직_arr[index]
        # if person.is_end(prev_cnt):
        #     print(f"멈춰 {prev_cnt}의 {person}가 3회를 이미 채웠어")
        #     continue

    for index in range(len(persons)):
        if used_bit & 1 << index: continue
        # for 당직_cnt1 in prev_당직_arr:
        #     if 당직_cnt1.is_end(prev_cnt):
        #         print(f"멈춰 {prev_cnt}의 {str(당직)}가 3회를 이미 채웠어")
        #         print_당직()
        #         continue

        new_name_arr = prev_name_arr + [persons[index]]
        new_당직_arr = prev_당직_arr + [(prev_cnt, 당직cnt[index])]
        print(new_당직_arr)
        permutation(prev_cnt + 1, used_bit | 1 << index, new_name_arr, new_당직_arr)


def is_complete(당직스):
    return all([당직.is_end_total() for 당직 in 당직스])



def permutation2(prev_cnt, used_bit, prev_name_arr):
    global persons, answer, 당직cnt
    if prev_cnt == 3:

        for depth, name in enumerate(prev_name_arr):
            for 당직 in 당직cnt:
                if 당직.name == name:
                    if 당직.is_end(depth):
                        return


        # 발굴완료하면, 카운팅..?! -> 막는 것은 node뻗을 때/ 세는 것은 완성후?
        print(f"선택된당직===============")
        for depth, name in enumerate(prev_name_arr):
            for 당직 in 당직cnt:
                if 당직.name == name:
                    당직.increase_cnt(depth)
                    print(f"증가 {당직}", end=" /")


        print()
        answer.append(list(prev_name_arr))
        return


    for index in range(len(persons)):
        if used_bit & 1 << index: continue
        # 현재 검사 이전에 직전까지 검사
        # 모두다 검사할 게 아니라, 선택된 수들만 누적된 상태로 검사해야한다.

        # 현재 검사 -> 직전 것들은 검사해봐야 의미 없음.. 현재 검사하고 넘어갔기 때문에?!
        if 당직cnt[index].is_end(prev_cnt):
            continue

        new_name_arr = prev_name_arr + [persons[index]]
        # 개별root node들마다 새로운 당직객체들을 만들어줘서 각각 관리되게 하기
        # 첫번재 node없는 곳에서는 여러 root를 내리기전까진 작동안해야한다.
        # 당직cnt[index].increase_cnt(prev_cnt)
        permutation2(prev_cnt + 1, used_bit | 1 << index, new_name_arr)

    if prev_cnt == 1:
        print("=====================1개 root 끝==========================")


class 당직스():
    def __init__(self, person_names: List):
        self.당직스 = [당직(name=person_name) for person_name in person_names]


if __name__ == '__main__':
    persons = ['주현', '현선', '성미', '재성', '석영']
    # person_names = ['주현', '현선']
    answer = []

    # 주현당직 = 당직(0, 0, 0, "주현")
    # 현선당직 = 당직(0, 0, 0, "현선")
    # 성미당직 = 당직(0, 0, 0, "성미")
    # 재성당직 = 당직(0, 0, 0, "재성")
    # 석영당직 = 당직(0, 0, 0, "석영")
    주현당직 = 당직("주현")
    현선당직 = 당직("현선")
    성미당직 = 당직("성미")
    재성당직 = 당직("재성")
    석영당직 = 당직("석영")

    # 당직cnt = [주현당직, 현선당직, 성미당직, 재성당직, 석영당직]
    당직cnt = 당직스(persons).당직스
    # 당직cnt = [주현당직, 현선당직]
    permutation2(0, 0, [])

    for 당직 in 당직cnt:
        print(당직, end=" ==\n")
    print()

    print(len(answer), answer)
    result = []
    for team in answer:
        for name in team:
            if 'B' in name:
                break
        else:
            result.append(team)
    print(len(result), result)
