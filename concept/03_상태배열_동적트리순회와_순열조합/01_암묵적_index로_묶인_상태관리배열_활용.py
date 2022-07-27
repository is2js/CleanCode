def 상태관리배열_커서등산시_직전상태초기화하며등산_action및상태값증가시_커서를_0으로내려_직전까지_다시등산(arr):
    #arr = sorted(arr)
    counter = [0] * len(arr)

    index = 0
    while index < len(arr):
        # 0부터 시작하는 현재커서 상태값은 횟수는 n번을 채우고, 값이n일 때 상태값0되면서 등산한다.
        if counter[index] == index:
            # next1
            counter[index] = 0
            index += 1
            continue # 다음루프로 넘어가는 것이자, 마지막이라면 break


        # action every 상태값 증가마다 loop
        # -> arr[index] 현재커서위치의 값
        # -> counter[index]: 현재커서위치의 상태값이자 && 커서등산전 0부터 +1씩 증가하는 반복문의 주체
        # -> arr[counter[index]]: 0~n-1로 움직이는 커서 위치의 값

        counter[index] += 1
        # 액션->상태값증가마다 -> 커서를 0으로 내려, 현재커서에 도달하기전까지,누적 등산한다
        # next2
        index = 0

        print(counter)
        # print(arr)

if __name__ == '__main__':
    상태관리배열_커서등산시_직전상태초기화하며등산_action및상태값증가시_커서를_0으로내려_직전까지_다시등산([1, 2, 3, 4])
