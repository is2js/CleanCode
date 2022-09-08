import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## n진법 string을 10진법 number로 변환
    input_ = '12 3'  # 3진법 12를 10진수로

    ## not pythonic -> 역순으로 배열 후, 10으로 나눈 나머지 -> 1의자리 => 업데이트는 10으로 나눈 몫으로 다음 1의자리 끌어오기
    number, base = map(int, input_.split())

    count = 0
    sum = 0
    # 10을 나눈 몫을 취하다보면, 11 -> 1 -> 0 / 10 -> 1 -> 0
    # => 10으로 나눈 몫으로 업데이트하여, 1의 자리수만 걸러낸다면, 종착역은 10의 자리가 더이상 없는 1의 자리만 남은 것 처리후 몫이 0일때다.
    while number != 0:
        share, reminder = divmod(number, 10)

        sum += reminder * (base ** count)

        count += 1
        number = share
    print(sum)


    ## n진법 수는 정수로 바꾸지말고 문자열로 두고 enumerate로 index(자리수)와 value(그때의 값)을 활용해라
    number, base = input_.split()
    base = int(base)
    ## iterable역순은 [::-1]을 활용해라
    answer = 0
    for i, value in enumerate(number[::-1]):
        answer += int(value) * (base ** i)

    print(answer)


    ## pythonic
    # -> int()는 int( ,base=10)으로 기본10진수 string을 변환하지만, 바꿀 수 있다.
    print(int(number, base=base))
