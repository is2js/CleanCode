import collections

from utils.main import CompositeTransactionPolicy


class TransactionPolicy(collections.UserDict):
    """잘못된 상속"""
    def __init__(self) -> None:
        super().__init__()

    def change_in_policy(self, customer_id, **new_policy_data):
        print(self)
        self[customer_id].update(**new_policy_data)


def solution():
    # 5. 컴포지션과 상속
    # 5.1. 상속이 좋은 선택인 경우
    #   부모 클래스의 메서드를 공짜로 전수받을 수 있는 장점이 있지만,
    #   한편으론 새로운 정의에 너무 많은 기능을 추가하게 되는 단점도 있다.
    #
    # 다음과 같은 경우, 상속은 좋은 선택의 예가 된다.
    #
    # 클래스의 기능을 그대로 물려받으면서 충분히 사용할 상황이 있고, 추가 기능을 더하거나 기존 기능을 수정하는 경우
    # 인터페이스용 클래스를 정의하고, 이를 하위 클래스에서 이를 상속받아 기능을 강제하려는 경우
    # 다형성을 통해 로직을 유연하게 설계하려는 경우 (Exception 을 상속받아 예외를 처리하는 경우가 대표적인 예다.)

    # 5.2. 상속 안티 패턴
    # (1) BaseCase
    # -> 도메인 객체을 상속한 유틸객체 -> 도메인을 주요기능을 물려받아 사용안함. 유틸로서만 사용됨.
    ## TransactionPolicy 이름만 보고 어떻게 사전 타입인지 알 수 있을까?
    ## UserDict 에 있는 pop(), items() 와 같은 메서드가 이 클래스에 실제로 필요할까?
    ## 단지 [dict의 첨자 기능]을 얻기 위해 사전을 확장하는 것은 충분한 근거가 되지 않는다.
    ## 이것이 구현 객체를 도메인 객체와 혼합할 때 흔히 발생하는 문제다.
    # policy = TransactionPolicy() # dict인지 모른다.
    # policy.change_in_policy(1, name="조재성", 나이="36")

    # (2) GoodCase
    #     [확장된 자료구조]를 만들고 싶다면, 상속하지말고, 생성자를 dict를 받아서 [상태로 소유]해서 써라.
    #     -> [일급컬렉션] 개념이다.
    #     첨자기능은 len + getitem 구현으로 첨자기능을 [소유 컬렉션 필드]에 적용할 수 있다.
    transaction_policy = CompositeTransactionPolicy({1:{}, 2:{}}, 여분="더미", 여분2="더미2")
    print(transaction_policy[1])
    transaction_policy.change_in_policy(1, 이름="조재성", 나이=36)
    print(transaction_policy[1])
    transaction_policy.change_in_policy(1, 이름="김석영", 나이=35)
    print(transaction_policy[1])
    pass
 
 
if __name__ == '__main__': 
    solution() 
