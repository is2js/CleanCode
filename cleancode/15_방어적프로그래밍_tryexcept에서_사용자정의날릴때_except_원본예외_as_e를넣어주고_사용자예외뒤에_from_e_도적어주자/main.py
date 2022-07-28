class InternalDataError(Exception):
    pass


def process(data, record_id):
    try:
        return data[record_id];
    except KeyError as e:
        raise InternalDataError("Record not present") from e


def solution():
    # 방어적 프로그래밍
    # 2번째 - 원본 예외 포함
    # 오류 처리 과정에서 [사용자정의] 오류를 발생시키며 메시지를 변경할 수도 있다.
    # -> try-except의 except에서 경우 원래 예외를 포함하는 것이 좋다.
    #    except 원본예외 as e:의 e를 활용한다.
    #    raise 사용자정의예외 from e를 달아주면 된다.

    # 예시로서 메모리db구성 자료구조인 dict를 가지되
    # 존재하지 않는 KeyError를 -> InternalDataError로 정의해서 발생시킨다.
    process({1: "1234", 2: "abcd"}, 3)
    # KeyError: 3
    # __main__.InternalDataError: Record not present

 
 
if __name__ == '__main__': 
    solution() 
