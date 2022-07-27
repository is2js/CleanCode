from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass



def solution():
    # 추상화 클래스는 상속을 확인한다.
    # - 추상클래스는 상속클래스 자리에 metaclass=ABCMeta를 입력하고, abstractmethod로 정의한다.
    # - 추상메서드는 pass로 비워두면 된다.
    # - 구상클래스는 @Override표시 없이, 그냥 같은 이름의 메서드를 구현한다.
    # 추상화 클래스는 파생 클래스가 인스턴스화될 때, 기반 클래스의 추상 메서드를 모두 구현했는지 확인한다.
    # 추상화 클래스를 사용하면 버그를 방지하고, 클래스 계층을 쉽게 유지 관리할 수 있다.

    # - 추상클래스는 객체를 생성할 수 없다.
    # TypeError: Can't instantiate abstract class Base with abstract methods bar, foo
    # Base()

    # 만약, 구상클래스가 구현을 안하면 에러가 뜬다.
    concrete = Concrete()
    # TypeError: Can't instantiate abstract class Concrete with abstract methods bar


if __name__ == '__main__': 
    solution() 
