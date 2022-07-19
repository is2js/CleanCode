class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__mangling = "username"

    pass

    def make_object(self, class_):
        return class_()

    @property
    def bar(self):
        return self._bar

    def __enter__(self):
        print("__enter__ 진입")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ 진입")


def get_two_values():
    return 1, 2


def solution():
    test = Test()
    print(test.foo)
    # 1-1. _var 필드 : 내수용 private으로 접근하지말라는 -> action으로 property 생성 가능
    # -> 인터프리터에 런타임에러로는 걸리지 않고 접근가능하지만, 경고창이 뜬다.
    # --> 객체의 인터페이스로 공개하는 용도가 아니라면, 모든 멤버에 접두사로 _ 를 달아주는 것이 좋다
    print(test._bar)

    # -> 이는 property자동생성으로 [_을 뗀 필드명]의 getter로 접근할 수 있다.
    print(test.bar)

    # 1-2. parameter_
    # -> paramter명에 예약어(키워드변수)와 충돌을 피하게 짓기 위해 사용한다
    # -> ex) class_
    print(test.make_object(Test))

    # 1-3. _  변수: 값을 반환받지만, 사용하지 않을 때
    # -> ex) 반복문 for _ 으로 index사용없이 반복만 이용하기
    # -> 튜플 반환시 하나는 _
    a, _ = get_two_values()
    print(sum([1 for _ in range(10)]))

    # 2. __변수 or __함수의 네임 맹글링 -> 비권장
    # -> 네임 맹글링(__ 을 붙이는 것)은 변수의 이름 앞에 클래스의 이름을 붙여준다.
    #    이는 여러 번 확장되는 클래스의 메서드를 이름 충돌 없이 오버라이드 하기 위해 만들어졌다.
    # -> 변수의 경우 _클래스__변수 로 접근 가능해진다.
    # --> 이러한 네임 맹글링을 통해 접근 제어자 private 의 효과를 본다고 생각하여,
    #     _ 대신 __ 을 사용하여 변수를 사용하는 코드들이 일부 있다.
    #     하지만 이런 목적으로 네임 맹글링을 사용하는 것은 일부 부작용 효과를 불러일으키기 때문에 권장되지 않는다.
    # print(test.__mangling)
    # TypeError: __init__() missing 1 required positional argument: '_Test__mangling'
    print(test._Test__mangling)

    # => private 를 표현하고 싶다면 _ 만 사용하자. 애초에 파이썬은 접근 제어자를 강제하는 철학을 가지고 있지 않다.

    # 3. __var__ = 매직메서드 = Dunder
    # ex> __enter__ 오버라이딩 -> exit도 같이 오버라이딩해야 with as에서 자동호출 되는 컨텍스트 관리자가 된다.
    with Test() as test:
        print("컨텍스트 관리자의 enter, exit는 with as 등에 진입할 때만 호출된다.")
        # 평상시 객체 생성 사용에서는 호출 안된다.


if __name__ == '__main__':
    solution()
