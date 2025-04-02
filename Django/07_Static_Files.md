## static files(정적파일)

서버 측에서 변경되지 않고 고정적으로 제공되는 파일(이미지, JS, CSS 파일 등)

**웹 서버와 정적 파일**

- 웹 서버의 기본 동작은 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서 응답(HTTP response)을 처리하고 제공하는 것


🙊 사진이 뜨지 않을 때 : **개발자 도구 켜기 → 크롬 새로고침 우클릭 → 캐시 비우기 및 강력 새로고침**

<aside>
📌

**Static files 경로**

1. 기본 경로
2. 추가 경로
</aside>

### 1. 기본경로

app폴더/ static

기본 경로 static file 제공

- articles/static/articles/ 경로에 이미지 파일 배치


- static files 경로는 DTL의 static tag를 사용해야함
- built-in tag가 아니기 때문에 load tag를 사용해 import 후 사용 가능


- static url 확인(안되면 서버 껐다 켜기)

- URL을 누르면 이미지만 제공해줌

### Static_URL

기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL

→ 실제 파일이나 디렉토리 경로가 아니며, URL로만 존재

- [settings.py](http://settings.py) 파일 제일 밑에 있음


<aside>
🔎

URL + STATIC_URL + 정적 파일 경로

http://127.0.0.1:8000/static/articles/sample-1.png

</aside>

### 2. 추가 경로

STATICFILES_DIRS에 문자열 값으로 추가 경로 설정

STATICFILES_DIRS : 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

**추가경로 static**

- 임의의 추가 경로 설정


- 추가 경로에 이미지 파일 배치



- static tag를 사용해 이미지 파일에 대한 경로 제공


- 이미지를 제공 받기 위해 요청하는 Request URL 확인


⇒ **정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요하다!**

---

# Media files

사용자가 웹에서 업로드하는 정적 파일(user-uploaded)

## 이미지 업로드

### ImageField()

이미지 업로드에 사용하는 모델 필드

- 이미지 객체가 직접 DB에 저장되는 것이 아닌 ‘이미지 파일의 경로’ 문자열이 저장됨
- 표 안에 직접적으로 이미지를 넣을 수 없음

<aside>
🔎

미디어 파일을 제공하기 전 준비사항

1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 URL 지
</aside>

### MEDIA_ROOT

미디어 파일들이 위치하는 디렉토리의 절대 경로


### MEDIA_URL

MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)



### MEDIA_ROOT와 MEDIA_URL에 대한 URL 지정

업로드 된 파일의 URL == settings.MEDIA_URL

MEDIA_URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT


(공식 문서)

**이미지 업로드**

- blank=True 속성을 작성해 빈 문자열이 저장될 수 있도록 제약 조건 설정

→ 게시글 작성 시 이미지 업로드 없이도 작성할 수 있도록 하기 위함


- migration 진행


- form요소의 enctype 속성 추가


- ModelForm의 2번째 인자로 요청받은 파일 데이터 작성
    - ModelForm의 상위 클래스 BaseModelForm의 생성자 함수의 2번째 위치 인자로 파일을 받도록 설정되어있음

- 이미지 업로드 input 확인



- 이미지 업로드 결과 확인



- 옆 파일에 media가 생기면 업로드가 되었다고 할 수 있음
    - 그 후 DB확인하기
- 동일한 파일명의 이미지를 업로드 하면 → 충돌이 나지 않고 같은 이름 뒤에 난수를 붙임
    - 파일명 구분을 친절히 해줌

### 업로드 이미지 제공

업로드 이미지 제공하기

- ‘URL’ 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
- article.image.url
    - 업로드 파일의 경로
- article.image
    - 업로드 파일의 파일 이름
    
    
- 업로드 이미지 출력 확인 및 MEDIA_URL 확인

- 이미지에 URL 주소가 생겼다~

<aside>
🔎

http://127.0.0.1:8000/media/kirby_05AqwH8.png 

> media가 경로에 있는 이유는 우리가 지정했기 때문에 MEDIA_URL

</aside>

- 이미지가 없는 페이지를 누르면 에러 → 조건문 만들어주기
- 이미지를 업로드하지 않은 게시물은 detail 템플릿을 렌더링 할 수 없음
- 이미지 데이터가 있는 경우만 이미지를 출력할 수 있도록 처리하기



### 업로드 이미지 수정

- 수정 페이지 form 요소에 enctype 속성 추가

- update view함수에서 업로드 파일에 대한 추가 코드 작성
    - instance는 9번째 인자기 때문에 앞에 작성해주기
- 삭제 하면 → 이미지 파일이 지워지진 않음
    - 그러면 이미지가 계속 쌓이는데 안쌓아지게 하는 라이브러리도 있고 클라우드에서 정적파일을 받아주는 경우도 있음


---

# 참고

## 미디어 파일 추가 경로

### ‘upload_to’ argument

ImageField()의 upload_to 속성을 사용해 다양한 추가 경로 설정

- 미디어 루트 이후 경로

2번째 방식 

→ 업로드 날짜 폴더가 생기고 그 안에 이미지 가 들어감


## BaseModelForm

### request.FILES가 두번째 위치 인자인 이유

ModelForm의 상위 클래스 BaseModelForm의 생성자 함수 키워드 인자 참고

- views.py안에 있는 request넣는 순서