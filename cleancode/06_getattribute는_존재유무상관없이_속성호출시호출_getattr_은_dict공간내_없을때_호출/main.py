class Myclass:
    def __init__(self, attribute=None):
        self._attribute = attribute

    # (1) 호출한 필드명이 iterable item으로 들어온다.
    #     존재하든 안하든 일단 호출된다. -> 그다음에 getattr(item)이 호출된다.
    def __getattribute__(self, item):
        print(f"__getattribute__({item})이 호출 됨")
        # 오버라이딩후 특별처리는 안할 것이므로, 부모것 __getattribute__ 그대로 반환
        # -> __dict__에 있는지 검사후, 그 필드값을 반환할 것이다.
        return super().__getattribute__(item)

    # (3) 객체가 __dict__공간에 필드를 소지안하고 있을 때,여기가 호출 된다.
    # -> AttributeError 대신 내가 메세지를 주고 싶은 변수들에 한해 예외처리를 할 수 있다.
    # -> 여기서는 no_로 시작하는 필드에 대해 AttributeError대신 예외문자열을 반환한다.
    def __getattr__(self, item: str):
        print(f"__getattr__({item})이 호출 됨")
        # (3-1) 없는 변수의 이름에서 특정처리후, 나만의 예외를 발생시킨다.
        if item.startswith("no_"):
            name = item.replace("no_", "")
            return f"no_아래에 {name}이라는 속성은 없습니다~!"

        # (3-2) 기본적인 없는 필드에 대한 예외
        raise AttributeError

    @property
    def attribute(self):
        return self._attribute


def solution():
    # 6. 객체의 동적인 속성
    # myObject.attribute 와 같이 객체의 속성을 호출하는 경우, 다음의 과정을 거친다.
    #
    # 1) myObject.attribute 호출
    # 2) __getattribute__ 호출 -> 해당 attribute가 없어도 일단 호출
    # 3) attribute 가 객체의 __dict__ 에 없는 경우 -> __getattr__ 를 호출한다.

    # (1)
    my_class = Myclass("hi~")
    print(my_class.attribute)
    # __getattribute__(attribute)이 호출 됨 -> 프로퍼티
    # __getattribute__(_attribute)이 호출 됨 -> 실제 속성
    # hi~

    # (2)
    print(my_class.no_attribute)
    # __getattribute__(no_attribute)이 호출 됨 -> attribute 가 객체의 __dict__ 에 없어도 일단 __getattribute__가 호출된다.
    # -> 동적으로 필드를 찾는다는 의미이다. -> 없으면 __getattr__를 호출하여 default로 AttributeError를 발생시킨다.
    # AttributeError: 'Myclass' object has no attribute 'no_attribute'
    # --> 없는 필드에 대한 추가처리를 여기서 해주자.

    # (3) 객체 미소유 필드를 호출 했을 때 호출되는 __getattr__내부에
    #    no로 시작하는 필드라면, 예외처리를 default AttributeError대신 문자열 반환하게 해주었다.
    print(my_class.no_attribute)
    # __getattribute__(no_attribute)이 호출 됨
    # __getattr__(no_attribute)이 호출 됨
    # no_아래에 attribute이라는 속성은 없습니다~!






if __name__ == '__main__': 
    solution() 
