class A:
    name = "class A"

    def __init__(self):
        print("class A init")

class B:
    name = "class B"

    def __init__(self):
        print("class B init")

class C(A, B):

    def __init__(self):
        # 상속한 클래스들의 생성자를 호출을 확인하기 위해
        # 부모 생성자를 super()를 통해서 호출한다.
        super().__init__()


def solution():
    # 파이썬의 다중 상속
    # (1) 메서드 결정 순서 MRO
    # 파이썬에서 다중 상속이 발생할 때, 부모의 어떤 메서드가 먼저 사용될까?
    # 한 마디로 말하면, 상속 순서가 앞쪽에 있는 부모 클래스의 메서드를 사용한다.
    # 정확히는 MRO 알고리즘을 사용하여 메서드 우선순위를 정한다.

    ## 상속한 클래스의 필드를 무료로 사용할 수 있다.
    # -> 상속A, B중에서 앞에 있는 것의 필드를 사용한다.
    print(C.name)
    # class A
    # -> 상속A, B중에서 앞에 있는 생성자를 호출한다.
    print(C())
    # class A init
    # <__main__.C object at 0x000001EE882F9668>

    # (2) 상속 메서드의 우선순위는 클래스.mro()를 통해 확인할 수 있다.
    for element in C.mro():
        # print(element)
        # <__main__.C object at 0x0000028F072FE6D8>
        # <class '__main__.C'>
        # <class '__main__.A'>
        # <class '__main__.B'>
        # <class 'object'>
        print(element.__name__)
        # <__main__.C object at 0x000002468025E6D8>
        # C
        # A
        # B
        # object
    pass
 
 
if __name__ == '__main__': 
    solution() 
