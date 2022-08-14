class CommandRepo:

    def __init__(self) -> None:
        self.repository = []
        self.cursor = -1  # cursor는 0번째 원소가 들어와야 0, 그전엔 -1로 초기화

    def add(self, value):
        # 4) cursor를 undo해도 길이/데이터가 보존되는 컬렉션,의 api로만 업데이트 하면 문제가 생긴다
        #    add시, cursor + 1 ~ len -1 까지 요소는 모두 제거한 뒤 add해서
        #    add된 요소가 컬렉션의 맨 끝이 되도록 하게 한다.
        for i in range(len(self.repository) - 1, self.cursor, -1):
            self.repository.remove(i)

        self.repository.append(value)
        # 1) cursor는 append실행후 컬렉션api를 통한 불변식으로 업데이트 한다
        self.cursor = len(self.repository) - 1

    def add_undo(self):
        # 2) undo는 컬렉션에 pop할 요소가 있을 때, 1개라도 있을 때
        #  ->  cursor 0이상일 때 (cursor >= 0) 일 때 할 수 있다.
        if self.cursor < 0:
            raise RuntimeError('cannot undo')
        # 3) undo는 제일마지막 것이 아닌(undo 여러번으로 커서만 내려간 상태)
        #    현재cursor위치의 것을 반환하고,
        #    지우지않고,
        #    cursor만 한칸 내려야, redo가 가능하다.
        last_value = self.repository[self.cursor]
        self.cursor -= 1
        return last_value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.repository!r}, {self.cursor!r})"

    def add_redo(self):
        # 7) redo는 undo한 상태여야한다
        #   -> cursor가 컬렉션의 끝보다 더 빽한 상태여야한다.
        #   -> add하면 cursor가 컬렉션 끝으로 업데이트 되며
        #   -> undo해야만, cursor가 뒤로 빽한다.
        if self.cursor == len(self.repository) - 1:
            raise RuntimeError('cannot redo')
        # 8) redo의 내용은
        # cursor를 뒤로 한칸 간 뒤, 그놈을 getter해서 실행하는 것이다.
        # -> 여기서는 cmd객체를 꺼내서 실행하진 않으므로, cursor만 올릴 수 밖에..
        self.cursor += 1
        execute = self.repository[self.cursor]
        # 9) python 3.8 이후에서는 먼저업데이트 후 사용은 대입표현식, 코끼리 연산자로 쓸 수 있다.
        #    java는 --cursor를 바로 사용하는 것과 같다.
        # execute = self.repository[self.cursor := self.cusror + 1]


if __name__ == '__main__':
    repo = CommandRepo()
    repo.add(1)
    repo.add(2)
    repo.add(3)
    print(repo)  # CommandRepo([1, 2, 3], 2)
    repo.add_undo()
    print(repo)  # CommandRepo([1, 2, 3], 1)

    # 5) undo로 cursor가 빽 한 상태에서, add하면,
    #    cursor보다 더 뒤에 있던 요소들은 다 날려놓음으로써
    #    현재add한 것이 컬렉션의 제일 마지막에 위치하게 한다
    repo.add(4)
    print(repo)  # CommandRepo([1, 3, 4], 2)

    # 6) redo는 undo를 요소제거안하고 커서만 빽한 이유이다.
    #    현재위치 (undo로 인해 1칸 빽한 cursor)에서 cursor만 +1 한 뒤
    #    getter로 꺼내서 시행(?)하면 되는데, 여기서는 값이므로 cursor만 옮기면 된다?
    # repo.redo() # raise RuntimeError('cannot redo')
    repo.add_undo()
    print(repo) # CommandRepo([1, 3, 4], 1)
    repo.add_redo()
    print(repo) # CommandRepo([1, 3, 4], 2)


