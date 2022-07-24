def func_only_return():
    return


def func_none_return():
    return None


def func_void():
    if True is False:
        return 0


def solution():
    # 3.6. 반환할 것이 없는 경우
    # 파이썬은 함수 내부에 return 문이 없는 경우 None 을 암묵적으로 반환한다.
    # 이를 명시적으로 return None 으로 둘 것이냐, 아니면 굳이 필요없는데 넣을 것이냐의 문제다.
    # 예를 들면 다음의 세 코드는 모두 같다
    # -> 정리
    print(func_only_return())
    print(func_none_return())
    print(func_void())
    # None
    # None
    # None

    #    return이나 return None이나 아예 return에 안걸리고 끝나는 void 3가지 모두 None을 반환한다.

    # -> 명시적으로 void라도 return None을 적어주자.
    pass 
 
 
if __name__ == '__main__': 
    solution() 
