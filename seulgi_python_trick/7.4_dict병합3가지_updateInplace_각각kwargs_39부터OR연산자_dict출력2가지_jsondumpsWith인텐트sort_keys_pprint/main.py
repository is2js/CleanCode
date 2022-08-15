import sys

input = sys.stdin.readline

if __name__ == '__main__':
    # 7.4 딕셔너리 표현식 특이점

    # True, 1, 1.0 은 모두 같은 것으로 취급된다. (True == 1 == 1.0 의 값은 True 다.)
    # 파이썬은 bool 을 int 의 서브 클래스로 취급한다.
    # 딕셔너리에 기존 키 값에 새로운 값이 업데이트 될 때, 값만 업데이트 하고 키 값 자체는 업데이트 하지 않는다.
    # (그래서 위 예제에서 키가 1.0 이 아니라 여전히 True 다.)
    # -> dict의 key는 t/f로 치환된 뒤, true와 같은 값들은 모두 같은 key의 value로 인식되고
    # -> 제일 마지막 value만 남는다.
    print({
        True: 'yes',
        1: 'yes1',
        1.0: 'yes11',
        False: 'no',
        # []: 'no1', # 빈배열은 값이 False만 hash로는 못온다. hash는 값만 온다.
        0: 'no11',
    })
    # {True: 'yes11', False: 'no11'}

    # 7.5. 딕셔너리를 병합하는 많은 방법
    # -> update 나 {**dict1, **dict2} 형태로 딕셔너리를 병합할 수 있다.
    # -> 파이썬 3.9 부터는 dict1 | dict2 형태의 문법도 추가된다고 한다.
    # (1) .update()
    xs = {'a': 1, 'b': 2, }
    ys = {'b': 3, 'c': 4, }
    # -> update없으면 추가, 있으면 [뒤쪽값으로] 덮어쓰기를 inplace로 한다.
    xs.update(ys)
    print(xs)
    # {'a': 1, 'b': 3, 'c': 4}

    # (2) 각각을 kwarg로 언패킹한 뒤, 다시 { }로 싸기
    ys = {'b': 3, 'c': 4, }
    xs = {'a': 1, 'b': 2, }
    print({**ys, **xs})
    # {'b': 2, 'c': 4, 'a': 1} -> 뒤쪽  b: 2로 덮어쓰기되었다.

    # (3) dict1 | dict2
    print(ys | xs)
    # {'b': 2, 'c': 4, 'a': 1}

    # 7.6. 보기 좋은 딕셔너리
    # json.dumps 나 pprint.pprint 를 사용해서 딕셔너리를 보기좋게 출력할 수 있다.
    # json 은 기본 데이터 타입이 아닌 데이터가 들어올 경우, TypyError 를 내므로 주의해야 한다.

    mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee, }
    import json

    ## json -> json.dumps()로 string형태의 json + indent +정렬까지 할 수 있다.
    print(json.dumps(mapping, indent=4, sort_keys=True))
    # {
    #     "a": 23,
    #     "b": 42,
    #     "c": 12648430
    # }

    ## 이 때, json의 자료형에없는 set 등이 포함된 경우, 에러가 난다.
    mapping['d'] = {1, 2, 3, }
    # print(json.dumps(mapping, indent=4, sort_keys=True))
    # TypeError: Object of type set is not JSON serializable

    # (2) pprint -> pprint.pprint 활용
    import pprint
    pprint.pprint(mapping)
    # {'a': 23, 'b': 42, 'c': 12648430, 'd': {1, 2, 3}}

