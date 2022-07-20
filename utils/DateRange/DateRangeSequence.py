class DateRangeSequence:
    def __init__(self, start_date, end_date):
        print("__init__")
        self._start_date = start_date
        self._end_date = end_date
        # 1) __getitem__에 걸릴 컬렉션필드를 들어온 인자들을 이용해 내수용 메서드로 생성한다.
        #    객체 생성시 list를 한번에 처음부터 끝까지 +1씩 증가시키며 생성하는 메서드다.
        #    끝이 정해진 것을 돌리는 게 아니라, 특정조건까지 돌리며 요소를 만들어서 append한다.
        self._range = self._create_range()

    def _create_range(self):
        print("_create_range")
        # 2) 걸릴 컬렉션필드를 생성
        # (1) 빈 list -> (2) while로 start_date부터 +1일씩 업데이트될 변수를 돌려가며
        #     end_date직전까지 +1일하면서 빈 list에 append한다.
        # (2) 다 채워진 list를 반환한다.
        days = []

        current_day = self._start_date # 초기값부터 시작하니, append후 업데이트
        while current_day < self._end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    # 3) getitem을 오버라이딩하되, index를 인자로받고, 범위만큼 생성한list를 인덱싱해서 반환한다.
    #   -> 객체 자체에 인덱싱이 가능해진다.
    def __getitem__(self, day_no):
        print(f"__getitem__({day_no})")
        return self._range[day_no]

    # 4) 생성한 range list의 길이를 반환한다.
    def __len__(self):
        print("__len__")
        return len(self._range)


    @property
    def end_date(self):
        return self._end_date

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
