def solution():
    ## 5.1 dict : 믿음직한 딕셔너리
    # 딕셔너리의 키는 불변타입(immutable) 만 가능하다.
    # 조회, 삽입, 갱신 및 삭제의 시간복잡도는 O(1) 이다.
    # 사용하지않을 이유가 거의 없다.

    ## collections.OrderedDict : 키 삽입 순서 기억
    # 해시의 특성상 데이터의 순서 개념이 없는데, OrderedDict 는 삽입 순서를 기억함.
    # -> 개인적으로 딕셔너리로 json 만들 때 유용하다고 생각.
    import collections
    ordered_dict = collections.OrderedDict(one=1, two=2, three=3)
    print(ordered_dict)
    # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
    ordered_dict['four'] = 4
    print(ordered_dict)
    # OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])

    ## collections.defaultdict : 누락된 키의 기본값
    # 키가 없는 경우, 기본 값을 알아서 반환한 뒤 동작 (위의 경우 list 반환)
    # defaultdict 인자로 callable 한 객체(따라서 함수도 가능)를 넣어주면 됨.
    # -> 개인적으로 평소에 굉장히 유용하게 잘 쓰고있음. 특히 위 같이 list 를 가지는 딕셔너리의 경우.
    from collections import defaultdict
    default_dict = defaultdict(list)
    # ->  초기화안해도 이미 list로 초기화되어, append가 가능하다.
    default_dict['dogs'].append('Rufus')
    default_dict['dogs'].append('Kathrin')
    print(default_dict)
    # defaultdict(<class 'list'>, {'dogs': ['Rufus', 'Kathrin']})
    print(default_dict['dogs'])
    # ['Rufus', 'Kathrin']

    ## types.MappingProxyType : 읽기 전용으로 만드는 딕셔너리 래퍼
    # 나도 처음보는데, 견고하게 프로그래밍하는데 굉장히 유용할거 같음...
    # 파이썬 3.3부터 들어온 클래스라고 함.
    # -> 프락시는 읽기 전용이며 원본 업데이트시 -> 읽기전용인, 프락시에도 반영된다.
    from types import MappingProxyType
    writable = {'one': 1, 'two': 2}
    read_only = MappingProxyType(writable)

    print(read_only['one'])
    # 1

    # read_only['one'] = 5
    # TypeError: 'mappingproxy' object does not support item assignment

    writable['one'] = 5
    print(read_only['one'])
    # 5


    pass
 
 
if __name__ == '__main__': 
    solution() 
