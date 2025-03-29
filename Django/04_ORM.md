## ORM

### ORM(Object-Relational-Mapping)

객체 지향 프로그래밍 언어를 사용하여 호환되지 않은 유형의 시스템 간에 데이터를 변환하는 기술

장고의 잔여물이 아님

### ORM의 역할

Django와 DB간에 사용하는 언어가 다르기 때문에 소통 불가



Django에 내장된 ORM이 중간에서 이를 해석

---

## QuerySet API

ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구

→ API를 사용하여 SQL이 아닌 python 코드로 데이터를 처리



### QuerySet API 구문

- 메서드로 동작
- Model class는 바로 사용할 수 없기 때문에 objects manager를 이용해 메서드 호출

### QuerySet API 구문 동작 예시



### Query

- 데이터 베이스에 특정한 데이터를 보여달라는 요청
- ‘쿼리문을 작성한다’ → 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

### QuerySet

- 데이터 베이스에게서 전달받은 객체 목록(데이터모음)
    - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
    - 리스트(인덱스, 반복, 슬라이싱 등)
- Django ORM을 통해 만들어진 자료형
- 단 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환

<aside>
💡

**QuerySet API는 python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것**

</aside>

### CRUD

소프트웨어가 가지는 기본적인 데이터 처리 기능

Create(저장) Read(조회) Update(갱신) Delete(삭제)

---

## 실습

### Create


- 한번에 설치도 가능

```python
$ pip install ipython django-extension   # 공백이 기준
```

- 공식문서에서 하나씩 복사해서 가져오기(하이픈 차이도 있음)

```python
# Application definition
# 앱 순서

INSTALLED_APPS = [
    # 직접 생성한 앱을 첫번째로
    'articles',
    # 설치한 앱(3rd party library)
    'django_extensions',
    # 내장 앱
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Django shell 실행


- Django 환경 안에서 실행되는 python shell(입력하는 QuerySet API구문이 Django프로젝트에 영향을 미침)



- 장고의 내장함수를 import
- for articles.models import Article → 유일하게 밖에서

데이터 객체를 만드는(생성하는) 3가지 방법

1. **첫번째 방법**

⇒ 테이블에 글이 작성됨

등록 후 


- pk :  primary key(id 값이랑 똑같음)
- created_at : 날짜
- id가 없으면 테이블 생성이 안됨

2. **두번째 방법**
- Save 메서드를 호출해야 비로소 DB에 데이터가 저장됨
- 테이블에 한 행(레코드)이 쓰여진 것

- 저장하면 리스트에 저장돼서 나옴
    

    

3. **세번째 방법**
- QuerySet API 중 create() 메서드 활용



- 한 줄로 끝남


In[22],Out[22] : 3번째 글 만듦→ output이 있음

In[23], Out[23] : 출력하면 바로 저장되었다는 사실을 알 수 있음

- save 필요 없음

### save()

객체를 데이터베이스에 저장하는 인스턴스 메서드

- Model 메서드 안에 있을,,
- 게시글이 안써지는 이유는 save()를 하지 않아서 일 확률이 높음

### Read

<aside>
🔎

**대표적인 조회 메서드**

- Return new QuerySets
    - all
    - filter()
- Do note return QuerySets
    - get()
    

⇒ 반환값이 있다는 것은 변수를 다룰 수 있다..!

</aside>

**all()** : 전체 데이터 조회


**filter()**: 주어진 매개변수와 일치하는 객체를 포함하는 QuerySet을 반환

- 무조건 QuerySet, 개수 상관 없음, 0개 이상



**get()** : 주어진 매개변수와 일치하는 객체를 반환

- 반환값이 Query가 아님



- 1번 게시글을 조회한 것(⬆️⬆️⬆️)
- 범위를 벗어난 에러



- 값이 여러개일 때의 에러


- 객체를 찾을 수 없으면 DoesNotExist예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

→ 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야함

→ 유일한 값이 있는 것만 조회해라 라는 것(pk)

### Update

데이터 수정 : 인스턴스 변수를 변경 후 save 메서드 호출

- 수정을 하려면 조회하는 게 먼저!
- 조회하고 재할당 후 저장!!!
- 저장해야 테이블이 바뀜(상태를 저장하는게 아니라 생성한다고 생각)


### Delete

데이터 삭제 : 삭제하려는 데이터 조회 후 delete 메서드 호출

- 조회를 먼저하고 삭제(update와 공통점)
- 굳이 저장을 하지 않아도 됨(제거하는 거니까)
- 지워진 pk값을 재활용하지 않음(ex, 2를 삭제했다면 2는 재생성X)
- 튜플을 반환(소괄호)

- 삭제 후 조회하면 조회가 되지 않음


---

## ORM with view

### 전체 게시글 조회

<aside>
📌

1. **전체 게시글 조회 ← 요거만!✅**
2. **단일 게시글 조회**
</aside>

1. 전체 게시글 조회


---

# 참고

## Field lookups

- 더 세부적인 문법을 거는 방법
- Query에서 조건을 구성하는 방법
- QuerySet메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨



## ORM, QuerySet API를 사용하는 이유

<aside>
💡

1. **데이터 베이스 추상화**
- 개발자는 특정 데이터베이스 시스템에 종속되지 않고 일관된 방식으로 데이터를 다룰 수 있음

2. **생산성 향상**
- 복잡한 SQL 쿼리를 직접 작성하는 대신 Python 코드로 데이터베이스 작업을 수행할 수 있음

3. **객체 지향적 접근**
- 데이터베이스 테이블을 Python 객체로 다룰 수 있어 객체 지향 프로그래밍의 이점을 활용할 수 있음
</aside>