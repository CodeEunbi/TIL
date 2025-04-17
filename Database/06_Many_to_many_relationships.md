## 팔로우 기능 구현

### 프로필 페이지

각 회원의 개인 프로필 페이지에 팔로우 기능을 구현하기 위해 프로필 페이지를 먼저 구현

### 프로필 구현

url 작성

```python
# accounts/urls.py
urlpatterns = [
		...
		path('profile/<username>/', views.profile, name='profile'),
]
```

view 함수 작성

```python
# accounts/views.py

from django.contrib.auth import get_user_model

def profile(request, username):
		User = get_user_model()
		person = User.objects.get(username=username)
		context = {
				'person':person,
		}
		return render(request, 'accounts/profile.html', context)
```

profile 템플릿 구현


프로필 페이지로 이동할 수 있는 링크 작성

```jsx
# articles/index.html

<a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
```
프로필 페이지 결과 확인

### 모델 관계 설정

User(M) - User(N)

0명 이상의 회원은 0명 이상의 회원과 관련

→ 회원은 0명 이상의 팔로워를 가질 수 있고, 0명 이상의 다른 회원들을 팔로잉 할 수 있음

- ManyToManyField 작성
- 참조 : 내가 팔로우하는 사람들(팔로잉, followings)
- 역참조 : 상대방 입장에서 나는 팔로워 중 한 명(팔로워, followers)
- 바뀌어도 상관없으나 관계 조회 시 생각하기 편한 방향으로 정한 것

- Migrations 진행 후 중개 테이블 확인


## 기능 구현

url 작성

```jsx
# accounts/urls.py

urlpatterns = [
		...,
		path('<int:user_pk>/follow/', views.follow, name='follow'),
]

```

view 함수 작성

```jsx
@login_required
def follow(request, user_pk):
		User = get_user_model()
		person = User.objects.get(pk=user_pk)
		if person != request.user:
				if request.user in person.followers.all():
						person.followers.remove(request.user)
				else:
						person.followers.add(request.user)
			return redirect('accounts:profile', person.username)
```

프로필 유저의 팔로잉, 팔로워 수  & 팔로우, 언팔로우 버튼 작성

팔로우 버튼 클릭 → 팔로우 버튼 변화 및 중개 테이블 데이터 확인

## Fixtures

Django 개발 시 데이터베이스 초기화 및 공유를 위해 사용되는 파일 형식

### Fixtures 사용 목적

- 샘플, 초기 데이터 세팅
- 협업 시 동일한 데이터 환경 맞추기

### 초기 데이터의 필요성

<aside>
🚨

초기 데이터의 필요성

협업하는 유저 A, B가 있다고 하자

- A가 먼저 프로젝트를 작업 후 원격 저장소에 push wlsgod
    - gitignore로 인해 DB는 업로드하지 않기 때문에 A가 생성한 데이터도 업로드 X
- B가 원격 저장소에 A가 push한 프로젝트를 pull(혹은 clone)
    - 결과적으로 B는 DB가 없는 프로젝트를 받게 됨

이처럼 프로젝트의 앱을 처음 설정할 때 동일하게 준비된 데이터로 데이터 베이스를 미리 채우는 것이 필요한 순간이 있음

➡️ Django에서는 fixtures를 사용해 앱에 초기 데이터(initial data)를 제공

</aside>

### fixtures 관련 명령어

dumpdata : 생성(데이터 추출)

loaddata : 로드(데이터 입력)

사전준비 

M:N까지 모두 작성된 Django 프로젝트에서 유저, 게시글, 댓글 등 각 데이터를 최소 2~3개 이상 생성

### dumpdata

데이터베이스의 특정 모델 혹은 앱 전체 데이터를 추출

### dumpdata 기본 명령어

```jsx
$ python manage.py dumpdata [앱이름.모델이름] [옵션] > 추출파일명.json
```

- 앱이름.모델이름 지정 : 특정 모델의 데이터를 추출
- 앱이름만 지정 : 해당 앱의 모든 모델에 대한 데이터를 추출
- 앱 혹은 모델명을 지정하지 않은 경우 : 프로젝트 전체의 모델 데이터를 추출
- - - format 옵션을 통해 JSON, YAML 등의 형식 지정 가능(기본값: JSON)

### 명령어 예시

```jsx
$ python manage.py dumpdata --indent 4 articles.article > articles.json
```

- articles 앱의 Article모델 데이터를 추출
- 명령어 실행 후 프로젝트 폴더에 articles.json파일이 생성됨
- artocles.json파일에는 Article 모델의 모든 데이터가 JSON 형식으로 작성되어있음

⇒ Fixtures 파일명은 자유롭게 작성 가능

