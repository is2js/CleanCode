def combination(arr, r):
    # 1. 어차피 정렬을 한번 해줘야하며, 문자열 입력시 list로 반환해준다.
    arr = sorted(arr)
    # 동적트리순회는 종착역의 값을 얻을 수가 없으므로(only 1방향연결의 linkedlist만 가능)
    # 마지막node마다 결과값을 저장할 배열
    result = []

    # 3.
    def generate(chosen):
        # 4. 꼬리재귀의 종착역을 설정한다.
        #    동적트리순회의 꼬리재귀는, 자식이 없어 for문 안도는 마지막node가 default 종착역이지만
        #    그전에, r만큼 누적결과값배열이 가득차면, 저장하고 빽한다.
        if len(chosen) == r:
            print(chosen)
            result.append(chosen[:])
            return

        # 4-2 composite객체(나도, 자식들도 스스로, 처리할 일)면 자신의 할일을 자식 진입전에 한다.
        #    ex> 내 자신의 출력사본 만들기 -> 자식들도 진입하면 출력사본 만들기
        #    -> 객체가 아니라면, 나자신의 상태를바꾸거나 이용하는 일이 없다.
        #    -> method레벨이라면 나 자신이 없고 자식들 뿐이다.

        # 5. 자식들을 순회하면서, 꼬리재귀를 업데이트인자로 호출하며 depth가 깊어진다.
        #    -> 상태배열이 따로 있다면, 체크하면서 진입하기도 한다.
        for index in range(len(arr)):
            # 6. 꼬리재귀 호출전에, [자식 진입전, depth마다 달라질 상태 or 누적결과값 업데이트]로서 파라미터 chosen을 업데이트하고 진입해야한다.
            #   -> 현재 자식을 chosen에 넣었는다.
            #   -> 자식은 업데이트된 누적결과값 파라미터를 이용한다.
            chosen.append(arr[index])
            generate(chosen)
            # 7. 재귀호출이 끝나면, 다시 부모node를 빽해서 올라와 [다음 자식을 위해 초기화]해놔야한다.
            #   -> choson에 넣은 것을 다시 도로 빼야한다.
            #   -> 상태값 변화는 없엇기 때문에 복원처리가 없다.
            chosen.pop()
            # 8. 여기까지 해주면, depth가 깊어질때마다 arr순서대로 1개씩 빼서 choson을 채우며
            #    마지막node가 아닌 종착역node(chosen r개)에 데이터가 출력되고 저장된다.
            #    -> **현재 arr를 터지하지 않고 똑같은 arr를 돌고 있으므로**
            #    -> 현재커서의 값 arr[index]를 넣고 자식진입해도, 처음부터 arr를 다시 돌아서**
            #    -> **모든 경우의 수의 조합을 다 짜게 된다.**
            #    -> **중복조합이 된다.**


    # 2. depth마다 원소를 하나씩 뽑아서 채워야하므로, 꼬리재귀로서 inner method를 만들고, 초기값을 인자로 채워넣는다.
    #   -> 고정된 값은 굳이 넣지 않고, context변수로서 활용한다.
    generate([])

    # 9.중복조합 결과값들 반환
    return result




def solution():
    print(combination([1, 2, 3], 2))
 
 
if __name__ == '__main__': 
    solution() 
