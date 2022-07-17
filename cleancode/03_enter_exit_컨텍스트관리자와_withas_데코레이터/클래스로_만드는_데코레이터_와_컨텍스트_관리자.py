import time
import contextlib


# 1. 데코레이터로 class를 생성하되, contextlib.ContextDecorator를 상속해서 만든다.
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


# 3. (시간측정데코)사용할 함수에 컨텍스트관리자로 만든 데코레이터를 붙여서 자동enter/exit가 수행되는지 확인한다.
@Timer("100만번 list comp반복하기")
def a():
    return [i for i in range(1000000)]


@Timer("100만번 for loop로 빈 list에 요소 append하기 ")
def b():
    result = []
    for i in range(1000000):
        result.append(i)
    return result


if __name__ == '__main__':
    # 컨텍스트 관리자(enter, exit구현 클래스)를 with as용이 아닌, 함수가 아닌데도 데코레이터로 사용하는 법
    # @Timer("데코레이터")
    a()
    b()