```jsx
$ python manage.py dumpdata --indent 4 accounts.user > users.json
$ python manage.py dumpdata --indent 4 articles.comment > comments.json
```
**Fixtures 파일을 직접 만들지 말것! 반드시 dumpdata 명령어를 사용해서 생성** 

### dumpdata 정리

<aside>
🚨

**dumpdata 정리**

- dumpdata 명령어를 사용하면 프로젝트 내 특정 앱 혹은 모델에 대한 데이터를 JSON 등 원하는 포맷으로 추출 가능
- 이렇게 생성된 데이터 파일은 추후 다른 환경에서 loaddata로 불러와 동일한 데이터 상태를 재현할 수 있으며 협업 및 배포에 큰 장점이 있음
</aside>

## loaddata

dumpdata를 통해 추출한 데이터 파일을 다시 데이터베이스에 반영

### loaddata 기본 명령어

```jsx
$ python manage.py loaddata 파일 경로
```

- Fixtures 파일의 기본 경로에 있는 파일을 DB에 반영
- Fixtures 파일의 기본 경로 : app_name/fixtures
- Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾아 load 진행

사전 준비

dumpdata로 생성한 파일들을 해당 위치로 이동

db.sqltie3 파일 삭제 후 migrate 진
### loaddata 명령어 예시

```jsx
$ python manage.py loaddata articles.json users.json comments.json
```

- dumpdata로 생성한 파일들을  모두 DB에 반영
- 파일은 작성 순서에 상관 없음

```jsx
$ python manage.py loaddata users.json
$ python manage.py loaddata articles.json
$ python manage.py loaddata comments.json
```

- 단 loaddata를 한번에 실행하지 않고 별도로 실행한다면 모델 관계에 따라 load 순서가 중요할 수 있음
    - comment는 article에 대한 key 및 user에 대한  key가 필요
    - article은 user에 대한 key가 필요
- 현재 모델 관계에서는 user → article → comment 순으로 data를 load해야 오류가 발생하지 않음

### loaddata 주의 사항

<aside>
⚠️

**loaddata 주의 사항**

- loaddata를 실행하기 전에 해당 모델에 대한 마이그레이션이 완료되어있어야함
- 같은 pk를 가진 데이터가 이미 있는 경우 중복 에러가 발생할 수 있음
    - 이 경우 기존 데이터를 지우거나, 새로운 fixture 파일을 사용해야함
</aside>

### loaddata 정리

<aside>
🔎

**loaddata 정리**

- loaddata 명령어는 dumpdata로 추출한 Fixture 파일을 DB로 불러오는 명령어이며, 개발 환경 준비나 협업 시 매우 유용
- 마이그레이션 상태를 먼저 확인하고, 인코딩 문제 등을 사전에 해결하면 매끄럽게 데이터를 복원할 수 있음
</aside>

## Improve query

‘query 개선하기’ ⇒ 같은 결과를 얻기 위해 DB측에 보내는 query 개수를 점차 줄여 조회하기

사전준비

- fixtures 데이터 : 게시글 10개, 댓글 100개, 유저 5개
- 모델 관계
    - N : 1 - Article : User / Comment : Article / Comment : Article
    - N : M - Article : User
    
    

서버 실행 후 확인


## annotate

- SQL의 GROUP  BY 사용
- 쿼리셋의 각 객체에 계산된 필드를 추가
- 집계 함수(Count, Sum 등)와 함께 사용

### annotate 예시

```jsx
Book.objects.annotate(num_authors=Count('authors'))
```

- 의미
    - 결과 객체에 ‘num_authors’라는 새로운 필드를 추가
    - 이 필드는 각 책과 연관된 저자의 수를 계산
- 결과
    - 결과에는 기존 필드와 함께 ‘num_authors’필드를 가지게 됨
    - book.num_authors로 해당 책의 저자 수에 접근할 수 있게 됨
    
    ### 문제 상황
    
- 문제 원인 : 각 게시글마다 댓글 개수를 반복 평가

```jsx
<!-- index_1.html-->

<p>댓글 개수 : {{ article.comment_set.count }}</p>
```

### annotate 적용

- 문제 해결 : 게시글을 조회하면서 댓글 개수까지 한번에 조회해서 가져오기

- 문제해결 :  ‘ 11 queries including 10 similar’ ⇒ ‘1 query’

## select_related

- SQL의 INNER JOIN를 사용
- 1:1 또는 N:1 참조 관계에서 사용
    - ForeignKey나 OneToOneField관계에 대해 JOIN을 수행
- 단일 쿼리로 관련 객체를 함께 가져와 성능을 향상

### select_related 예시

```jsx
Book.objects.select_related('publisher')
```

의미

- Book 모델과 연관된 publisher 모델의 데이터를 함께 가져옴
- ForeignKey관계인 ‘publisher’를 JOIN하여 단일 쿼리 만으로 데이터 조회

결과

