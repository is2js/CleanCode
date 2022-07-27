def solution(): 
    # 4.6. 네임드튜플은 어디에 적합한가
    # -> 불변속성을 가진 불변클래스를 지역변수로 생성하여, 객체를 만들 수 있다.
    #     class정의없이 & 빠르게 & 튜플처럼 사용할 수 있다.
    # -> tuple이나 list는 값context라 순서를 기억해야하는 단점이 있고, 가변이라 느리다.
    # -> 불변 클래스를 수동으로 정의하는 메모리 효율적인 지름길이다.

    from collections import namedtuple
    Car = namedtuple("Car", ["color", "mileage"])
    my_car = Car("red", 3812.4)
    print(my_car.color)
    print(my_car.mileage)

    #### tuple의 속성을 가지고 있어 [객체의 속성]을 좌항 변수+콤마로 언패킹이 가능하다.
    color, mileage = my_car
    print(color, mileage)

    #### 필드들을 상속해서 쓸 수 있다. 있다 자식의 필드는 ()소괄호로 튜플의 string으로 입력한다.
    #### namedtuple._fields도 namedtuple이기 때문에 튜플 + 튜플형태로 만든다.
    ElectricCar = namedtuple("ElectricCar", Car._fields + ("charge",))
    electric_car = ElectricCar("red", 1234, 45.0)
    print(electric_car.charge)


    #### 내장 도우미 메서드들이 있다.
    # (1) _asdict(): 내장한 불변의 속성들과 값들을 -> dict변환
    # (2) _replace(): 불변속성을 강제변경
    # (3) _make(): 객체생성을 생성자가 아닌 list로 나열해서 생성
    print(my_car._asdict()) # OrderedDict([('color', 'red'), ('mileage', 3812.4)])

    print(my_car._replace(color="blue")) # inplace가 아닌 변경된 객체 생성해서 반환이다
    print(my_car)

    print(Car._make(['green', 9999])) # Car(color='green', mileage=9999)





if __name__ == '__main__': 
    solution() 
