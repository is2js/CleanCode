from collections import defaultdict


class CallCount:
    # 1. 생성자에서 호출시 데이터를 저장할 빈 컬렉션 필드를 초기화한다.
    # -> item이 들어오면, default 0부터 카운팅할 수 있게 defaultdict를 만든다.
    def __init__(self):
        self._counts = defaultdict(int)

    # 2. 객체를 함수처럼 호출하기 위해 __call__을 오버라이딩한다.
    # -> 호출시 인자를 받아 default dict에 +=1씩 카운팅하게 한다.
    def __call__(self, *args, **kwargs):
        self._counts[args] += 1
        return self._counts[args]

    pass


def solution():
    # 7. 호출형 객체
    # 매직 메서드 __call__를 구현하면, 클래스의 객체도 함수없이 ()호출형으로 사용할 수 있다.
    # ->
    call_count = CallCount()

    print(call_count(1))
    print(call_count(1))
    print(call_count(1))
    print(call_count(2))
    # 1
    # 2
    # 3
    # 1


if __name__ == '__main__':
    solution()
