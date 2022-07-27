def bad_validate(name):
    if len(name) < 10:
        raise ValueError


class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


def good_validate(name):
    if len(name) < 10:
        raise NameTooShortError


def solution():
    # 자신만의 예외 클래스 정의하기
    # 고유한 예외 타입을 정의하면 코드의 의도가 좀 더 명확하게 표시되고 디버깅하기 더 쉬워진다.
    # 파이썬 내장 Exception 클래스 또는 ValueError 나 KeyError 와 같은 구체적인 예외 클래스에서 사용자 정의 예외를 파생시키자.
    # 상속을 사용하여 논리적으로 그룹화된 예외 계층을 정의할 수 있다.
    # raise 일반Error는 BadCase다.
    # 일반Error를 상속한 BaseValidationError -> 구체적Error를 사용하자
    # bad_validate("10글자 이상")
    # 1. BaseValidationError: 내장Error상속
    #    class BaseValidationError(ValueError):
    # 2. 구체적Error: BaseValidationError상속
    # NameTooShortError()
    # 3. 메서드레베레에서느 구체적Error사용하기
    good_validate("10글자 이상")



 
if __name__ == '__main__': 
    solution() 
