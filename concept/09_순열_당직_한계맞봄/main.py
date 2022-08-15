import copy


class 당직():
    def __init__(self, 당직, 부당직, 부부당직, name="이름없음"):
        self.당직 = 당직
        self.부당직 = 부당직
        self.부부당직 = 부부당직
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
        # for cnt, 당직 in prev_당직_arr:
        #     if 당직.is_end(cnt):
        #         return
        #     당직.increase_cnt(cnt)
        # 위에코드는, 첫번째가 통과해서 increate했어도, 중간에서 탈락하는 경우
        # 첫번째를 카운팅하고 끝나버린다. -> 다 검사하고 다 증가 시켜야한다.
        for cnt, 당직 in prev_당직_arr:
            if 당직.is_end(cnt):
                return
        for cnt, 당직 in prev_당직_arr:
            당직.increase_cnt(cnt)
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


if __name__ == '__main__':
    persons = ['주현', '현선', '성미', '재성', '석영']
    # persons = ['주현', '현선']
    answer = []

    주현당직 = 당직(0, 0, 0, "주현")
    현선당직 = 당직(0, 0, 0, "현선")
    성미당직 = 당직(0, 0, 0, "성미")
    재성당직 = 당직(0, 0, 0, "재성")
    석영당직 = 당직(0, 0, 0, "석영")

    당직cnt = [주현당직, 현선당직, 성미당직, 재성당직, 석영당직]
    # 당직cnt = [주현당직, 현선당직]
    permutation(0, 0, [], [])
    print(len(answer), answer)
    print_당직()
