def solution():
    ## 5.4. 세트와 멀티세트
    # (1) set : 믿음직한 세트
    # -> 변경 가능한 해시 자료구조로, 데이터 자료구조에 접근하는데 O(1) 의 시간복잡도가 걸림.
    # 해쉬구조로 순서보장은 안되지만, 중복을 제거하고, add를 할 수 있다.
    vowels = {'a', 'e', 'i', 'o', 'u'}
    print('e' in vowels)

    vowels.add('x')
    print(vowels)
    # {'e', 'i', 'x', 'u', 'o', 'a'}

    # (2) frozenset : 불변세트
    # -> set을 이용해서 생성자에서 생성된다.
    # -> add등 상태변경이 안된다.
    frozen_vowels = frozenset(vowels)
    # frozen_vowels.add('x')
    # AttributeError: 'frozenset' object has no attribute 'add'

    # (3) collections.Counter : 멀티세트(bag)
    # -> 클래스처럼 객체로 생성하여 사용하며
    # -> dict를 인자로 생성 or update할 수 있다.
    # -> update하면 덮어쓰기가 아니라 추가가 된다.
    from collections import Counter
    inventory = Counter()
    root = {'sword': 1, 'bread': 3}
    inventory.update(root)
    print(inventory)
    # Counter({'bread': 3, 'sword': 1})
    more_root = {'sword': 1, 'apple': 1}
    inventory.update(more_root)
    print(inventory)
    # Counter({'bread': 3, 'sword': 2, 'apple': 1})

    # len을 때리면 key의 갯수가 반환된다.
    print(len(inventory))
    # 3

    # values()를 때리면, count들이 list처럼 <class 'dict_values'> 자료구조에 있다
    print(inventory.values())
    print(type(inventory.values()))
    # dict_values([2, 3, 1])
    # <class 'dict_values'>


    # values()이후 sum을 때리면, 총 count합이 반환된다.
    print(sum(inventory.values()))
    # 6
    pass
 
 
if __name__ == '__main__': 
    solution() 
