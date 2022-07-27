from typing import List


def a_길이가_같아_암묵적_index_묶인_개별요소_상태관리_배열_with_while(arr: List):
    arr = sorted(arr)
    # 1. 길이가 같은 배열을 선언 -> 암묵적으로 index로 묶임 & 각 요소의 상태관리를 해준다.
    # -> 객체라면, 각 요소+상태관리요소가 객체로 묶이고, 배열길이만큼 list 내부에 들어가야한다.
    # -> 각 요소의 상태관리는 대부분 0으로 초기화해서 한다.
    # -> 원래배열과 암묵적으로 묶인 배열을 위아래에 두고 생각한다
    # [0, 0, 0] -> 길이가 같아 index로 묶인 counter
    # [1, 2, 3] -> 원래 배열
    counter = [0] * len(arr)

    # 2. 묶인 배열들을 같이 처리하려면, index를 사용해서 통해 배열길이만큼 반복문을 돌아야한다
    for index in range(len(arr)):
        # 3. 내부에서는 arr[i]와 counter[i]를 같이 사용한다.
        # arr[i] 액션마다 -> counter[i]상태를 업데이트한다.
        arr[index] = arr[index] + 1
        counter[index] = counter[index] + 1

    # print(counter)
    # print(arr)

    # 3. 하지만, 상태관리를 하는 마당에, arr길이만큼만 처리하지 않는다
    # -> arr길이 이상 왔다갔다 순회를 해야한다면,
    # -> index를 반복문 밖으로 빼서 컨트롤이 가능한, i = 0 while i업데이트 을 써야한다.
    #   for i in range(len(arr)) <-> i = 0  while i < len(arr) i += 1
    i = 0
    while i < len(arr):
        # action
        i = i + 1


def b_arr는_action을_counter는_action후_상태업뎃_counter의상태종착역에서_등산(arr):
    arr = sorted(arr)
    counter = [0] * len(arr)

    index = 0

    # 커서가 마지막 요소 위치를 넘어섰다면 (index == len(arr)) 종료된다.
    while index < len(arr):
        # index인 커서가 그냥 증가하는 것이 아니라, 특정상태일때 등산시켜보자.
        # 커서 자리에서 action을 하고, 액션의 counter를 올리기만 하자.
        # 현재커서에서 액션의 횟수가 3회가 찾을 경우 -> 커서를 올리자
        #  0초기화부터 시작하므로 == 3도달시 등산이다.
        if counter[index] == 3:
            # 각 요소의 상태종착역에 도달해야지만, 다음커서로 넘어가는 것이 for문과의 차이점
            index += 1
            continue  # early return을 반복문에선 early continue로 넘어간다.

        # (아직 counter가 3이 안찬 상태)
        # action -> 현재커서 위치에서 기존요소에 +1
        arr[index] += 1
        # action후에는 counter의 종착역까지 상태관리가 들어가야한다.
        counter[index] += 1

    print(counter)
    print(arr)


def c_각_상태종착역에서_등산직전_상태값초기화후_등산(arr):
    arr = sorted(arr)
    counter = [0] * len(arr)

    index = 0
    while index < len(arr):
        if counter[index] == 3:  # 각 요소 상태값의 종착역 -> 이후 등산
            # 1. 등산 하기 직전에, 상태값을 0으로 초기화해줄 수있다.
            # -> 이는 등산 후부터 현재시점보다 커서를 내린 뒤, 새롭게 누적 카운티을 할것이라는 얘기다
            counter[index] = 0
            index += 1  # 현재(index)요소는 종착상태 -> 커서등산
            continue

        arr[index] += 1  # action
        counter[index] += 1  # action후 상태 업데이트

    print(counter)
    print(arr)


def d_action횟수의_종착상태값을_커서위치index로_지정하면_index수만큼만_action(arr):
    arr = sorted(arr)
    counter = [0] * len(arr)

    index = 0
    while index < len(arr):
        # 1. 각 요소 종착상태값을,  커서위치로 지정할 수 있다.
        #    0 -> 0번, 1 -> 1번, 2->2번, 3->3번만 액션한다.
        # [0, 0, 0] -> [0, 1, 2]
        # if counter[index] == 3:
        if counter[index] == index:
            counter[index] = 0
            index += 1
            continue

        arr[index] += 1
        counter[index] += 1

    print(counter)
    print(arr)


