from typing import List


class Enum:
    ACE = 1
    TEN = 10


def has_ace(first_card, second_card) -> bool:
    return any([card == 1 for card in [first_card, second_card]])


def get_sum(first_card, second_card):
    return sum([first_card, second_card])

def has_ace2(cards) -> bool:
    return any([card == 1 for card in cards])


def get_sum2(cards):
    return sum(cards)

def has_ace3(cards) -> bool:
    return any([card == 1 for card in cards.cards])

def get_sum3(cards):
    return sum(cards.cards)


class Cards:
    def __init__(self, *cards) -> object:
        self.cards = cards

    def has_ace4(self) -> bool:
        return any([card == 1 for card in self.cards])

    def get_sum4(self):
        return sum(self.cards)

    def isBlackjack(self):
        return self.has_ace4() and self.get_sum4() == 11

    def __repr__(self):
        return f"{self.__class__.__name__}({self.cards!r}, )"



def solution():
    first_card = 1 or 11
    second_card = 10

    # 1. 같은 타입이면 list로 묶은 반복문으로 [일괄처리]할 수 있다
    is_ace = False
    for card in [first_card, second_card]:
        if card == 1:
            is_ace = True

    print(is_ace)

    # 2. list comp는 append지만, 조건식을 작성하면, 불린을 append할 수 있다.
    print([card == 1 for card in [first_card, second_card]])

    # 3. python은 any()는 T/F로 구성된 iter를 받아 1개라도 존재하는지 유무를 알려준다.
    print(any([card == 1 for card in [first_card, second_card]]))

    # 4. method추출
    has_ace(first_card, second_card)

    # 5. ace를 가지고 있으면서 && 그 합이 11이하여야 변경가능하고, 11이면 blackjack이다.
    if has_ace(first_card, second_card) and first_card + second_card == 11:
        print("blackjack")

    # 6. 같은형의 연산도 묶어서 처리할 수 있다.
    #    묶어서 처리하면, 메서드로 추출할 수 있다.
    if has_ace(first_card, second_card) and get_sum(first_card, second_card) == 11:
        print("blackjack")

    # 7. 묶는 부분이 공통이면 파라미터추출로 올려서 묶는 부분만 따로 처리할 수 있다.
    #  -> 추출안될 수도 있으면 직접 추출한다.
    cards = [first_card, second_card]
    if has_ace2(cards) and get_sum2(cards) == 11:
        print("blackjack")

    # 8. 같은형이 묶인다면, 일급컬레션을 고려한다.
    cards = Cards([first_card, second_card])
    if has_ace3(cards) and get_sum3(cards) == 11:
        print("blackjack")

    # 9. *args로 가변인자로 받자.
    cards = Cards(first_card, second_card)
    print(cards)
    if has_ace3(cards) and get_sum3(cards) == 11:
        print("blackjack")

    # 10. 내수용메서드는 객체에게 위임할 수 있다.
    cards = Cards(first_card, second_card)
    print(cards)
    if cards.has_ace4() and cards.get_sum4() == 11:
        print("blackjack")

    # 11. 조건식에 1개 도메인에 대한 메서드들이 나열되어있으면 묶어서 위임할 수 있다.
    cards = Cards(first_card, second_card)
    print(cards)
    if cards.isBlackjack():
        print("blackjack")




if __name__ == '__main__':
    solution()