- Book 객체를 조회할 때 연관된 Publisher 정보도 함께 로드
- book.publisher.name과 같은 접근이 추가적인 데이터베이스 쿼리없이 가능

### 문제 상황

- 문제 원인 : 각 게시글마다 작성한 유저명까지 반복 평가

```jsx
<!-- index_2.html -->

{% for article in articles %}
		<h3>작성자 : {{ article.user.username }}</h3>
		<p>제목 : {{ article.title }}</p>
		<hr>
{% endfor %}
```

### selected_related 적용

- 문제 해결 : 게시글을 조회하면서 유저 정보까지 한번에 조회해서 가져오기

- 문제 해결 : ‘11 queries including 10 similar and 8 duplicates’ ⇒ ‘1 query’

## prefetch_related

- SQL이 아닌 python을 사용한 JOIN을 진행
    - 관련 객체들을 미리 가져와 메모리에 저장하여 성능을 향상
- M:N 또는 N:1 역참조 관계에서 사용
    - ManyToManyField나 역참조 관계에 대해 별도의 쿼리를 실행

### prefetch_related 예시

```jsx
Book.objects.prefetch_related('authors')
```

의미

- Boook과 Author는 ManyToMany 관계로 가정
- Book 모델과 연관된 모든 Author 모델의 데이터를 미리 가져옴
- Django가 별도의 쿼리로 Author 데이터를 가져와 관계를 설정

결정

- Book 객체들을 조회한 후, 연관된 모든 Author 정보가 미리 로드
- for author in book.authors.all()와 같은 반복이 추가적인 데이터베이스 쿼리 없이 실행됨

### 문제 상황

문제 원인 : 각 게시글 출력 후 각 게시글의 댓글 목록까지 개별적으로 모두 평가

```jsx
<!-- index_3.html -->

{% for article in articles %}
		<p>제목 : {{ article.title }}</p>
		<p>댓글 목록</p>
		{% for comment in article.comment_set.all %}
				<p>{{ comment.content }}</p>
		{% endfor %}
		<hr>
{% endfor %}
```

### prefetch_related 적용

문제 해결 : 게시글을 조회하면서 참조된 댓글까지 한번에 조회해서 가져오기

문제 해결 : ‘11 queries including 10 similar’ → ‘2 queries’

## select_related & prefetch_related

### 문제 상황

### 문제 원인

- ‘게시글’ + ‘각 게시글의 댓글 목록’ + ‘댓글의 작성자’를 단계적으로 평가

```jsx
<!-- index_4.html -->

{% for article in articles %}
		<p>제목 : {{ article.title }}</p>
		<p>댓글 목록</p>
		{% for comment in article.comment_set.all %}
				<p>{{ comment.user.username }} : {{ comment.content }}</p>
		{% endfor %}
		<hr>
{% endfor %}
```

### prefetch_related 적용

문제해결 1단계

- 게시글을 조회하면서 참조된 댓글까지 한번에 조회


- ‘111 queries including 110 similar and 100 duplicates’

→ ‘102 queries including 100 similar and 100 duplicates’


아직 각 댓글을 조회하면서 각 댓글의 작성자를 중복 조회중

## select_related & prefetch_related 적용

문제 해결 2단계

- ‘게시글’ + ‘각 게시글의 댓글 목록’ + ‘댓글의 작성자’를 한번에 조회

- ‘102 queries including 100 similar and 100 duplicates’

→ 2 queries

---

# 참고

## ‘exists’ method

### .exists()

- QuerySet에 결과가 하나 이상 존재하는지 여부를 확인하는 메서드
- 결과가 포함되어있으면 True를 반환하고 결과가 포함되어있지 않으면 False를 반환

### .exists() 특징

- 데이터베이스에 최한의 쿼리만 실해앟여 효율적
- 전체 QuerySet을 평가하지 않고 결과의 존재 여부만 확인

→ 대량의 QuerySet에 있는 특정 객체 검색에 유용

### exists 적용 예시

## 한꺼번에 dump 하기

- 다만 모든 데이터를 한 번에 추출할 경우 파일 용량이 커질 수 있으므로, 필요에 따라 특정 앱만 추출하거나 파일을 압축하여 관리하는 방법을 고려
- 데이터 베이스 변경이 잦은 경우 전체 추출보다는 앱 단위 또는 모델 단위로 관리하는 편이 유지 보수에 용

## loaddata인코딩 에러 해결법

### 인코딩 문제

- JSON 파일 생성 및 로딩 시, 파일이 특정 문자 인코딩(ex. UTF-8)으로 저장되지 않으면 한글 등 비ASCII 문자가 깨지거나 UnicodeDecodeError 등의 에러가 발생할 수 있음
- 윈도우 환경에서 생성한 파일을 리눅스 환경에서 로딩할 때 혹은 반대 상황에서 인코딩 이슈가 빈번히 발생