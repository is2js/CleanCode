import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    ## 빈문자열에 문자열list의 누적합 빈문자열누적합 대신 join을 활용하자.
    lst = [ '1', '100', '33']

    ## not pythonic
    result = ''
    for i in range(len(lst)):
        result += lst[i]
    print(result)

    ## pythonic
    # -> 1개라도 일단 list배열로 간주하고 집계를 하는 식으로 계산하는 것이 좋다.
    # -> 문자열list로 1개씩 append하지말고, stream -> join하자.
    print(''.join(lst))
