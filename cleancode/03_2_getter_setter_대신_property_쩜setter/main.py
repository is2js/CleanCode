import re



class User:
    EMAIL_PATTERN = re.compile(r"[^@]+@[^@].[^@]+")
    EMAIL_FORMAT = re.compile("[^@]+@[^@]+[^@]+")

    def __init__(self, username):
        self.username = username
        self._email = None

    def set_email(self, new_email):
        if not self._is_valid_email(new_email):
            raise ValueError("유효한 이메일이 아닙니다.")
        self._email = new_email

    # private메서드는 self._메서드명()으로 생성한다.
    def _is_valid_email(self, email):
        # 상수는 클래스 변수라도 self(객체).상수명으로 사용되므로 -> 필드로 생성하되, 생성자내부에서 생성되므로 빼고 self도 삭제한다.
        # match = re.match(self.EMAIL_FORMAT, email) # re.match는 re.compile한 상수에 매칭되는 것이 없으면, None을 반환한다.
        # print(match)
        return re.match(self.EMAIL_FORMAT, email) is not None

    def get_email(self):
        return self._email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not self._is_valid_email2(value):
            raise ValueError("이메일 형식이 다릅니다.")
        self._email = value

    def _is_valid_email2(self, email):
        return re.match(self.EMAIL_PATTERN, email) is not None


def solution():
    user = User("조재성")
    # user.username
    ######################## not pythonic #########################
    #user.set_email("조재성") # _private필드를 setter
    #print(user.get_email()) # _private필드를 getter로 꺼낸다.
    # ValueError: 유효한 이메일이 아닙니다.
    user.set_email("조재성@gmail.com") # _private필드를 setter
    print(user.get_email()) # _private필드를 getter로 꺼낸다.

    # 파이썬은 자바에서 흔히 보이는 getter 와 setter 의 철학을 가지지 않는다.
    # -> 애초에 private 과 같은 접근제어자가 없는 맥락과 마찬가지.
    # -> 다만, @property 와 @.setter 라는 어노테이션을 통해 getter 와 setter 의 역할을 대신한다
    # @property 와 .setter 는 어떤 특별한 처리를 해야하는 경우에 활용한다.
    # 단순히 값을 받아오거나 세팅하는 경우에는, 바로 멤버 변수로 바로 접근하여 처리하는 게 일반적이다.
    user.email = "3123@sdf.com"
    print(user.email)

if __name__ == "__main__":
    solution()
