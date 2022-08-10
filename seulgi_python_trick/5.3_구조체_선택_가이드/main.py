class Car:
    def __init__(self, color, automatic, mileage):
        self.color = color
        self.automatic = automatic
        self.mileage = mileage

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color!r}, {self.automatic!r}, {self.mileage!r})"

    pass


def solution():
    ## 5.3 레코드별 구조체 / 데이터전송객체
    # 배열과 비교하여 레코드 데이터 구조는
    # 고정된 수의 필드를 제공하며,
    # 각 필드는 이름을 가질 수 있고, 서로 다른 타입을 담을 수 있다.

    ## 선택 가이드
    # 몇 개(2~3)의 필드만 갖고 있다. -> 튜플
    #   필드 순서를 기억하기 쉽거나, 필드명이 불필요 한 경우. 튜플을 사용하자.
    #   ex. 삼차원 공간에서의 점 : (x, y, z)

    # 불변 필드가 필요하다.
    #   일반 튜플,
    #   collections.namedtuple,
    #   typing.NamedTuple 가 좋은 옵션이다.

    # 오타가 발생하지 않도록 필드 이름을 고정할 필요가 있다.
    # collections.namedtuple, typing.NamedTuple 사용

    # 간단하게 유지하기를 원한다. -> dict
    # 일반 딕셔너리 객체는 JSON 과 매우 비슷한 편리한 구문을 제공하므로, 좋은 선택일 수 있다.

    # 데이터 구조를 완전히 제어할 필요가 있다. -> class
    # @property 의 세터와 게터를 사용하여 사용자 정의 클래스를 작성해야 한다.

    # 객체에 동작을 추가해야 한다. -> class
    # 사용자 정의 클래스를 작성하거나, collections.namedtuple 혹은 typing.NamedTuple을 확장하여 작성한다.

    # 데이터를 디스크에 저장하거나, 네트워크로 전송해야 해서 데이터를 일려로 빽빽하게 담아야 한다.
    # struct.Struct 를 사용하는 것이 좋다.

    # 안정적이고 기본적인 선택은? -> typing.NamedTuple
    # typing.NamedTuple 이 파이썬 3.x 에서 레코드 구조체 구현을 위한 일반적인 권장사항이다.







    ## dict
    # 딕셔너리를 사용하여 작성된 데이터 객체는 변경 가능하며, 필드는 언제든지 바뀔 수 있다.
    # -> db가 없을 때 key를 id로 써서 value로 record를 사용할 수 있음.
    # -> record별로 쓴다면 key에 필드명, value에 데이터를 가져간다.
    car1 = {
        'color': 'red',
        'mileage': '3812.4',
        'automatic': 'true',
    }
    # dict자체에 멋진 repr이 있어서 따로 정의도 안해줘도 된다.
    print(car1)
    # {'color': 'red', 'mileage': '3812.4', 'automatic': 'true'}

    ## tuple
    # 불변 객체 record을 만든다. -> 필드이름이 없다.
    # 튜플은 딕셔너리와 달리 불변 객체다. 따라서 변경에 따른 버그를 유발하지는 않는다.
    car1 = ('red', 3812.4, True)

    # tuple 자체에 멋진 repr이 ('red', 3812.4, True)
    print(car1)

    ## 사용자 정의 클래스
    # 클래스를 사용하면 데이터 객체에 대한 "청사진"을 정의하여 모든 객체가 동일한 필드 집합을 제공하도록 할 수 있다.
    # 메써드를 추가함으로써 동작을 구현할 수 있다. 다만 이러한 구현은 이 클래스가 더 이상 일반 데이터 객체가 아니라는 것을 의미하기도 한다.
    car1 = Car('red', 3812.4, True)

    # 클래스부터는 객체출력을 위한 repr를 정의해줘야한다.
    print(car1)
    # Car('red', 3812.4, True)

    ## collections.namedtuple : (메서드없이) 편리한 데이터 객체
    # 잘 사용하면 클래스보다는 가볍고, 딕셔너리보다는 안정성있고(불변이기 때문) 의도가 명확한 레코드를 만들 수 있다.
    # 내부적으로는 클래스로 구현된다. 다만 메모리 사용량이 일반 클래스보다 더 좋으며 튜플만큼 효율적이다.
    from collections import namedtuple
    # 빈칸으로 필드를 정의해서 불변클래스를 생성한다
    namedCar = namedtuple('Car', 'color mileage automatic')
    print(namedCar)
    # <class '__main__.Car'>
    car1 = namedCar('red', 3812.4, True)
    print(car1)
    # namedtuple에도 멋진 repr가 있다.
    # Car(color='red', mileage=3812.4, automatic=True)

    # 불변클래스로 수정이 안된다.
    # car1.mileage = 12
    # AttributeError: can't set attribute


    ## typing.NamedTuple
    # namedtuple 과 매우 흡사하며,
    # -> 주요 차이점은 새로운 레코드 타입을 정의하고, 타입 힌트를 지원할 수 있다는 점이다.
    # -> 상속해서 클래스로 만든다.
    from typing import NamedTuple
    class typingCar(NamedTuple):
        color: str
        mileage: float
        automatic: bool

    car = typingCar('red', 3812.4, True)
    print(car)
    # typingCar(color='red', mileage=3812.4, automatic=True)

    ## types.SimpleNamespace : 세련된 속성 접근
    #파이썬 3.3에서 추가됐다.
    #딕셔너리에서 사용하는 obj['key'] 문법 대신 obj.key 방식으로 속성에 접근할 수 있다.
    # -> my) dict kwargs처럼 생성하는데, .속성으로 접근/변경이 가능하다
    # typing이 아니라 types에 있다.
    from types import SimpleNamespace
    car = SimpleNamespace(color='red', mileage=3812.4, automatic=True)

    print(car)
    # namespace(automatic=True, color='red', mileage=3812.4)
    car.mileage = 12
    print(car)
    # namespace(automatic=True, color='red', mileage=12)

    ## 새속성 추가 및 속성삭제가 가능하다.
    car.windshield = 'broken'
    del car.automatic
    print(car)
    # namespace(color='red', mileage=12, windshield='broken')

    pass
 
 
if __name__ == '__main__': 
    solution() 
