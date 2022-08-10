def solution():
    ## 5.5. 스택 (LIFO)
    # (1) list : 간단한 내장 스택
    # -> python에서의 pop가능한 stack
    # -> 리스트는 내부적으로 동적 배열로 구현된다.
    # 리스트 특정 요소 접근에 시간 복잡도 O(1) 만큼 소요된다.
    s = []
    s.append('eat')
    s.append('sleep')
    s.append('code')
    print(s.pop())
    print(s.pop())
    print(s.pop())
    # code
    # sleep
    # eat

    ## 5.6. 큐 (FIFO)
    # (2) collections.deque : 빠르고 강력한 스택
    # 스택(pop)과 큐(popleft)로 모두 사용가능한 자료구조다.
    # -> 데크는 내부적으로는 [이중 연결리스트로 구현]되어 있다.
    # -> 따라서 특정 요소 접근에 [시간 복잡도 O(n)] 만큼 소요된다.
    # -> 스택은 그냥 리스트로. 큐는 데크로 짜는게 맞다고 본다.
    from collections import deque
    q = deque()
    q.append('eat')
    q.append('sleep')
    q.append('code')
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    # eat
    # sleep
    # code

    # 5.7. 우선순위 큐
    # (3) heapq : 리스트 기반 이진 힙
    # -> 원본list(주로 빈[] list의 지역변수)를 인자로 넣어서 inplace적용시키는 특징
    # -> 최소 힙(min heap)으로 구성되어 있으므로 넣었다 빼는 것만으로 O(NlogN)에 오름차순 정렬이 완료된다.
    # --> 보통 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은'원소이기 때문이다

    # heapq.heappush(리스트, 우선순위 == value)  or
    # heapq.heappush(리스트, (우선순위, 아이템)) 과 heapq.heappop(...) 로 우선순위 힙을 구현한다.
    # 최소 힙 구현만 제공하기 때문에 기본적으로 우선순위 값이 오름차순으로 뽑힌다.
    # 최대 힙을 구현하려면 이 우선순위를 그대로 가져가되, 음수(-1)을 곱해주면 된다.
    import heapq as hq

    q =[]
    hq.heappush(q, (2, 'code'))
    hq.heappush(q, (1, 'eat'))
    hq.heappush(q, (3, 'sleep'))

    ## heapopop(q)하면, 우선순위 낮은 순서대로 자동으로 나온다.
    ## stack이든, 우선순위 heapq이든, 기반list가 빈배열되기 전까지 돌린다
    while q:
        print(hq.heappop(q))
    # (1, 'eat')
    # (2, 'code')
    # (3, 'sleep')
    pass
 
 
if __name__ == '__main__': 
    solution() 
