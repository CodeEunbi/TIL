# Many to one relationships

## 모델 관계

### Many to one relationships N:1 or 1:N

한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

### Comment(N) - Article(1)

0개 이상의 댓글은 1개의 게시글에 작성될 수 있다

### 테이블 관계


## 댓글 모델 정의

### ForeignKey()

한 모델이 다른 모델을 참조하는 관계를 설정하는 필드

→ N : 1관계 표현

→ 데이터베이스에서 외래 키로 구현

### 댓글 모델 정의

ForeignKey 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장

외래 키는 ForeignKey클래스를 작성하는 위치와 관계없이 테이블의 마지막 필드로 생성됨



<aside>
🔎

ForeignKey(to, on_delete)

- to : 참조하는 모델 class 이름
- on_delete : 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)
</aside>

<aside>
🔎

on_delete의 ‘CASADE’

- 참조된 객체(부모 객체)가 삭제될 때 이를 참조하는 모든 객체도 삭제되도록 지정
</aside>

### Migration 이후 댓글 테이블 확인

댓글 테이블의 article_id 외래키 필드 확인

만들어지는 필드 이름

- ‘참조 대상 클래스 이름’ + ‘_’ + ‘클래스 이름’

⇒ 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장 되었던 이유


## 댓글 생성 연습

<aside>
🔑

댓글 생성 연습

1. shell_plus 실행 및 게시글 작성
2. 댓글 생성
3. shelll_plus 실행 및 게시글 작성
4. comment 인스턴스를 통한 article 값 참조하기
5. comment 인스턴스를 통한 article 값 참조하기
6. 두 번째 댓글 생성
7. 작성된 댓글 데이터 확인
</aside>

1. shell_plus 실행 및 게시글 작성

2. 댓글 생성

**IntegrityError: NOT NULL constraint failed: articles_comment.article_id**

→ NOT NULL 제약 조건이 실패했다

무언가 값이 존재하지 않는다

무언가? → articles_comment.article_id

articles_comment 테이블의 article_id 필드의 값이 존재하지 않는다

3. shelll_plus 실행 및 게시글 작성

4. comment 인스턴스를 통한 article 값 참조하기

5. comment 인스턴스를 통한 article 값 참조하기

6. 두 번째 댓글 생성

7. 작성된 댓글 데이터 확인



## 관계 모델 참조

### 역참조

- N : 1 관계에서 1에서 N을 참조하거나 조회하는 것(1 → N)
- 모델 간의 관계에서 관계를 정의한 모델이 아닌, 관계의 대상이 되는 모델에서 연결된 객체들에 접근하는 방식

⇒ N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만, 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 키워드가 필요

<aside>
🔎

역참조

참조(comment → Article)

⇒ 1번 댓글이 작성된 게시글 정보

역참조(Article → comment)

⇒ 1번 게시글에 작성된 모든 댓글 정보 X

</aside>

```jsx
article.comment_set.all()
모델 인스턴스.related manager(역참조 이름).QuerySet API

# 특정 게시글에 작성된 댓글 전체를 조회하는 요청
```

### related manager

N : 1 혹은 M : N관계에서 역참조 시에 사용하는 매니저

→ objects 매니저를 통해 QuerySet API를 사용했던 것처럼 related manager를 통해 QuerySet API를 사용할 수 있게 됨

<aside>
❗

**related manager 이름 규칙**

- N :  1 관계에서 생성되는 Related manager의 이름은 ‘모델명_set’ 형태로 자동 생성됨
    - 관계를 직접 정의하지 않은 모델에서 연결된 객체들을 조회할 수 있게 함
- 특정 댓글의 게시글 참조(Comment → Article)
    - comment.article
- 특정 게시글의 댓글 목록 참조(Article → Comment)
    - article.comment_set.all()
</aside>

### related manager 연습

- shell_plus 실행 및 1번 게시글 조회

- 1번 게시글에 작성된 모든 댓글 조회하기(역참조)

- 1번 게시글에 작성된 모든 댓글 내용 출력


## 댓글 구현

1. 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm정의

2. detail view 함수에서 CommentForm을 사용하여 detail 페이지에 렌더링

3. View함수에서 처
- Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요한 필드이기 때문에 출력
- 하지만 외래 키 필드 데이터는 사용자로부터 입력 받는 값이 아닌 view 함수 내에서 다른 방법으로 전달받아 저장되어야함

4. CommentForm의 출력 필드 조정하여 외래 키 필드가 출력되지 않도록 함

5. 어디서 외래키 데이터를 받아야할까?
- detail 페이지의 URL을 살펴보면 path(’<int:pk>/’, views.detail, name=’detail’)에서 해당 게시글의 pk값이 사용되고 있음
- 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값

6. url 작성 및 action 값 작성

7. comments_create view 함수 정의
→ URL로 받은 pk 인자를 게시글을 조회하는데 사용

8. article 객체는 어떻게/언제 저장할 수 있을까?
save(commit=False)

: DB에 저장 요청을 보내지 않고 인스턴스만 반환

(Create, but don’t save the new instance)

9. save의 commit 인자를 활용해 외래 키 데이터 추가 입력

10. 댓글 작성 후 테이블 확인



### 댓글 READ

1. detail view 함수에서 전체 댓글 데이터를 조회

2. 전체 댓글 출력 및 확인



### 댓글 DELETE

1. 댓글 삭제 url 작성

2. 댓글 삭제 view 함수 정의

3. 댓글 삭제 버튼 작성

4. 댓글 삭제 버튼 출력 확인 및 삭제 테스트


---

# 참고

## 데이터 무결성

<aside>
🔑

데이터 무결성

- 데이터 베이스에 저장된 데이터의 정확성, 일관성, 유효성을 유지하는 것
- 데이터 베이스에 저장된 데이터 값의 정확성을 보장하는 것

중요성

1. 데이터의 신뢰성 확보
2. 시스템 안정성
3. 보안 강화
</aside>

### admin site 댓글 등록

Comment 모델을 admin site에 등록해 CRUD 동작 확인하기


### 댓글 추가 구현

1. 댓글이 없는 경우 대체 콘텐츠 출력 : DTL의 ‘for empty’태그 활용


2. 댓글 개수 출력하기
- DTL filter - ‘length’ 사용

- QuerySetAPI - ‘count()’ 사용