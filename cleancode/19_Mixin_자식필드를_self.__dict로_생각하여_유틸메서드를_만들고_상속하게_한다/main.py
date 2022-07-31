import json
import pickle


class Serializer:
    def to_json(self):
        print(f"저는 self.__class__.__name__: {self.__class__.__name__}의 self.__dict__: {self.__dict__}입니다.")
        return json.dumps(self.__dict__)

    def to_pickle(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, path)


## 유틸메서드를 정의한 Mixin클래스를 상속받으면
# -> 무료로 유틸메서드를 사용할 수 있다.
# -> 이 때, 유틸메서드에 정의된 self.__dict__는 내 필드들을 dict로 만들어서 json을 만들 때 사용된다.

class A(Serializer):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b


def solution():
    # 믹스인 (Mixin) 클래스
    # -> 유틸메서드(상태없이 in->out)를 구현하고, 다른클래스가 상속받아 공짜로 사용한다.
    # --> [상속받는 클래스의 상태값(필드들)을 사용하기 위해 self.__dict__같은 메직메서드를 사용해서 정의한다.
    # --> 이 때, self는 상속받은 클래스의 객체를 의미하게 된다.

    # -> 행위을 캡슐화해놓고, 상속만 받으면, 코드가 재사용되는 클래스
    # --> 유틸을 만들어내기 위한 라이브러리도 자주 사용되는 것 같다. ex> json, pickle
    a = A(1, 2)
    print(a.to_json())
    # 저는 self.__class__.__name__: A의 self.__dict__: {'a': 1, 'b': 2}입니다.
    # {"a": 1, "b": 2}
    pass


if __name__ == '__main__':
    solution()
