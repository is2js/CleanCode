import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## n자리수를 맞춘 출력

    ## not pythonic
    s = '가나다'
    n = 7

    empty_count = n - len(s)
    left = ''
    for _ in range(empty_count):
        left += ' '
    left +=  s
    print(left)

    right = ''
    right += s
    for _ in range(empty_count):
        right += ' '
    print(right)

    center = ''
    # -> empty_count를 반반 나눠서, 앞뒤로 붙여주자.
    # -> empty_count는 짝수라고 했으니, 2로 나눈 몫으로 처리하면 된다.
    half_count = empty_count // 2

    for _ in range(half_count):
        center += ' '
    center += s
    for _ in range(half_count):
        center += ' '

    print(center)

    ## pythonic

    # string.ljust, .center, rjust는 공백으로 자리수를 맞춰 출력해준다.
    print(s.ljust(7))
    print(s.rjust(7))
    print(s.center(7))

