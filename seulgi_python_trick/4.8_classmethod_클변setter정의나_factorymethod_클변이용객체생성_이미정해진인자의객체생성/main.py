class MyClass:
    def method(self):
        """인스턴스 메서드: self 를 첫 번째 인자로 받음"""
        # 메서드의 반환은 튜플을 반환할 수 도 있다.
        return "instance method called", self

    @classmethod
    def class_method(cls):
        """클래스 메서드: cls 를 첫 번째 인자로 받음"""
        return "class method called", cls

    @staticmethod
    def static_method():
        """정적 메서드: self, cls 둘 다 안받음"""
        return "static method called"


class Pizza:
    fee = 1000

    def __init__(self, ingredients=None):
        self.ingredients = ingredients

    def __repr__(self):
        return f"{self.__class__.__name__}({self.ingredients!r})"

    @classmethod
    def 모짜렐라_factory(cls):
        return cls(["모짜렐라치즈", "도우"])

    @classmethod
    def 마가렛_factory(cls):
        return cls(["마가렛", "도우"])

    @classmethod
    def raise_fee(cls, fee):
        if fee < cls.fee:
            print("기존비용보다 싼 가격으로 올릴 수 없습니다.")
            return
        temp, cls.fee = cls.fee, fee
        print(f"increate fee {temp} -> {cls.fee}")


def solution():
    # 4.8. 인스턴스 메서드, 클래스 메서드, 정적 메서드
    # (1) 인스턴스 메서드는 인스턴스가 필요하며, self 를 통해 인스턴스에 접근할 수 있다.
    # (2) 클래스 메서드는 인스턴스가 필요하지 않다. 인스턴스(self) 에는 접근할 수 없지만 클래스 자체(cls) 에 접근할 수 있다.
    # (3) 정적 메서드는 cls 또는 self 에 접근할 수 없다.
    #    -> class내부에 정의되어있기 때문에, 외부메서드와 똑같은 유틸메서드 기능을 하지만,
    #       class에 묶어주면서 && Class와 인스턴스 모두에서 접근가능하다.
    #    -> 일반함수처럼 작동하지만 자신을 정의한 클래스의 네임스페이스 속한다.
    #    -> 정적 및 클래스 메서드는 클래스 설계에 대한 개발자의 의도를 전달하고 강제한다.
    #       이러한 점 덕분에, [유지 보수] 하는데 확실히 도움이 된다
    my_class = MyClass()
    # (1) 인스턴스에서 호출하는 인스턴스 메서드
    print(my_class.method())
    # ('instance method called', <__main__.MyClass object at 0x0000027BEF087320>)

    # (2) 클래스로 바로 호출하는 클래스 메서드
    print(MyClass.class_method())
    # ('class method called', <class '__main__.MyClass'>)

    # (3) 클래스로 바로 호출해도되고, 인스턴스에서 접근해도 되는 유틸메서드 = static메서드
    print(MyClass.static_method())
    # static method called
    print(my_class.static_method())
    # static method called

    #### 클래스메서드로 cls를 이용한 factory메서드 만들기
    ## class()로 생성자로 객체 생성하는 것보다 목적의식이 뚜렷해지며, 권장되고 있다.
    # (0) 생성자로 생성 -> 필드 생성
    pizza = Pizza(["재료1", "재료2"])
    #pizza.ingredients
    print(pizza) # Pizza(['재료1', '재료2'])

    # (1) cls( 이미 정해진 인자값들 )로 [이미 인자가 정해진 객체]를 생성해주는 factory
    print(Pizza.모짜렐라_factory())
    # Pizza(['모짜렐라치즈', '도우'])
    print(Pizza.마가렛_factory())
    # Pizza(['마가렛', '도우'])

    # (2) cls.클래스변수를 사용하여 객체를 생성하는 factory


    #### 클래스메서드로 cls를 이용해, 클래스변수 setter만들기
    ## 모든 인스턴스가 바라보고 사용되는 공용 변수(클래스변수)가 외부에서 막 사용되지 않기 위해
    ## 클래스 내부에서 클래스변수 수정하도록 코딩해주는 것
    #print(Pizza.fee)
    Pizza.raise_fee(1500)
    # increate fee 1000 -> 1500
    Pizza.raise_fee(1200)
    # 기존비용보다 싼 가격으로 올릴 수 없습니다.





    pass


if __name__ == '__main__':
    solution()