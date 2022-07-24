class Car:
    def __init__(self, color=None, mileage=None):
        self.color = color
        self.mileage = mileage

    def __repr__(self) -> str:
        print("__repr__ 호출")
        return f"{self.__class__.__name__}({self.color!r})"

    def __str__(self) -> str:
        print("__str__ 호출")
        return f"a {self.color} car"


def solution():
    # 문자열 변환 -> 모든 클래스는 __repr__ 이 필요하다
    # __str__ 및 __repr__ 메서드를 사용하여 자신의 클래스에서 문자열 변환을 제어할 수 있다.
    # __str__ 의 결과는 읽을 수 있어야 한다. -> repr를 안쓰도록 재정의해서 완벽한 문자열을 반환하게 한다.
    # __repr__ 의 결과는 모호하지 않아야 한다. -> live template으로 정의해놓아야할 듯하다.
    #                                         self의.class.name ( 필드!r )형태로 클래스이름( 필드raw값들)을 반환하게 한다
    # 항상 __repr__ 을 클래스에 추가하라.
    # __str__ 의 기본 구현은 __repr__ 을 호출하기만 한다.
    # 따라서 클래스에 최소한의 구현으로 거의 모든 경우에 유용한 문자열 변환 결과가 보장된다.
    car = Car("blue", 10)

    print(car) # repr가 출력된다.
    str(car)
    # __str__ 호출
    # __repr__ 호출 -> 재정의안할 경우 그렇다.


if __name__ == '__main__': 
    solution() 
