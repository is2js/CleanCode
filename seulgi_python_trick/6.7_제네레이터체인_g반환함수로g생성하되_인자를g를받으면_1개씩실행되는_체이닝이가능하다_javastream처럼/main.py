from random import randint


def solution():
    ## 이터레이터를 가진 이터러블과  2가지 생성방법의 제네레이터

    ## 이터레이터 -> class 시작부터 step을 가져 + next메서드안에서 1번에 1개씩 return하고 상태값을 올려 기억
    ##(1) iterable(iter)구현시, self가 아닌 내가 만든 iterator를 반환하기
    # -> __iter__를 구현안해도, 내부에서 Iterable 자료구조를 상속한 기본자료구조들은 for in 에 들어가는 iterable들은 내부적으로 iter를 생성해서 1개씩 반환한다고 한다.
    # -> __iter__ 직접 구현시 iterator를 직접구현해서 반환해줘야한다.

    ##  요약) iterable -> iter시 내부자동생성 or 직접구현한 iterator 반환
    #        iterator -> iter시 self반환 + 상태값 가짐 + next구현

    class RandomIntIterable:
        def __init__(self, n):
            self.n = n

        def __iter__(self):
            # return self
            return RandomIntIterator(self.n)

    # -> iterator는 상태값을 가져서, 1개씩 반환하면서, current값을 1개씩 올린다.
    class RandomIntIterator:
        def __init__(self, n):
            self.n = n
            self.count = 0

        def __iter__(self):
            # iterator는 iter구현시 self를 반환하고, next가 자동호출되도록 한다.
            return self

        def __next__(self):
            # input의 갯수를 아직 못채웟을때만 1개씩 반환해준다.
            if self.count < self.n:
                self.count += 1
                return randint(1, 100)
            else:
                raise StopIteration

    # print(next(RandomIntIterable(5)))
    # TypeError: 'RandomIntIterable' object is not an iterator

    # iterator를 사용하는 iterable은,
    # -> iterator용 next()는 직접적으로 호출못하지만,
    # -> iter가 호출되는 for문안에서는 , iterator가 생성되어 작동한다.
    for x in RandomIntIterable(5):
        print(x)
        # 97
        # 41
        # 44
        # 90
        # 22

    ## 제네레이터 -> function+yield or (제네레이터 comp)로 만들고,
    #              함수안에 컬렉션에 대해 한 1개씩 yield하도록 정의하되
    #              그 컬렉션이 다 메모리에 올라가지 않아 메모리 성능이 좋음.
    #             반복문에 사용하든 or 제너레이터객체를 next()를 호출할 수 있다.

    ## 제네레이터 필요충분조건
    # 1. 클래스가 아닌 함수로 정의한다.
    # 2. 프로토콜처럼 Iterable와 Iterator의 두 요소를 분리하지 않고 한 요소에 담을 수 있다.
    # 3. 호출될 때마다 한 번씩 반환할 값을 반환하는 키워드가 ‘yield’이며, 이는 함수가 아니다.
    #    즉 return 문처럼 ()를 사용하지 않는다.

    # (1) 제네레이터 생성을 위한 [함수 속 yield]
    # -> 제공할 제한 수가 없다면, input -> 함수 속에서 상태값을 가져 제한한다.
    #    n -> count를 0부터  n-1까지 상태값으로 올리기
    def random_number_generator(n):
        count = 0
        while count < n:
            yield randint(1, 100)
            count += 1

    # (2) 제네레이터 객체로 사용한다면, 마치 next( 객체 )하기 전까지의 함수 객체(클로져느낌)이다.
    generator = random_number_generator(5)
    print(generator)
    print(next(generator))  # 상태값count가 내부에서 0 -> 1로 업데이트될 것이다.
    # 51
    print(next(generator))
    # 19
    print(next(generator))
    print(next(generator))
    print(next(generator))
    # 95
    # 26
    # 87
    # print(next(generator))
    # StopIteration

    # (3) 제네리이터 는 comprehension으로 생성할 수도 있다.
    # -> list, dict comp처럼 복잡하지 않은 정도의 generator comp를 구현할 수 있다.
    print((n for n in generator))
    # <generator object solution.<locals>.<genexpr> at 0x000001BACBB7D8B8>

    # -> 함수 속에 들어갈 때, 인자가 1개라면 ()를 생략할 수 있다.
    # -> 프린트를 찍어보니, 지역변수에 담지 않았는데도, 함수객체로서, 식별자를 가지는 것 같다.
    print(n for n in generator)
    # <generator object solution.<locals>.<genexpr> at 0x000001BACBB7D8B8>

    # -> 지역변수로 받아서, 함수+yield로 정의한 제네레이터 객체로 받을 수 있다.
    generator_2 = (n for n in generator)
    print(generator_2)
    # <generator object solution.<locals>.<genexpr> at 0x0000012D266FD8B8>

    ## 제네레이터 체인
    # -> 제네레이터는 함수객체로서 for in이나 next()에 들어가야지 상태값 바꾸면서 1개씩 작동한다
    # -> 이 함수 객체를 다음 제네레이터[함수]의 인자로 체이닝하면, 1개 요소씩 작동할 수 있다.
    # (1) 함수든 genexp이든 제네레이터 객체를 만든다.
    integers = (integer for integer in range(1, 9))

    # -> 이 때, 제네레이터용 함수는, [함수 호출결과가 제네레이터 객체]이다.
    def integers():
        for i in range(1, 9):
            yield i
    # g = integers()

    # (2) 인자로 체이닝 할 수 있게 [함수로 제네레이터]를 만들되, 인자를 generator -> 내부 yield할 iterable이 되게 한다.
    def squared(generator_):
        for i in generator_:
            print(f"{i} -> {i * i}로 변환 중")
            yield i * i

    # (3) 제네레이터 체이닝했어도, 제네레이터용 함수 호출결과가 g객체다.
    chain = squared(integers())
    print(chain)
    # <generator object solution.<locals>.squared at 0x0000015F63C4D9A8>
    # (4) 제네레이터 객체는, for/next()이외에 list자료구조로 변신할 수 있다.
    print(list(chain))
    # 1 -> 1로 변환 중
    # 2 -> 4로 변환 중
    # 3 -> 9로 변환 중
    # 4 -> 16로 변환 중
    # 5 -> 25로 변환 중
    # 6 -> 36로 변환 중
    # 7 -> 49로 변환 중
    # 8 -> 64로 변환 중
    # [1, 4, 9, 16, 25, 36, 49, 64]
    # -----------------> 제네레이터 체인은 1개씩을 순차적으로 작동시킨다.

    # chain 은 한 방향으로 흐르는 일련의 파이프라인을 갖고있다.
    # 위 구조에서 파이프라인은 integers 를 거쳐 squared 로, 그리고 마지막에 list 로 실행된다.
    # 파이프라인의 좋은 점은 단계 별로 할 일을 분리하여 처리할 수 있다는 것이다.
    # 또한 데이터 처리가 '한 번에 한 항목씩' 이뤄진다는 것이다. 즉 체인 처리 단계 사이에 버퍼링이 없다.
    # 체인에 새로운 블록을 추가시키고 싶을 때 다음과 같이 쉽게 붙일 수 있다.

    # (5) 추가 [제네레이터를 인자로 받는 제네레이터용 함수]를 추가 체이닝
    def negated(generator_):
        for i in generator_:
            yield -i

    chain = negated(squared(integers()))
    print(list(chain))
    # [-1, -4, -9, -16, -25, -36, -49, -64]



if __name__ == '__main__':
    solution()
