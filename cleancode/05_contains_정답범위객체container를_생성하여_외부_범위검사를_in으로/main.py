class Coord:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value


# (2) 정답범위들을 객체1개에 모두 소지해야 in 에 1개의 객체로 쓰이며
#    contains에는 정답범위를 표기할 수 있다.
class Grid:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    # (4) 정답범위 객체를 인자로 받는 외부 in 으로 사용되는contains를 정의하여
    #    컨테이너 객체가 되자.
    def __contains__(self, coord):
        print(coord)
        return self.x_min <= coord.x <= self.x_max \
               and self.y_min <= coord.y <= self.y_max


def solution():
    # 5. 컨테이너 객체
    # -> 컨테이너 객체는 [ X in Y ]포함여부 조건문의 Y에 들어갈 수 있는 객체로
    # -> 매직 메서드 __contains__를 구현한 객체다.

    # 즉 아래 두 문장은 같은 문장이다. -> contains구현 container가 element를 특정조건으로 포함여부를 검사한다.
    # element in container
    # container.__contains__(element)

    # 어떤 객체를 컨테이너 객체로 잘 설계하면 훨씬 가독성이 좋다.
    # -> 즉, [어떤 범위를 확인하는 if Y.a <= X.x <= Y.b 문]을 정답범위를 가지는 Y의 contains내부 구현으로 숨기고
    # --> 외부에서는  [ X in Y ]로 간단하게 사용할 수 있게 된다.

    # -> my) 원하는 범위를 검사하기 위해선, 검사대상인 element가 아니라  <=  <= 정답범위를 필드로 소유한 객체 Y를 class로 정의해야한다
    # --> a <= coord.x <= b and m <= coord.y <= n이라면
    # --> X의 최소범위, 최대범위 와 Y의 최소, 최대범위인 a, b, n, n을 필드로 가진 정답범위class를 설계후 객체로 만들어야한다.

    # -> 즉, 범위를 확인해주는 용도의 정답범위객체를 새롭게 생성해야한다.

    coord = Coord(5, 3)
    ## bad case -> 범위확인하는데 contains(정답범위 객체)를 안쓰는 경우
    if 0 <= coord.x <= 100 and 0 <= coord.y <= 100:
        pass

    ## good case
    # (1) coord필드들의 정답범위들을 필드로 가지고 있는 class Grid를 만든다.
    # -> 필드로 정답범위들을 다 가지고 있어야한다.
    grid = Grid(0, 100, 0, 100)
    # grid.x_min
    # grid.x_max
    # grid.y_min
    # grid.y_max

    # (3) a in b 포함여부 조건문에서 a는 __contains__(self, )의 인자로 들어와 범위검사 대상이 되며
    #     b가 contains를 구현해야한다.
    if coord in grid:
        print("grid객체에 포함되는 좌표입니다.")

    if not Coord(6, 3) in Grid(x_min=0, x_max=5, y_min=0, y_max=5):
        print("grid객체에 포함되지 않는 좌표입니다.")
    pass


if __name__ == '__main__':
    solution()