def e_등산전까진_상태값만큼_반복되는_중에_0번째요소와_현재커서와_스왑_action_최종_짝수_제자리_홀수_한번바뀜_1개위치와는_1번스왑만_유효(iterable):
    arr = sorted(iterable)
    counter = [0] * len(arr)

    # 0. 스왑하면 arr의 구성이 달라지므로 원본을 보존하여 찍어놓는다.
    print(arr, "<--원본")

    index = 0
    while index < len(arr):
        # 1. 반복문이 커서의 상태값기준으로 다음커서로 넘어가는데
        #    상태값종착역(0부터 커서위치직전까지)전까지는 action후 상태값만 증가하는 구조이다.
        #    0~n-1까지 반복되고 등산하므로, 커서의 위치n번 반복된다.
        if counter[index] == index:
            counter[index] = 0
            index += 1
            continue

        # 1. action은 커서의위치(n번, 0~n-1)만큼 반복되는데,
        #    only 1개요소 0번째요소와 스왑action을 주면
        #    현재커서에서는 0->x, 1-> 0과 스왑1번, 2-> 0과스왑 2번이다.
        #    -> 스왑2번하면 제자리이다.
        #    -> 스왑3번하면 1번스왑과 동일하다 -> 결국 스왑은 1개요소와는 1번만
        #    --> 결국, 1개요소와는 1번만 스왑해도 의미를 가진다.
        # arr[index] += 1
        arr[0], arr[index] = arr[index], arr[0]

        # 2. 스왑action마다출력을 해야 1번스왑만 의미를 가지는 것을 확인할 수 있다.
        print(arr, f"<- {index}-상태{counter[index]}")
        counter[index] += 1

    print(counter)
    print(arr)


def f_등산전까지_0부터_현재커서직전까지_증가하는_action횟수를_활용하여_현재커서와_스왑(iterable):
    arr = sorted(iterable)
    counter = [0] * len(arr)

    index = 0
    while index < len(arr):
        # 0. index업데이트 이전에, index상태값(action횟수)이 커서에 오기직전까지 종착역만큼 루프를 돈다.
        if counter[index] == index:
            counter[index] = 0
            index += 1
            continue

        # 1. action횟수가 커서에 도달직전까지 반복되는 중인데,
        #   -> 내 커서 도달전까지 증가하는 action횟수 위치랑 스왑하기
        #   --> action횟수 = 0부터 나 직전까지만 들어옴 -> 0부터 나직전까지 스왑
        action_count = counter[index]
        arr[action_count], arr[index] = arr[index], arr[action_count]

        counter[index] += 1

        print(counter)
        print(arr)
    print(counter)
    print(arr)


def g_현재커서와_action횟수위치와_스왑action_후_상태값은_증가시키되_커서를_0으로내려_현재커서까지_다시등산(iterable):
    arr = sorted(iterable)
    counter = [0] * len(arr)

    index = 0
    while index < len(arr):
        if counter[index] == index:
            counter[index] = 0
            index += 1
            continue

        action_count = counter[index]
        arr[action_count], arr[index] = arr[index], arr[action_count]
        # 스왑후 현재커서의 상태값은 업데이트하되
        counter[index] += 1
        # action후, 상태값이 증가된 상태로, 상태값은 안내리고, 커서만 내린다.
        # -> [이미 등산후 직전상태값은 0으로 초기화]하면서 올라왔으므로
        # -> 커서는 0부터 다시 [0으로 초기화된 상태값]만큼 action하며 올라올 것이다.
        # 즉, 상위 상태값 1증가마다, 커서를 0부터 [현재커서에 도달]하여, [현재커서 상태값이 +1]되는 순간까지 등산시킨다.
        #    그동안 액션은 등산하면서(0->0번, 1->1번, 2->2번) action 누적된다.
        index = 0

        print(counter)
        print(arr)
    print(counter)
    print(arr)


def h_누적등산확인만(iterable):
    arr = sorted(iterable)
    counter = [0] * len(arr)

    index = 0
    while index < len(arr):
        if counter[index] == index:
            counter[index] = 0
            index += 1
            continue

        # action: 현재커서(나)는 0부터 커서직전까지의 위치와 스왑을 시행함.
        action_count = counter[index]
        arr[action_count], arr[index] = arr[index], arr[action_count]
        # action후 업데이트 이전에 현재상태 출력
        print(counter, f"현재 커서{index} 현재상태값{counter[index]}")
        print(arr)
        # action count update
        counter[index] += 1
        # 직전커서는 처음부터 다시 등산
        # -> 커서1부터, 직전까지와 스왑을 반복함.
        # -> 커서1이면, 0자리와 1번
        # -> 커서2이면, 커서1(0자리와 1번) + 0자리와 1번
        # -> 커서2이면, 커서1(0자리와 1번) + 1자리와 1번
        # -> 커서3이면, 커서1 + 커서2 + 0자리와 1번
        # -> 커서3이면, 커서1 + 커서2 + 1자리와 1번
        # -> 커서3이면, 커서1 + 커서2 + 2자리와 1번
        index = 0


