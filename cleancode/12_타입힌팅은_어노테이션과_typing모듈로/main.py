from typing import List


class MyClass:
    pass


def func(a: int, b: str = None, c: MyClass = None) -> None:
    pass


def func2(a: List[int]) -> None:
    pass


def solution():
    # 타입힌팅 by 어노테이션
    # (1) 파라미터: 옆 = None
    # (2) 함수() -> 끝:
    # (3) 변수: 옆 = 1
    # (4)  List 나 Dict 같은 컬렉션 타입이나 Class 타입은 -> typing 모듈을 사용
    #     -> 파라미터: List[int]
    # 다만 자료구조 복잡해질수록 타입 힌팅도 길어지게 되고, 과연 이게 읽기 좋은 코드인지는 생각해봐야 한다.
    func(1, "abc", MyClass())
    func("abc", "def", MyClass())  # Expected type 'int', got 'str' instead

    a: int = 1
    b: float = 2
    print(b)

    func2([1, 2, 3, 4])

    c: List[int] = [1, 2, 3]
    d: List[float] = [1, 2, 3]
    f: List[str] = [1, 2, 3] # Expected type 'List[str]', got 'List[int]' instead


if __name__ == '__main__':
    solution()
