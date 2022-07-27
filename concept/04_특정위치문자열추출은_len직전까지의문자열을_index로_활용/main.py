def solution():
    # 특정위치의 문자열을 추출하고 싶다면
    # 인덱싱해야하는데
    # 특정위치 문자열의 인덱스 -> index
    # 특정위치 문자열 직전의 인덱스 -> index - 1
    #                    길이   -> index
    # "문자열"[ len("직전까지의문자열") ] -> 문자열[index]
    # --> 특정위치의 문자열을 추출하고 싶다면,
    # --> 인덱스 자리에 len(직전까지의 문자열)을 사용하면 된다.

    print("asnkd;asdf"[len("asnkd")])

    "가나다라마바사"
    print(r"///ㅁ\\\\"[len("///")])
 
 
if __name__ == '__main__': 
    solution() 
