import sys

input = sys.stdin.readline

if __name__ == '__main__':
    ## iterable의 각 요소 변환시, list comp외에 list(map( , ))도 있다.
    data = [
        '123',
        '1234',
        '12345',
        '12346',
    ]

    ## list(map())을 모를 때, 각 원소의 길이
    print([len(x) for x in data])

    ## list(map())을 이용한 각 원소 변환
    print(list(map(lambda x: len(x), data)))
    print(list(map(len, data)))

    ## input되는 요소도 map의 함수객체 자리에 lambda를 넣어줄 수 있다.
    input_data = '123'
    print(list(map(lambda x: int(x) - 1, input_data)))