def i_홀수커서_0부터직전까지스왑_짝수커서_0번째와_누적등산스왑하면_마지막요소유지한체_섞인다(arr):
    arr = sorted(arr)
    counter = [0] * len(arr)

    print(arr)

    index = 0
    while index < len(arr):
        if counter[index] == index:
            counter[index] = 0
            index += 1
            continue

        # action
        # -> 짝수커서는 0하고만 스왑
        if index % 2 == 0:
            arr[0], arr[index] = arr[index], arr[0]
        # -> 홀수커서는 0부터 n-1까지 1씩증가하는 위치와 다 스왑
        else:
            arr[counter[index]], arr[index] = arr[index], arr[counter[index]]

        print(arr, f"<- 현재 커서위치: {index}")

        counter[index] += 1
        index = 0
        # [1, 2, 3, 4]
        # [2, 1, 3, 4] <- 현재 커서위치: 1
        # [3, 1, 2, 4] <- 현재 커서위치: 2
        # [1, 3, 2, 4] <- 현재 커서위치: 1
        # [2, 3, 1, 4] <- 현재 커서위치: 2
        # [3, 2, 1, 4] <- 현재 커서위치: 1
        # [4, 2, 1, 3] <- 현재 커서위치: 3
        # [2, 4, 1, 3] <- 현재 커서위치: 1
        # [1, 4, 2, 3] <- 현재 커서위치: 2
        # [4, 1, 2, 3] <- 현재 커서위치: 1
        # [2, 1, 4, 3] <- 현재 커서위치: 2
        # [1, 2, 4, 3] <- 현재 커서위치: 1
        # [1, 3, 4, 2] <- 현재 커서위치: 3
        # [3, 1, 4, 2] <- 현재 커서위치: 1
        # [4, 1, 3, 2] <- 현재 커서위치: 2
        # [1, 4, 3, 2] <- 현재 커서위치: 1
        # [3, 4, 1, 2] <- 현재 커서위치: 2
        # [4, 3, 1, 2] <- 현재 커서위치: 1
        # [4, 3, 2, 1] <- 현재 커서위치: 3
        # [3, 4, 2, 1] <- 현재 커서위치: 1
        # [2, 4, 3, 1] <- 현재 커서위치: 2
        # [4, 2, 3, 1] <- 현재 커서위치: 1
        # [3, 2, 4, 1] <- 현재 커서위치: 2
        # [2, 3, 4, 1] <- 현재 커서위치: 1


def j_print대신_arr의_저장은_이중배열에(iterable):
    arr = sorted(iterable)
    counter = [0] * len(arr)
    # 1. arr들의 저장은 이중리스트에 append한다.
    #    값배열은 slicing얕은복사만 해도, 완전히 복사된다.
    result = [arr[:]]

    index = 0
    while index < len(arr):
        if counter[index] == index:
            counter[index] = 0
            index += 1
            continue
        # action
        if index % 2 == 0:
            arr[0], arr[index] = arr[index], arr[0]
        else:
            arr[counter[index]], arr[index] = arr[index], arr[counter[index]]
        # 2. action후 바로 저장
        #    값 배열의 저장은 얕은복사로 사본만들어서
        result.append(arr[:])
        counter[index] += 1
        index = 0

    # 3. 다 돌고 저장된 값 반환
    return result


def solution():
    # a_길이가_같아_암묵적_index_묶인_개별요소_상태관리_배열_with_while([1, 2, 3])
    # b_arr는_action을_counter는_action후_상태업뎃_counter의상태종착역에서_등산([1, 2, 3])
    # c_각_상태종착역에서_등산직전_상태값초기화후_등산([1, 2, 3])
    # d_action횟수의_종착상태값을_커서위치index로_지정하면_index수만큼만_action([0, 0, 0])
    # e_등산전까진_상태값만큼_반복되는_중에_0번째요소와_현재커서와_스왑_action_최종_짝수_제자리_홀수_한번바뀜_1개위치와는_1번스왑만_유효("ABC")
    # f_등산전까지_0부터_현재커서직전까지_증가하는_action횟수를_활용하여_현재커서와_스왑("ABC")
    # g_현재커서와_action횟수위치와_스왑action_후_상태값은_증가시키되_커서를_0으로내려_현재커서까지_다시등산("ABC")
    # h_누적등산확인만([1, 2, 3])
    # i_홀수커서_0부터직전까지스왑_짝수커서_0번째와_누적등산스왑하면_마지막요소유지한체_섞인다([1, 2, 3, 4])
    result = j_print대신_arr의_저장은_이중배열에([1, 2, 3])
    print(result)


if __name__ == "__main__":
    solution()
