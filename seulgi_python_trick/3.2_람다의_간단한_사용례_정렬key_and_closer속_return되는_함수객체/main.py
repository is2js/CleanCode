def solution():
    # 3.2. 람다는 단일 표현식 함수다
    #  간단한 익명함수 작성이 가능하다. 또한, 편리하고 "비격식적인" 지름길을 제공한다.
    # 1. 가장 흔한 사례는 정렬에 사용하는 key 함수를 작성하는 것이다.
    tuples = [
        (1, 'd'),
        (2, 'b'),
        (4, 'a'),
        (3, 'c'),
    ]
    print(sorted(tuples, key=lambda x: x[1]))

    # [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]

    # 2. 클로저 : 클로저로써 함수 팩토리를 사용하는 사례도 있다.
    #    cf) my) 클로저는 return문에 지역메서드 함수객체를 외부에서 반환했음에도, 지역변수 등의 지역상태를 기억하고 있는 상태다.
    def make_adder(n):
        # 반환된 람다 함수객체는, 입력된 지역변수n을 기억된 상태로, x에 대해 -> x + n를 수행한다
        return lambda x: x + n

    # -> 함수객체의 특정인자를 지역변수로서 먼저 인식시키는 클로저를 사용한 뒤
    #    나머지 인자를 외부에서 입력받기
    plus_3 = make_adder(3)  # n=3 -> x+3
    plus_5 = make_adder(5)  # n=3 -> x+5
    print(plus_3(2))  # 5
    print(plus_5(2))  # 7

    # 3. 람다 함수를 자제하는 경우
    # 람다 함수로는 간단한 일만 해야한다. 다음 예를 보면 확 와닿을 것이다.
    ## bad case : 람다를 이용해 filter()로 필터링한 뒤 list화
    print(list(filter(lambda x: x % 2 == 0, range(16))))
    ## good case: 필터링하는데는 굳이 람다를 이용할 필요없다.
    #      -> 반복문+필터링은 listcomp를 활용한다.
    print([x for x in range(16) if x % 2 == 0])


if __name__ == '__main__':
    solution()
