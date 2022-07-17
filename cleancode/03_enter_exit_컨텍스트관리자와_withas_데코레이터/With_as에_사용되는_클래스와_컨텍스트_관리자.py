class DBConnector:

    def __init__(self, id, password) -> None:
        self.id = id
        self.password = password
        print("1. DBConnector.__init__")

    def connect(self):
        print("3. DBConnector.connect")

    def close(self):
        print("6. DBConnector.close")

    def __enter__(self):
        print("2. DBConnector.__enter__")
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("5. DBConnector.__exit__", end =" / ")
        print(f"exc_type: {exc_type}, exc_val: {exc_val}, exc_tb: {exc_tb}")
        self.close()


if __name__ == '__main__':
    db_connector = DBConnector(id='id', password='password')

    # not pythonic
    db_connector.connect()
    db_connector.close()

    # pythonic
    with DBConnector(id='id', password='password') as db_connector:
        # 1) enter를 오버라이딩 안하면, init만 호출된다.
        # >>> 1. DBConnector.__init__
        # 2) enter오버라이딩 후, 내부에는 내부의 self.연결메서드를 호출하도록 정의하면
        # -> __exit__오버라이딩 안됬다고 에러 뜬다 -> 쌍으로 정의해주자.
        # 3) exit 내부에 close()호출까지 같이 정의하면
        # >>> 1. DBConnector.__init__
        # >>> 2. DBConnector.__enter__
        # >>> 3. DBConnector.connect
        # >>> 5. DBConnector.__exit__ / exc_type: None, exc_val: None, exc_tb: None
        # >>> 6. DBConnector.close

        # 4) with as문에 내 할일을 시행하면
        print("4. 내 할일")
        # >>> 1. DBConnector.__init__
        # >>> 2. DBConnector.__enter__
        # >>> 3. DBConnector.connect
        # >>> 4. 내 할일
        # >>> 5. DBConnector.__exit__ / exc_type: None, exc_val: None, exc_tb: None
        # >>> 6. DBConnector.close
