from random import randint


class RandomIntIterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        # return self
        return RandomIntIterator(self.n)


# -> iterator는 상태값을 가져서, 1개씩 반환하면서, current값을 1개씩 올린다.
class RandomIntIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0

    def __iter__(self):
        # iterator는 iter구현시 self를 반환하고, next가 자동호출되도록 한다.
        return self

    def __next__(self):
        # input의 갯수를 아직 못채웟을때만 1개씩 반환해준다.
        if self.count < self.n:
            self.count += 1
            return randint(1, 100)
        else:
            raise StopIteration


if __name__ == '__main__':
    # print(next(RandomIntIterable(5)))
    # TypeError: 'RandomIntIterable' object is not an iterator

    # iterator를 사용하는 iterable은,
    # -> iterator용 next()는 직접적으로 호출못하지만,
    # -> iter가 호출되는 for문안에서는 , iterator가 생성되어 작동한다.
    for x in RandomIntIterable(5):
        print(x)
        # 97
        # 41
        # 44
        # 90
        # 22