def solution():
    # 2. 방어적 프로그래밍
    # 2.1. 에러 핸들링

    # 1) 값 대체
    #   잘못된 값을 생성하거나 프로그램 전체가 종료될 위험이 있을 경우, 결과 값을 안전한 다른 값으로 대체하는 것이다.
    #  -> 일반적으로 '기본 값' 을 쓰는 것을 말한다.
    # (1) dict에서 값을 꺼낼 때, get의 2번재 인자값에 기본값을 준다.
    configuration = {
        "db_port" : 5432,
        "db_host_none" : None,
        "db_host_false" : False
    }
    # 만약, db주소가 dict안에 아예
    # get()의 기본값은, False도 None도 아닌 아예 할당안해서 key가 없을 경우만 기본값으로 대체한다.
    # print(configuration.get("db_host_none", "localhost"))
    # print(configuration.get("db_host_false", "localhost"))
    print(configuration.get("db_host_not_allocate", "localhost"))
    # None
    # False
    # localhost


    # (2) False가능성 있는 값객체에 [or 기본값(값은 항상참)]을 주자.
    빈문자열은_False다 = ""
    영은_False다 = 0
    빈컬렉션은_False다 = []
    빈컬렉션은_False다2 = dict()
    빈컬렉션은_False다3 = list()
    None은_False다 = None
    false_candidates = [
        "",
        0,
        [],
        dict(),
        list(),
        tuple(),
        None
    ]

    for false_candidate in false_candidates:
        variable = false_candidate or "기본값"
        print(variable)


if __name__ == '__main__':
    solution()