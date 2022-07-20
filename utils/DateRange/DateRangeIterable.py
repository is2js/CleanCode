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