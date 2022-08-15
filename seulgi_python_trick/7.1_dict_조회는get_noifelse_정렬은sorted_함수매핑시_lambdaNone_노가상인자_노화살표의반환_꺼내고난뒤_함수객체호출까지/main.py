def greeting(userid):
    if userid in name_for_userid:
        return f"Hi {name_for_userid[userid]}"
    return f"Hi There"
    pass


def greeting_with_get(userid):
    return f"Hi {name_for_userid.get(userid, 'There')}"


if __name__ == '__main__':
    ## 7. dict 트릭
    # (1) key 존재유무 확인 if else 대신 dict.get( , 기본값)을 쓰자.
    # -> my) dict조회시 key 존재유무 검사를 if로 하지말고 get으로 하자.
    # -> 딕셔너리에 없는 Key 값을 처리해야 할 땐, get 메서드나 collections.defaultdict 을 사용하자.
    name_for_userid = {
        382: "Alice"
    }
    # 지양해야할 코드 -> else문으로 기본값을 반환함.
    print(greeting(382))
    print(greeting(1))
    # 지향해야할 코드 -> get의 2번재 인자로 기본값을 반환함
    print(greeting_with_get(382))
    print(greeting_with_get(1))

    # (2) dict정렬 with sorted
    ## sorted 의 key 와 reverse 파라미터의 인자 값을 활용하여 효과적으로 정렬할 수 있다.
    ## -> key 에는 callable 한 객체(즉 함수나 __call__ 메소드를 가진 클래스)를 주면 된다.
    ## -> 이 객체의 반환 값을 기준으로 모든 요소를 비교한다.
    ## -> reversed 에는 bool 값 (즉 True 나 False) 를 주면 된다. 오름차순, 내림차순을 정할 수 있다.
    xs = {"a": 4, "b": 3, "c": 2, "d": 1, }
    print(sorted(xs))
    # ['a', 'b', 'c', 'd']
    ## sorted에는 dict.items()의 결과물인 iterable을 받을 수 있다.
    print(sorted(xs.items()))
    # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]

    ## sorted는 key에 람다식으로 정렬대상을 반환하는 함수객체를 지정한다.
    print(sorted(xs.items(), key=lambda x: x[1]))
    # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
    print(sorted(xs.items(), key=lambda x: x[1], reverse=True))


    # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]

    # (3) 딕셔너리로 switch/case 문 모방하기
    # -> dict에 callable한 함수객체( ()부르기 전 함수 )를 매핑해서 호출할 수 있다.
    # -> lambda식 value(함수객체)에 대한 기본값은 lambda: None으로 return값을 None으로지정해준다.
    # 파이썬에는 switch/case 문이 문법적으로 없다.
    # 위처럼 코딩하면 긴 if 체인을 다루지 않아도 되고, 좀 더 파이써닉하게 사용할 수 있다.
    # 실제 프로덕션에서 쓸 때는, 딕셔너리를 따로 상수로 빼놓아 한 번만 만들어놓아야 좀 더 이상적이다.
    def dispatch_dict(operator, x, y):
        # lambda식에 들어가는 x, y를 받아올 때는, 가상인자가 아니므로
        # 그냥 가상인자-> 없이 return해주는 식으로 매핑해야한다.
        return {
            "ADD": lambda: x + y,
            "SUB": lambda: x - y,
            "MUL": lambda: x * y,
            "DIV": lambda: x / y,
            # dict를 조회할 땐 무조건 get을 쓰자.
            # 람다식은 함수객체라서,꺼내고 난 뒤 ()로 호출해줘야한다.
        }.get(operator, lambda: None)()

    print(dispatch_dict("ADD", 1, 2))
    # 3
    print(dispatch_dict("ROOT", 1, 2))
    # None
