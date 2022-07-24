def solution():
    # 참고 사이트: https://shoark7.github.io/programming/python/how-python-evaluates-conditional-expression
    # https://devpouch.tistory.com/61
    # 요점 정리
    # 식별자:동일성:두 변수가 동일한(identical) 객체를 가리키는 경우, is 표현식은 True 로 평가된다.
    # 값:동등성:두 변수가 동등한(equal: 내용이 같은) 객체를 가리키는 경우,== 표현식은 True 로 평가된다
    # -> 변수를 변수에 재할당한다면, 같은 메모리주소를 보는 변수(메모리주소 별명) 추가 개념일 뿐이다.
    # -> 변수에 배열이 값을 담고 있을 땐 -> slicing을 통한 얕은 복사를 한다면,  깊은 복사라 할 수 있다.
    #                                -> 1차원 값배열만 slicing으로 깊은 복사하자.
    # -> 변수에 객체 요소를 담고 있을 땐 -> slicing은 얕은 복사일 뿐이다.(객체 꺼내서 조작 가능)
    #                               -> deepcopy를 통한 깊은 복사를 해야한다.
    # -> 변수에 값을 재할당한다면,  값에 따라 새로운 메모리주소가 잡힌 변수가 된다.

    a = [1, 2, 3]
    # [기존 변수를 변수에 할당에 사용]한다는 말은, temp로서 [기존 변수 업데이트(다른식별자)가 되기 전 같은 메모리주소의 사본 저장]
    b = a

    c = [1, 2, 3]

    # 변수는 메모리주소의 별명이며, 식별자며 id다.
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}") # 변수에 기존 변수 할당은, 식별자 통째로 복사다.
    print(f"id(c) = {id(c)}") # 같은 값의 할당이라도, 식별자가 다르다.
    print(a == b) # [==]는 값만 비교다 -> 기존변수 할당은 통째로 복사하니 id같아 값도 같다.
    print(a is b) # [is]는 식별자(id, 객체, 메모리주소) 비교다.
    print(a == c) # 값은 같으니 같다
    print(a is c) # 값만 같고, 변수는 달라 식별자가 다르다.

    x = 1
    y = 2
    temp = x
    print(id(temp), id(x)) # 기존변수를 업데이트 안한다면, 메모리주소가 같은 곳을 바라보는 사본 식별자가 된다.
    x = 2
    print(id(temp), id(x)) # 기존변수에 새로운 값을 넣은 순간, 새로운 메모리주소의 식별자가 된다.(변수는 우항의 값에 대한 메모리주소다.)
    print(temp + y) # 기존변수 업데이트 전에 사본을 떠놓은 것을 current값계산에 사용한다.


    # java와 비교한 python의 boolean
    # (1) 빈 문자열empty""은 [비교식]에서는 식별자가 할당되어 is not None이지만, [if문]에서는 False다
    print(r'"" is',  "Not none" if "" is not None else "None")   # True
    print(r'"" is', "True" if "" else "False") # False

    # (2) 공백 문자열 " "은 [비교식]에서는 식별자에 할당되어 is not None이고, [if문]에서도 True다
    print(r'" " is',  "Not none" if " " is not None else "None")   # True
    print(r'" " is', "True" if " " else "False") # True

    # (3) 빈 컨테이너들 (반복문의 in에 올 수 있는 녀석들 <-> 조건문의 in)
    print(r'[] is',  "Not none" if [] is not None else "None")   # True
    print(r'[] is', "True" if [] else "False") # False
    print(r'() is',  "Not none" if () is not None else "None")   # True
    print(r'() is', "True" if () else "False") # False
    print(r'dict() is',  "Not none" if dict() is not None else "None")   # True
    print(r'dict() is', "True" if dict() else "False") # False

    # (4) 빈 이차원배열은 true다
    print(r'[[]] is',  "Not none" if [[]] is not None else "None")   # True
    print(r'[[]] is', "True" if [[]] else "False") # False

    # (4) 숫자 0과 0.0
    print(r'0 is',  "Not none" if 0 is not None else "None")   # True
    print(r'0 is', "True" if 0 else "False") # False
    print(r'0.0 is',  "Not none" if 0.0 is not None else "None")   # True
    print(r'0.0 is', "True" if 0.0 else "False") # False

    # (5) None
    print(r'None is',  "Not none" if None is not None else "None")   # True
    print(r'None is', "True" if None else "False") # False

    # (6) boolean반환 확인은 그냥 bool()내장함수를 쓰면 된다.
    print(bool(""), bool([[]]))

if __name__ == '__main__': 
    solution() 
