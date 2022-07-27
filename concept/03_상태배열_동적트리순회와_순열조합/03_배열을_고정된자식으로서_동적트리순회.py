def fixed_sub_tree_all_node_traversal(arr):
    # 1. 객체level이 아니라, method레벨에서의 [동적트리순회]는
    #    재귀 정의하기 전에, 선언되는 변수들은 [재귀를 사용하는 객체 내부 필드]가 된다.
    #    -> arr를 선언했다면 고정된 [컬렉션필드, 자식들]로 간주된다.
    #    method level에서는 [자식객체들의 순회하며, 꼬리재귀]가 아니라
    #    -> [공용 컬렉션 필드를 고정된 자식들로 간주]하여 -> [같은 순서로, 같은 횟수만큼] 다음 depth의 자식node들을 순회한다.
    arr = sorted(arr)

    # 2. 트리순회부터는 linkedlist가 아니기 때문에, 종착역의 값을 연쇄 return받지 못한다.
    #    대신 depth마다 달라지는 값을 실시간으로 반영하는 [꼬리재귀 파라미터]를 사용해서 업데이트 시킨다.
    #    트리순회는 [같은 상태]로 다음level자식들을 돌아야하니 [진입전 상태변화] -> [자식] -> [상태 복구]의 과정이 있다.
    #    결국엔 root도 자식들을 다돌고 root로 복귀한다면, 파라미터의 값은 비어있을 것이다.
    #    -> 그래서 최종 종착역마다 출력하거나, 결과를 담을 변수가 필요하다.
    result = []

    # 4. 이 inner 재귀내에서 [고정된 자식들]을 순회한다.
    #    만약, arr말고 객체의 고정된 필드가 있으면 그것 처리부터 하고 자식을 돌면되는데 여기선 없다.
    #    -> 지역변수 arr는 composite객체의 자식들이라 생각한다.
    def generate(chosen):
        # 5. 자식들을 a부터 d까지 또 a-a, a-b, 이렇게 순회해나갈 것이다.
        #    무한으로 자식을 순회하면 끝도 없는 tree가 만들어지니
        #    종착역node를 잡아줘야한다.
        #    종착역은 주로, 업데이트되는 파라미터변수를 활용해서 만족시 그만둔다.
        if len(chosen) == 2:
            # 6. tree 속 종착역 node의 값은 바로 return 못하니, 출력하고 저장해준다.
            print(chosen)
            result.append(chosen[:])
            return

        # 7. 자식들을 순회하는데, method level에선 서로 다른 객체며, 서로 다른 자식이 아니다.
        #   -> 하나의 지역변수 컬렉션필드를 고정된 자식이라고 생각하고, 그것들을 똑같이 순회한다.
        for index in range(len(arr)):
            # 8. depth가 깊어지기 전에, [현재depth에서 업데이트된 내역을 인자로 반영]해줘야한다.
            #  -> 대부분 자식들 중, 현재 값을 이용해서 꼬리재귀 파라미터를 업데이트한다.
            chosen.append(arr[index])
            generate(chosen)
            # 9. 다음 자식으로 순회하기 전, 업데이트 내역을 복구해서, 똑같은 조건으로 다음자식node로 뻗어나간다
            chosen.pop()

        # 10. 자식들의 순회가 끝나면, 재귀메서드가 종료되어 가상의 공간=depth가 1칸 줄어들면서
        #     직전 부모node로 빽한다.

        pass

    # 3. 고정되어있지만 [자식들에 대해 depth를 추가하며 동적트리순회]하려면, inner로 재귀함수를 정의해야한다.
    #    재귀 -> 가상의 stack공간 추가 -> depth공간으로 간주된다.
    #    이 가상의 공간에서 일어나는 일들을 업데이트에서 반영하려면, 파라미터가 들어간 재귀를 정의해야한다.
    #    [가상의 depth마다 변화를 받을 누적결과변수]를 파라미터로 추가하고
    #   -> 최초 호출하는 root에서 default값을 인자로 줘야한다.
    #   -> depth가 깊어짐에 따라, 현재 자식의 값을 []빈배열에 기록하고 싶다.
    generate([])

    # 11. 동적트리순회 재귀메서드가 종료되는 다음에는, result에 종착역 값들이 모여있을 것이다.
    return result
    # [1, 1]
    # [1, 2]
    # [1, 3]
    # [1, 4]
    # [2, 1]
    # [2, 2]
    # [2, 3]
    # [2, 4]
    # [3, 1]
    # [3, 2]
    # [3, 3]
    # [3, 4]
    # [4, 1]
    # [4, 2]
    # [4, 3]
    # [4, 4]


def fixed_sub_tree_특정_node_traversal_with_상태배열(arr):
    arr = sorted(arr)  # 동적트리순회시 고정된 자식
    result = []

    # 1. [순회 중인 자식]에 대해 사용체크를 해주는 0 초기화 상태배열을 선언한다.
    #    arr[index] 순회중인 자식 / used[index] 순회 중인 자식의 사용 유무
    # used = [0 for _ in range(len(arr))]

    # 4. 상태배열은 depth깊어짐에 따라 무조건 업데이트 되므로, 재귀 파라미터로 넣어놓자.
    # def generate(chosen):
    def generate(chosen, used):
        # 1.5 동적트리순회도 재귀라서 종착역을 설정해놔야한다.
        if len(chosen) == 3:
            print(chosen)
            result.append(chosen)
            return

        for index in range(len(arr)):
            # 2. 고정된 자식들로 트리를 순회하는데
            #    [현재 자식의 상태]를 확인해서, 사용한 상태면 진입안한다.
            ###############
            # 선택된 것을 다음depth에서는 [고정 자식들에서 제외시켜 순회]하는 조합은,
            # 그 다
            # 순열은 [사용체크 해놓고
            ###############
            if used[index] == 1:
                continue
            # 3. (사용안한 자식일 경우) -> 사용체크를 해서 진입한다.
            # -> [상태변수는 무조건 업데이트 되므로 꼬리재귀 파라미터로 미리 추가]해주자
            used[index] = 1
            # 5. my) 생각해보니, 동적트리순회의 연산은 자신의 연산이 없는 대신
            #   -> 자식들 순회중으로서 진입직전에 연산을 해준다.
            #   -> node는 줄기연산의 결과일 뿐이다?!
            # 6. 누적결과가 쌓일chosen도 업데이트해준다.
            chosen.append(arr[index])
            generate(chosen, used)
            chosen.pop()
            used[index] = 0

    generate([], [0 for _ in range(len(arr))])


    return result




def solution():
    # fixed_sub_tree_all_node_traversal([1, 2, 3, 4])
    fixed_sub_tree_특정_node_traversal_with_상태배열([1, 2, 3])
    pass
    # [1, 2, 3]
    # [1, 2, 4]
    # [1, 3, 2]
    # [1, 3, 4]
    # [1, 4, 2]
    # [1, 4, 3]
    # [2, 1, 3]
    # [2, 1, 4]
    # [2, 3, 1]
    # [2, 3, 4]
    # [2, 4, 1]
    # [2, 4, 3]
    # [3, 1, 2]
    # [3, 1, 4]
    # [3, 2, 1]
    # [3, 2, 4]
    # [3, 4, 1]
    # [3, 4, 2]
    # [4, 1, 2]
    # [4, 1, 3]
    # [4, 2, 1]
    # [4, 2, 3]
    # [4, 3, 1]
    # [4, 3, 2]
    #
    # Process finished with exit code 0


if __name__ == '__main__':
    solution()
