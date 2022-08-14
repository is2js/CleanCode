def solution():
    pass


if __name__ == '__main__':
    ## 제네레이터
    # -> 이터러블(iter) 객체 2개 중
    #    (1) len/getitem의 시퀀스 객체는 iter구현안해도 이터러블 객체에 속한다.
    #    (2) iter/next의 이터레이터 객체를 의미한다.
    #    -> 이 이터러블 - 이터레이터 중 - next에서 return이 아닌 yield로 구현한 객체를
    #    ->  제네레이터라고 한다.

    ## 객체는 class에 iter / next구현후 next안에 yield로 반환해야한다.
    ## for in 에 넣으면 iter호출 -> next호출 -> next에서 return value하거나 yield value한다.
    class SequenceIterator:
        # 1) 기본적으로 움직이는 current_필드가 있어야하며, start_인자를 받아 초기화해줄 수 있다.
        # 2) step과 start, end범위(raise StopIteration)를 가지면 더 좋다.
        # def __init__(self, start=0, end=None, step=1):
        def __init__(self, start=0, step=1):
            self.start = start
            self._current = start
            # self.end = end
            self.step = step

        def __iter__(self):
            return self

        def __next__(self):
            # if self._current >= self.end:
            #     raise StopIteration

            current = self._current  # (3) 지역변수로 챙겨놔야한다.
            # return self._current # (1) 사용해할 값이, 사용 후
            self._current += self.step  # (2) 업데이트를 해야된다면,
            return current


    for number in SequenceIterator():
        print(number)
        if number == 10:
            break


    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10

    ## 함수로도 제네레이터를 구현할 수 있다.
    # -> 반복문 속 1개의 값을 1개씩 return싶은데, return하면 종료되니, yiedl를 쓴다.
    def test_generator_yield():
        for i in range(10):
            yield i


    print(test_generator_yield())
    # <generator object test_generator_yield at 0x0000027A636A3138>
    # 이를 제너레이터 인스턴스라고 하는데, 이는 이터러블이자 이터레이터 객체다.
    # (함수를 호출했는데 객체가 반환되었다. 굉장히 이상해 보일 수 있는데, 파이썬에서 제너레이터를 약간 특수하게 소개하는 이유이기도 한 것 같다.)
    # 따라서, 이 인스턴스를 가지고 반복문을 돌릴 수 있다!
    # 제너레이터는 미리 값을 생성하지 않기 때문에(Lazy), 보통 메모리를 절약하기 위해 사용된다.

    from collections.abc import Iterable, Iterator, Generator
    from itertools import product

    abstracts = Iterable, Iterator, Generator
    concretes = list, tuple, set, dict

    for concrete, abstract in product(concretes, abstracts):
        # print(concrete, abstract)
        print(f"{concrete.__name__}는 {abstract.__name__}를 상속받나요? {issubclass(concrete, abstract)}")
        # list는 Iterable를 상속받나요? True
        # list는 Iterator를 상속받나요? False
        # list는 Generator를 상속받나요? False
        # tuple는 Iterable를 상속받나요? True
        # tuple는 Iterator를 상속받나요? False
        # tuple는 Generator를 상속받나요? False
        # set는 Iterable를 상속받나요? True
        # set는 Iterator를 상속받나요? False
        # set는 Generator를 상속받나요? False
        # dict는 Iterable를 상속받나요? True
        # dict는 Iterator를 상속받나요? False
        # dict는 Generator를 상속받나요? False

    # 추가 공부자료: https://shoark7.github.io/programming/python/iterable-iterator-generator-in-python
    solution()
