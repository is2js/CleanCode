def yell(text):
    return text.upper() + " ! "


def greet(func):
    greeting = func("abc")
    print(greeting)


def get_speak_func(text, volume):
    def whisper():
        return text.lower() + "..."

    def yell():
        return text.upper() + "!"

    if volume >= 0.5:
        return yell

    return whisper


def solution():
    bark = yell
    print(bark("abc"))
    print(bark.__name__)  # 호출전 함수는 일급객체로서, 변수에 할당해도 name은 함수이름이 나온다.

    functions = [bark, str.lower, str.capitalize]
    print(functions[0]("abc"))  # 함수 객체를 list에 넣어서 인덱싱후 호출할 수 도 있다.

    greet(bark)  # 함수객체를 인자로 넘겨서 내부에서 호출할 수도 있다.

    # 지역함수 객체를 return으로 반환한 뒤, 외부에서 ()를 달아 호출해도, 지역상태가 포착되어있다.
    func = get_speak_func("Hello, World", 0.7)
    print(func())
    print(get_speak_func("Hello, World", 0.4)())

    # 위 코드에서 whisper 나 yell 내부를 보면 부모 함수에서 정의된 text 에 아무 이상없이 접근하고 있다.
    # 이렇게 동작하는 함수를 렉시컬 클로저, 짧게 클로저라고 한다.
    # 클로저는 프로그램 흐름이 더 이상 해당 범위에 있지 않은 경우에도 둘러싼 어휘(lexical) 범위 안의 값들을 기억한다.

    # my) 클로저는 지역메서드를 외부에서 반환했음에도, 지역변수 등의 지역상태를 기억하고 있는 상태다.


if __name__ == '__main__':
    solution()
