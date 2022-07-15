@echo off

:: 첫번째인자%1으로 폴더가 없으면 생성한다.
if not exist ".\%1\" md ".\%1"

:: 2번재인자%2으로 폴더가 없으면 생성하고, 이미 있으면 에러를 띄운다.
:: 1번째인자\2번째 인자폴더를 현재폴더로 인식한다.
if not exist ".\%1\%2" (
        md ".\%1\%2"
    ) else (
        echo "already have folder"
        GOTO:EOF
    )
    ::변수할당시 = 사이에 공백이 있으면 안된다.
    Set CURRENT_FOLDER=%1\%2
)

::root폴더에 작성한 *.py파일들을 인자로 생성된 폴더로 다 이동시킨다.
copy .\*.py .\%CURRENT_FOLDER% /DHKYCSIL


::기존 Main.py 초기문장 적어 초기화
echo def solution(): > .\main.py
echo     pass >> .\main.py
echo. >> .\main.py
echo. >> .\main.py
echo if __name__ == '__main__': >> .\main.py
echo     solution() >> .\main.py