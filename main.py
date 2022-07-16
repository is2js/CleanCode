def fibonacci_loop(n):
    assert n < 0, "0이하를 입력할 수 없습니다."
    if n <= 1:
        return n


if __name__ == "__main__":
    fibonacci_loop(10)
