## 파이썬 클린코드 학습



### 📜 학습 교재

- [참고 블로그](https://dailyheumsi.tistory.com/category/%EB%8D%94%20%EB%82%98%EC%9D%80%20%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EA%B0%80%20%EB%90%98%EA%B8%B0%20%EC%9C%84%ED%95%B4/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%8A%A4%EB%9F%BD%EA%B2%8C)

| 교재명 | Python cleancode                                             | Python Tricks                                                | etc                   |
| :----: | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------- |
| 이미지 | ![image-20220716012838378](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220716012838378.png) | ![image-20220717004101722](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220717004101722.png) |                       |
|  폴더  | [cleancode](../cleancode)                                    | [seulgi_python_trick](../seulgi_python_trick)                | [concept](../concept) |



### ✒ pycharm, pylint, black 세팅

- [돌범의 pycharm 세팅 및 단축키 설정 블로그 글](https://blog.chojaeseong.com/pycharm/settings/shortcut/2022/02/13/pycharrm_settings_shortcut.html)



### 🛠 학습 세팅

- learn.bat 작성한다.

    - **배치파일을 통해 학습한 파이썬 파일을 폴더별로 자동 백업한다.** 

- root폴더에서 main.py외에 필요한 py파일들을 만들어서 특정chapter를 학습한다.

- 학습 종료 후 아래와 같은 커맨드를 통해 학습내용을 정리한다.
    ```shell
    ./learn.bat [cc(cleancode) or cpt(concept) or sg(seulgi_python_trick)그외] [하위 chapter폴더명]
    ```
  ![521dc07c-45b8-4ffa-b87b-c89efd5f6c39](https://raw.githubusercontent.com/is3js/screenshots/main/521dc07c-45b8-4ffa-b87b-c89efd5f6c39.gif)
  