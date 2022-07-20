import functools

def null_decorator(func):
    print("null_decorator ~!")
    return func


def greet():
    print("Hello!")


@null_decorator
def greet_with_decorator():
    print("Hello!")


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args)
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def lowercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args)
        return result.lower()

    return wrapper


# @lowercase
@uppercase
def return_hello(name):
    return name


def solution():
    # 3.3. 데코레이터의 힘
    # 데코레이터는 다른 함수를 "장식" 하거나 "포장"하고, 감싼 함수가 실행되기 전후에 다른 코드를 실행할 수 있게 한다.
    # 데코레이터가 유용한 경우는 다음과 같은 경우다.
    # 로그 남기기
    # 접근 제어와 인증 시행
    # 계측 및 시간 측정
    # 비율 제한
    # 캐싱 및 기타
    # (1) 데코레이터의 작성은, ()호출부 없는 함수객체를 받고 -> 함수객체를 반환하는 [메서드로 생성 정의]하고 -> 이후 사용해보자.
    # null_decorator(greet)
    # -> 인자로 준 함수객체는 함수로 생성이 안되니 ()붙여서 기본메서드부터 정의했다가 다시 풀어주자.
    # null_decorator(greet())
    # null_decorator(greet)
    # (2) 데코레이터는 클로져로써 함수객체를 반환한다고 생각하고, 반환되는 함수에 ()를 붙여 호출해주자.
    # null_decorator(greet)()
    # (3) 이제 데코레이터 작동을 확인했으면 -> 메소드정의부에 @데코레이터를 붙여주자.
    # -> 함수호출만해도, ()없이 데코레이터로 들어갔다가 ()까지 마지막에 ()로 호출한다.
    # greet_with_decorator()

    # (4) 문자열을 반환하는 base기본함수 return_hello에다가 메서드로서 대문자로 바꿔주는 데코레이터를 작성해보자.
    # return_hello()
    # (5) 클로져로서, 함수객체를 인자로 받고, 지역상태를 기억시켜, 외부반환하여 사용하는 형태로 만든다.
    # print(uppercase(return_hello))
    # (6) 장식할 때, base함수를 호출해서 결과값을 받고, 그 결과값을 장식할 것이라면
    #    -> 이미 호출한 함수가 되어서, 외부로 함수객체 반환이 안된다.
    # print(uppercase(return_hello))
    # print(uppercase(return_hello) () )
    # TypeError: 'str' object is not callable

    # (7) base()호출 결과물 장식 로직을, 그대로 inner method wrapper로 감싼 뒤
    # -> return wrapper (함수객체)를 해준다.
    # print(uppercase(return_hello)())

    # (8) 데코레이터 메서드가 완성되었으면, base함수에 @로 달아주기
    # print(return_hello())

    # (9) 다중 데코레이터는, 아래에서부터 -> 위로 달아준다.
    # print(lowercase(uppercase(return_hello))())

    # (10) base함수가 인자가 필요할 때는, 외부반환되는 wrapper에서 *args, **kwargs로 받으면 받아 제공하면 된다.
    print(return_hello("Abc"))
    pass


if __name__ == "__main__":
    solution()
