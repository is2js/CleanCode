def a(*args):
    print(f"type(args): {type(args)}")
    print(f"args: {args}")

    # print(f"type(*args): {type(*args)}")
    # print(f"*args: {*args}")
    pass


# (1) 외부에서는 컬렉션 값들을 콤마로 가변배열을 입력해주면
def vector_addition(*vector_variables):
    # (2) 함수 내에선 *를 떼서 컬렉션요소들의 가변배열을 tuple로 묶을 수도 있지만,
    print(vector_variables) # ([1, 3], [2, 4], [6, 7])
    # (3) 언패킹된 *vector_variables를 그대로 쓰면, 값들이 인자로서 콤마들로 들어간다.
    print(*vector_variables) # [1, 3] [2, 4] [6, 7]
    # (4) zip은 2중 컬렉션이 아니라, 단일 컬렉션들을 콤마로 받는 메서드다
    #  -> zip(a, b, c) -> 그러므로 콤마 입력 그대로 쓰기 위해 언패킹을 유지한다.
    print(*zip(*vector_variables)) # (1, 2, 6) (3, 4, 7)
    # (5) 즉, 인자의 가변배열(콤마)상태를 그대로 들고와 zip에 입력할 때 사용한다.
    # -> zip은 단일컬렉션 가변배열을 받아, 각 인덱스가 같은 요소들끼리 모아서 튜플로 반환해준다.
    # --> [1, 3] [2, 4] [6, 7] -> [ (1, 2, 6 ), (3, 4, 7) ]
    # ---> [sum(1,2,6), sum(3,4,7)] -> [ 9, 14]
    print([sum(i) for i in zip(*vector_variables)]) # [9, 14]


    # return [sum(i) for i in zip(vector_variables)]


def keyword_addition(**kwargs):
    # print(**kwargs) -> 키워드 파라미터는 **를 떼곤 못쓴다.
    print(kwargs) # {'key': '키', 'value': '밸류'}
    pass


def solution():
    # 1. * 인자는 외부에선 콤파의 튜플입력 -> 함수 내에서 *를 떼면, 튜플이다
    a(1, 2, 3, 4)
    # type(args): <class 'tuple'>
    # args: (1, 2, 3, 4)

    # (1) 인자를 1개만 줘도 튜플로 인식한다.
    a(1)
    # type(args): <class 'tuple'>
    # args: (1,)

    # (2) 함수 내에서 *를 붙이면 언패킹 상태로 여러 값들이 콤마로 입력된다.
    # -> 파라미터는 *를 붙이되, 함수내에선 *를 떼고 튜플로 사용한다.
    # type(*args) ->TypeError: type() takes 1 or 3 arguments -> 3개의 값이 콤마로들어간다.
    # print(*args) -> print(f"*args: {*args}") : SyntaxError: can't use starred expression here
    # -> f-string의 { }는 인자가 들어가는게 아니라 변수가 들어가서 에러난다.

    # (3) 인자로는 *를 붙여 언패킹 할 수 있다. print에 튜플이 아닌 여러값들이 들어간다.
    # -> [인자의 *]는 언패킹, [파라미터의 *]는 이미 언패킹한 값들이 콤마로 입력된 상태를 의미한다.
    # -> 함수내에선 *args 이미 언패킹한 상태를 -> args로 패킹해서 튜플로 사용한다.
    b = [1, 2, 3, 4]
    print(b)
    # [1, 2, 3, 4]
    print(*b)
    # 1 2 3 4

    # (4) 인자로는 list나 tuple을 1단계 언패킹할 때 사용한다.
    c = ((1, 2), (3, 4))
    d = [[1, 2, 3, 4]]
    print(*c) # (1, 2) (3, 4)
    print(*d) # [1, 2, 3, 4]

    # 정리 -> *args파라미터는 외부에서 콤마로 입력하지만, 내부에서는 묶어서 사용할 가변배열로 생각한다.

    # 2. *가변배열(외부콤마, 내부tuple묶기)는 언제 사용할까 -> zip()과 연계한다.
    # (1) 안에서 묶이지만, 외부에서는 입력편의성을 위해 콤마로 언패킹한 상태로 입력하게 한다.
    vector_addition([1, 3], [2, 4], [6, 7])
    # vector_addition(1)

    # 정리
    # 파라미터*args : 외부에서 콤마로 가변배열 입력을 유도하며, 내부에서 가변배열을 변수로서 유지할 수 있게 한다. -> 컬렉션 가변배열이면 zip(*args)에 넣을 수 있다.
    #              : *를 뗀 args는 tuple로 요소들을 묶어서, 가변배열입력을 tuple배열로 만든다.
    #  인자*args : 외부의 컬렉션의 괄호를 제거하고 콤마상태의 가변배열을 함수에 입력하는 언패킹입력 역할이다.


    # 3. **kargs: 외부에서 가변배열 이후 입력한 키워드인자에 대해, **를 때면 dict로 패킹해준다.
    # -> 함수내부에선 무조건 dict형태로만 사용해야한다. **를 떼고는 사용 못한다.
    keyword_addition(key="키", value="밸류")






if __name__ == "__main__":
    solution()
