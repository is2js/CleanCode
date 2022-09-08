import sys 
 
input = sys.stdin.readline 
 
 
if __name__ == '__main__':
    input_ = '5 3'
    a, b = map(int, input_.split())
    # share, reminder = divmod(a, b)

    # 몫과 나머지가 동시에 필요할 때
    # 공백 출력은 요소를 언패킹으로 출력
    print(*divmod(a, b))
