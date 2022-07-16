def solution():
    arr = [1, 2, 3, 4]

    # 첨자가 아닌, len(arr)을 이용하여 인덱싱
    last = arr[len(arr) - 1]
    print(last)

    # getitem 상속을 구현한 객체 = 첨자형 객체의 인덱싱 + 슬라이싱
    last = arr[-1]
    print(last)
    odds = arr[::2] # 처음부터 2개씩(홀수번째)
    print(odds)
    evens = arr[1::2] # 짝수번째
    print(evens)
    reverse = arr[::-1]
    print(reverse)


class Bag:
    def __init__(self, item_size=None, user_name=None):
        self._items = [None] * item_size
        self._item_cnt = 0
        self._user_name = user_name

    def add_item(self, item):
        self._items[self._item_cnt] = item
        self._item_cnt += 1

    # 객체[인덱싱]로 객체를 인덱싱해서, 내부 컬렉션필드 인덱싱 값을 얻으려면,
    # -> 해당 컬렉션필드[인덱스]를 반환하는, getitem을 오버라이딩 해야한다.
    def __getitem__(self, item):
        return self._items[item]



if __name__ == '__main__':
    solution()
    # n개의 None으로 초기화한 빈 리스트의 capacity(갯수), "사람이름", 들어온 "item"의 갯수를  필드로 가지는 객체
    # 아이템이 들어올때마다, count = 0 -> list의 index로서 사용해서 채우고 +1
    js_bag = Bag(10, "chojaeseong")
    js_bag.add_item("음료수")
    js_bag.add_item("김밥")
    js_bag.add_item("라면")
    js_bag.add_item("소주")

    print(js_bag[0]) # TypeError: 'Bag' object does not support indexing
    # getitem 오버라이딩 적용후
    print(js_bag[0]) # 음료수
    print(js_bag[-1]) # None # 동적으로 늘어나는 list가 아니라 미리 갯수가 정해져있고,  None으로 차있기 때문에
    print(js_bag[::2]) # ['음료수', '라면', None, None, None]




