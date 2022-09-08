## 파이썬 클린코드 학습



### 📜 학습 교재

- [참고 블로그](https://dailyheumsi.tistory.com/category/%EB%8D%94%20%EB%82%98%EC%9D%80%20%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EA%B0%80%20%EB%90%98%EA%B8%B0%20%EC%9C%84%ED%95%B4/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%8A%A4%EB%9F%BD%EA%B2%8C)

| 교재명 | Python cleancode                                             | Python Tricks                                                | Pythonic                                                     |
| :----: | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 이미지 | ![image-20220716012838378](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220716012838378.png) | ![image-20220717004101722](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220717004101722.png) | ![image-20220727190948380](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220727190948380.png) |
|  폴더  | [cleancode](../cleancode)                                    | [seulgi_python_trick](../seulgi_python_trick)                | [pythonic](../pythonic)                                      |
|        |                                                              |                                                              |                                                              |
| 이미지 |                                                              |                                                              |                                                              |
|  폴더  |                                                              |                                                              |                                                              |





### ✒ pycharm 및 pylint, black 세팅

- [돌범의 pycharm 세팅 및 단축키 설정 블로그 글](https://blog.chojaeseong.com/pycharm/settings/shortcut/2022/02/13/pycharrm_settings_shortcut.html)





### 🛠 학습 세팅

- `learn.bat` 작성한다.

    - **배치파일을 통해 학습한 root에서 .py파일들로 학습만 파일들을 폴더별로 자동 백업한다.** 
    - root폴더에서 main.py외에 필요한 py파일들을 만들어서 특정chapter를 학습한다.

- 학습 종료 후 아래와 같은 커맨드를 통해 학습내용을 정리한다.
    ```shell
    ./learn.bat cc[sg,cpt,pn] 하위_chapter_폴더명
    ```
  ![image-20220722010621957](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220722010621957.png)
  
  
  ![521dc07c-45b8-4ffa-b87b-c89efd5f6c39](https://raw.githubusercontent.com/is3js/screenshots/main/521dc07c-45b8-4ffa-b87b-c89efd5f6c39.gif)





### 학습교재별 요약

#### CleanCode

| 매직 메서드                      | 예시 문                                                      | 컨셉            | 용례                                                         |
| -------------------------------- | ------------------------------------------------------------ | --------------- | ------------------------------------------------------------ |
| `__getitem__`                    | `obj[index]`<br />`obj[i:j]`<br />`obj[i:j:k]`<br />`obj[-1]`<br />`obj[::-1]` | 첨자형 객체     | 객체 컬렉션 속성을 객체로 인덱싱                             |
| `__enter__`<br />`__exit__`      | `with obj as :`<br />`class decorator`                       | 컨테스트 관리자 | with에 들어갈 객체<br />class로 만드는 데코레이터            |
| `__iter__/__next__`              | `for i in obj:`                                              | 이터러블 객체   | a,b범위값을 가져, 호출마다 한칸씩 이동하면서 해당요소 생성후 반환 |
| `__getitem__/__len__`            | `for i in obj:`                                              | 시퀀스객체      | a,b범위값으로 생성자에서 컬렉션을 만들고, 호출시마다 인덱싱해서 반환 |
| `__contains__`                   | ` in obj`                                                    | 컨테이너 객체   | 정답범위를 필드로 가지고 있어 특정객체 범위검사시 `in`으로 확인하게 한다. |
| `__getattribute__ / __getattr__` | `obj.attribute`                                              | 동적 속성조회   | 객체의 필드 호출시 없어도 호출되는 attribute와 없으면 AttributeError를 반환하는 getattr를 이용해서 없는 특정 필드에 대한 예외처리를 함 |
| `__call__`                       | `obj(item)`                                                  | 호출형 객체     | 함수말고 객체자체도 ()로 호출할 수 있게 함. 처리에 필요한 상태는 객체 속성으로 가지고 있어야함. |

