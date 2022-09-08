import random
import string
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## 숫자 -> 알파벳 매핑은 chr()를, 알파뱃->숫자매핑은 ord()를

    # not pythonic
    #  a 97+0~97+25 까지 26개
    #  A 65+0~65+25 까지 26개
    number = random.randint(0, 1)
    result = ''
    if number:
        for i in range(65, 65 + 25 + 1):
            result += chr(i)
    else:
        for i in range(97, 97 + 25 + 1):
            result += chr(i)
    print(result)

    # pythonic
    ## 1개씩 매핑은 chr/ord 65/97이 있지만,
    # -> 알파벳전체매핑인 string모듈을 이용한다.
    if number:
        print(string.ascii_uppercase)
    else:
        print(string.ascii_lowercase)
    print(string.digits)
