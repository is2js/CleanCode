@echo off

:: 첫번째 인자에 첫번 째폴더명 약어를 받아, 변수에 할당한다.
if "%1" == "cc" (
    SET FIRST_FOLDER=cleancode
) else if "%1" == "cpt" (
    SET FIRST_FOLDER=concept
) else if "%1" == "sg" (
    SET FIRST_FOLDER=seulgi_python_trick
) else (
    SET FIRST_FOLDER=%1
)

if not exist ".\%FIRST_FOLDER%\" md ".\%FIRST_FOLDER%"

:: 2번재인자%2으로 폴더가 없으면 생성하고, 이미 있으면 에러를 띄운다.
:: 1번째인자\2번째 인자폴더를 현재폴더로 인식한다.
if not exist ".\%FIRST_FOLDER%\%2" (
        md ".\%FIRST_FOLDER%\%2"
    ) else (
        echo "already have folder"
        GOTO:EOF
    )
    ::변수할당시 = 사이에 공백이 있으면 안된다.
    Set CURRENT_FOLDER=%FIRST_FOLDER%\%2
)

::root폴더에 작성한 *.py파일들을 인자로 생성된 폴더로 다 이동시킨다.
copy .\*.py .\%CURRENT_FOLDER% /DHKYCSIL

del .\*.py

::기존 Main.py 초기문장 적어 초기화
echo import sys > .\main.py
echo. >> .\main.py
echo input = sys.stdin.readline >> .\main.py
echo. >> .\main.py
echo. >> .\main.py
echo if __name__ == '__main__': >> .\main.py
echo     pass >> .\main.py