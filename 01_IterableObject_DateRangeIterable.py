from datetime import date, timedelta


class DateRangeIterable:
    def __init__(self, start_date, end_date):
        self._start_date = start_date
        self._end_date = end_date
        # 2) next구현을 위해, _private 인덱스변수를 시작값으로 초기화한다.
        self._present_day = start_date

    def __iter__(self):
        print("__iter__호출")
        return self

    def __next__(self):
        print("__next__호출")
        # 1) index개념의 변수를 객체의 _private필드로 만들고, start값으로 초기화한다.
        # 3) __next__의 종료조건은 raise StopIteration이므로 먼저 종착역을 설정한다.
        if self._present_day >= self._end_date:
            raise StopIteration
        # 4) 반복되는 동안, index변수업데이트 전에 초기값을 지역변수로 저장해놓고 -> +1 업데이트 이후 -> 저장한 값을 반환만 해준다.
        # -> 업데이트해야하는데, 반환시에는 기존값을 반환해야한다면, 지역변수로 빼놔야한다.
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @end_date.setter
    def end_date(self, value):
        self._end_date = value


def solution():
    # 사이의 day를 하나씩 반환하는 Iterable클래스() 사용 생성후 -> Iterable객체를 만든다.
    #  -> datetime패키지의 timedelta + date모듈이 필요하다.
    #  -> class는 내부에 __iter__를 구현하며 self(객체 자신)을 반환한다.
    #  -> class는 내부에 __next__를 구현하며, raise StopIteration에 걸리기 전까지
    #     timedelta(days=)를 이용해, start_date로 시작한 변수를 업데이트시키면서, 기존 값을 반환한다.

    date_range_iterable = DateRangeIterable(date(2019, 1, 1), date(2019, 1, 5))
    for day in date_range_iterable:
        print(day)
    # __iter__호출 -> 반복문위에서 1번만 호출되며, iterator객체(self)를 반환후, 다음부터는 __next__가 호출 된다.
    # __next__호출
    # 2019-01-01
    # __next__호출
    # 2019-01-02
    # __next__호출
    # 2019-01-03
    # __next__호출
    # 2019-01-04
    # __next__호출 -> 마지막 호출은 raise StopIteration에 의해 종료된다.


    # [이터러블, 이터레이터, 제너레이터]
    # 이터러블은 __iter__ 를 구현하여 반복 구문을 사용할 수 있게 정의한 객체다. 즉 for i in A: ... 구문을 쓸 수 있도록 하는 객체다.
    # (시퀀스 객체로도 가능하지만, 일반적으로 반복을 기대한다면 이터러블 객체가 맞다.)
    # __iter__ 는 이터레이터를 반환해야 한다.
    #
    # 이터레이터는 __next__ 를 구현하여 한 번에 하나씩의 값을 생산하는 로직을 정의한 객체다.
    # 이터러블에서 쓰이지만, 이터러블 그 자체는 아니다. 예를 들어 다음 코드를 보자.
    # class SequenceIterator:
    #  def __init__(self, start=0, step=1):
    #      self.current = start
    #      self.step = step
    #
    #  def __next__(self):
    #      value = self.current
    #      self.current += self.step
    #      return value

    # 위 객체는 이터레이터(__next__ 가 존재)지만 이터러블은 아니다. (__iter__ 가 없기 때문)
    # 다만 위가 일반적인 경우는 아니고, 보통은 객체에 이터러블과 이터레이터 둘 다 구현한다.

    # 제너레이터는 yield 문을 포함하고 있는 함수다.
    # 즉 위의 객체에서 __next__ 가 return value 가 아니라 yield value 가 되면, __next__ 함수는 제너레이터 된다.
    # 제너레이터를 호출하면 제너레이터의 인스턴스를 만든다. 다음의 예를 통해 확인할 수 있다.
    # def test_a():
    #     for i in range(10):
    #         yield i
    #
    # >>> test_a()
    # >>> <generator object test_a at 0x1096c8550>

    # 이를 제너레이터 인스턴스라고 하는데, 이는 이터러블이자 이터레이터 객체다. (함수를 호출했는데 객체가 반환되었다. 굉장히 이상해 보일 수 있는데, 파이썬에서 제너레이터를 약간 특수하게 소개하는 이유이기도 한 것 같다.)
    # 따라서, 이 인스턴스를 가지고 반복문을 돌릴 수 있다!
    # -> 제너레이터는 미리 값을 생성하지 않기 때문에(Lazy), 보통 메모리를 절약하기 위해 사용된다.


 
if __name__ == '__main__':
    solution()
