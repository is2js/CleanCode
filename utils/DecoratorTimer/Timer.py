# 1. 데코레이터를 함수가 아닌 __enter__와 __exit__ 오버라이딩 class를 생성하되, contextlib.ContextDecorator를 상속해서 만든다.
class Timer(contextlib.ContextDecorator):

    def __init__(self, name) -> None:
        self.name = name

    # 2. enter와 exit를 구현하며, 시작 데코로직을 enter에 / 종료 데코로직을 exit에 구현한다.
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        operation_time = self.end - self.start
        print(f">>[Timer] 수행시간 of {self.name}: {operation_time} sec")