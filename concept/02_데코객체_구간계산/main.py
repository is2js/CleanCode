class DurationPriceRule:

    def __init__(self, price, duration, prev) -> None:
        self.price = price
        self.duration = duration
        self.prev = prev

    def calculate(self, duration):
        # 특이점 객체 아니여야 && 전체구간이 내 하한보다 커야 계산한다.
        # 돌아가며 누적하는 계산이고, 쪼개진 구간들은 모두 참석하는데, 내 구간 아니면 0을 반환하면 된다.
        if self.prev.duration is None or duration <= self.prev.duration:
            return 0

        upperbound = self.duration if duration > self.duration else duration
        target_duration = upperbound - self.prev.duration
        return target_duration * self.price


class DurationPriceCalc:

    def __init__(self) -> None:
        self.rule = DurationPriceRule(0, 0, None)

    def add_rule(self, price, duration):
        if self.rule.duration >= duration:
            raise ValueError("invalid duration")
        if price == 0:
            raise ValueError("invalid price")

        self.rule = DurationPriceRule(price, duration, self.rule)

    def calculate(self, duration):
        sum = 0
        target_rule = self.rule
        while True:
            temp = target_rule.calculate(duration)
            print(temp)
            sum += temp
            target_rule = target_rule.prev
            if target_rule.prev is None:
                break
        if sum == 0:
            raise RuntimeError("invalid calc's calculate")
        return sum


def solution():
    duration = 180
    calc = DurationPriceCalc()
    calc.add_rule(20, 5) # 5초까진 초당 20원 -> 100원
    calc.add_rule(10, 10) # 5~10초까진 초당 10원 -> 50원
    calc.add_rule(1, 200) # 10~180초까진 초당 1원 -> 170원

    print(">>", calc.calculate(duration))


if __name__ == '__main__':
    solution()
