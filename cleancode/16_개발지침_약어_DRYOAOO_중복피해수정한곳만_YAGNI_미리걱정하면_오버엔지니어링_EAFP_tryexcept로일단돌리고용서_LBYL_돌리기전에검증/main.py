def solution():
    # 개발지침 약어
    # 1. DRY / OAOO
    # Do not Repeat Yourself
    # Once And Only Once
    # -> 중복을 피하고 한번에 한일만 해야 -> 코드를 변경하려고 할 때 [수정이 필요한 곳은 단 한 군데만] 있어야 한다.

    # 2. YAGNI
    # You Ain't Gonna Need It
    # -> [오직 현재의 요구사항]을 잘 해결하기 위한 소프트웨어를 작성해야 한다.
    # -> 내가 짜고 있는 코드가 일어나지도 않을 미래의 일을 예상하고, 코드를 더 복잡하게 만들고 있는 건 아닌지,
    #    즉, 지금 필요하지도 않은 [오버 엔지니어링]을 하고 있는 건 아닌지 염두해야 한다.

    # 3. KIS
    # Keep It Simple
    # YAGNI 원칙과 비슷하다. 디자인이 단순할수록 유지 관리가 쉽다는 것이다.
    # 모든 확장 가능성, 좀 더 일반화적인 추상화가 지금 기능 개발 시점에서는 섣부를 수 있다.
    # 코드 측면의 단순함이란 문제에 맞는 가장 작은 데이터 구조(표준 라이브러리 등)를 사용하는 것을 의미한다.

    # 4. EAFP
    # Easier to Ask Forgiveness than Permisson
    # 허락보다 용서를 구하는 게 쉽다.
    # -> 일단 코드를 실행하고 실제 동작하지 않을 경우를 대응한다는 뜻이다.
    # try:
    #     with open(filename) as f:
    #         pass
    # except:
    #     pass

    # 5. LBYL
    # Look Before You Leap
    # 도약하기 전에 살펴라.
    # 코드를 실행하기 전에, 먼저 무엇을 사용하려고 하는지 확인하라는 뜻이다.
    # if os.path.exists(filename):
    #     with open(filename) as f:
    #         pass
    # -> 파이썬은 LBYL보다는 EAFP 방식으로 만들어졌다
    pass
 
 
if __name__ == '__main__': 
    solution() 
