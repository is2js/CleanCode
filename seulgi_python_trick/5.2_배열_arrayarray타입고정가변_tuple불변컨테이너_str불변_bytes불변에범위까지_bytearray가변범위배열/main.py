def solution():
    ## 5.2. 배열 데이터 구조
    ## list : 가변 동적배열
    arr = ['one', 'two', 'three']
    print(arr[0])
    # one

    ## 각 요소를 건들일 수 있는 동적배열이다.
    arr[0] = 1
    print(arr[0])
    # 1

    print(arr)
    # [1, 'two', 'three']

    ## tuple : 불변 컨테이너
    # -> 각 요소를 건들일 수 없는 불변 컨테이너
    # 콤마로 생성된다.
    arr = 'one', 'two', 'three'
    #arr[1] = 1
    # TypeError: 'tuple' object does not support item assignment

    ## array.array :기본적인 타입 지정 배열
    # 리스트나 튜플보다는 공간 효율적이다.
    # 나도 처음 보긴 하는건데, 견고하게 프로그래밍 짜야될 때 좋지 않을까 싶다.

    import array
    arr = array.array('f', [1., 2., 3.])
    print(arr)
    # array('f', [1.0, 2.0, 3.0])

    ## 같은 타입으로는 요소를 변경할 수 있다.
    arr[0] = 23.
    print(arr)
    # array('f', [23.0, 2.0, 3.0])

    ## 기본타입외 다른형으로 변경은 안된다.
    # arr[1] = "hello"
    # TypeError: must be real number, not str

    ## str: 유니코드문자로 구성된 불변배열
    arr = "abcd"
    arr[1]
    print(arr)
    # abcd

    ## 불변 배열이라서 요소를 수정할 순 없다.
    # arr[1] = "e"
    # TypeError: 'str' object does not support item assignment


    ## bytes: 단일바이트의 불변 배열
    arr = bytes((0,1,2,3))

    ## 바이트의 출력은 자체 문법이 있다.
    print(arr)
    # b'\x00\x01\x02\x03'

    print(arr[1])
    # 1

    ## 불변배열이라 수정은 안된다.
    # arr[1] = 0
    # TypeError: 'bytes' object does not support item assignment

    ## 또한, 0 ~ 255까지의 제한범위가 있따.
    # ValueError: bytes must be in range(0, 256)
    # bytes((0, 300))

    ## bytearray: 단일바이트의 가변배열
    # -> 가변배열로서 요소들의 수정가능하다.
    arr = bytearray((0,1,2,3,4))
    arr[1] = 23
    print(arr)
    # bytearray(b'\x00\x17\x02\x03\x04')

    pass
 
 
if __name__ == '__main__': 
    solution() 
