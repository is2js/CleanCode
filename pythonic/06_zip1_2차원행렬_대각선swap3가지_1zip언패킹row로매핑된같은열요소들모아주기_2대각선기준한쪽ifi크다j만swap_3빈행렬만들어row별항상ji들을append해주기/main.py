import pprint
import random
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 2차원 list 뒤집기
    mylist = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    for row in mylist:
        print(*row)
    ## not pythonic
    # -> 역순이랑은 다른 개념이다. -> 역순은 row만 뒤집는다.
    # -> 원본 유지한 체 정렬한다면 sorted()를 활용한다.
    # pprint.pprint(my_list[::-1])

    ##  대각 swap을 시도한다면? => 실패..
    ##  엄청 복잡해진다. => i==j기준으로 한쪽만 생각해서 좌표바꿔 스왑하면 된다.
    # # 이중for문 i, j에서... i, j -> 대각은? cf) 1차원 반대index = len - 1 + i
    # # -> 각 대각선index k는?  1->1, 2by2-> 3, 3by3 -> row + (row-1) , NbyN -> 2N-1개의 대갓선
    # diagonal_count = 2 * len(my_list) - 1
    # for k in range(diagonal_count):
    #     # 대각선 반대index는... (0,0)  (1,0) (0,1)   (2,0) (1,1) (0,2)  (3,0) (2,1) (1,2) (0,3)
    #     # => 합이 x+y k로 일정한 특징 && x,y좌표만 바꿔주면 동일하니, 절반까지만 움직이면 된다?
    #     # (k,0)부터 시작해서 1씩 줄면서 (0,k)까지 간다.
    #     # 갯수는 총 k개다.. => 가운데 or 왼쪽을 의미하는 양쪽 인덱스 합의 절반까지만 진행하면 된다? 갯수로는 len - 1 // 2
    #     k_len = k + 1
    #     k_half_len = k_len // 2
    #     for i in range(0, k_half_len):
    #         # 절반까지는 작용
    #         if k - i <= len(my_list) - 1:
    #             print("swap until half")
    #             my_list[k - i][0 + i], my_list[0 + i][k - i] = my_list[0 + i][k - i], my_list[k - i][0 + i]
    #         #절반이후로는.. 0번째 컬럼이 아니며, 총갯수도 다르다...
    #         else:
    #
    # for row in my_list:
    #     print(*row)

    ## (1) i, j 중 기준대각선에서 한쪽만 선택한 뒤, ji와 스왑하면 대각선 swap이다.
    # for i in range(len(my_list)):
    #     for j in range(len(my_list[i])):
    #         if i > j:
    #             my_list[i][j], my_list[j][i] = my_list[j][i], my_list[i][j]
    #
    # for row in my_list:
    #     print(*row)

    ## (2) 똑같은 형태의 2차원 빈행렬을 만들어놓고, row마다 j,i를 append시킨다.
    # -> swap이 아니라 swap될 좌표의 요소를 빈 row별로 채워넣는다.
    # swapped_lst = [[] for _ in range(len(my_list))]
    # for i in range(len(my_list)):
    #     for j in range(len(my_list[i])):
    #         # 원래는 i,j를 집어넣어야하지만, j,i를 append한다.
    #         swapped_lst[i].append( my_list[j][i])
    #
    # for row in swapped_lst:
    #     print(*row)

    ## pythonic -> zip을 이용해서 대각선 swap
    # -> 2차원 lst를 *언패킹하면 row 튜플이 된다.
    # -> zip()을 씌우면, row별 같은 칼럼의 요소들이 동시에 뽑힌 튜플리스트가 된다.
    print(list(zip(*mylist)))
    # -> 튜플 리스트를 list 리스트(2차원 배열)로 바꾸려면, map(list, ))을 활용하면 된다.
    print(list(map(list, zip(*mylist))))
    # -> 길이가 다른 것들이 zip 에 들어가면, 짧은 것 기준으로 끝난다.
    # -> zip은 암묵적index매핑된 여러 배열들의 각 요소를 동시에 뽑아 모아쓸 수 있다.
    #    2차원 행렬은, row별로 각각 index에 매핑된 것으로 볼 수 있다.
    # -> 만약 동물별 울음소리를 각 배열마다 매핑해놨다면, zip으로 묶어서 동시에 뽑아보되,
    #   list대신 dict를 씌우면, 2 중에 먼저 뽑힌 것을 key 뒤에것을 value로 매핑할 수 있다.
    animals = ['cat', 'dog', 'lion']
    sounds = ['meow', 'woof', 'roar']
    sounds2 = ['meow', 'woof', 'roar']
    print(list(zip(animals, sounds)))  # [('cat', 'meow'), ('dog', 'woof'), ('lion', 'roar')]
    print(dict(zip(animals, sounds)))  # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
    # print(dict(zip(animals, sounds, sounds2)))

    composite1 = ['cat', 'dog']
    composite2 = ['a', 'b', 'c', 'd', 'e']

    composite = random.choice([composite1, composite2])
    if len(composite) == 2:
        graph = dict(zip(list('yn'), composite))
    else:
        graph = dict(zip(range(1, len(composite) + 1), composite))
    print(graph)
