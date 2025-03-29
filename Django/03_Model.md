## Model

## model class

### Model을 통한 DB(데이터베이스) 관리



### Django Model

DB의 테이블을 정의하고 데이터를 조작(생성, 조회, 수정, 삭제 - CRUD)할 수 있는 기능들을 제공

→ 테이블 구조를 설계하는 청사진(blue print)


작성한 모델 클래스는 최종적으로 DB에 테이블 구조를 만들음



django.db.models 모듈의 Model이라는 부모 클래스를 상속받음

Model은 model에 관련된 모든 코드가 이미 작성되어있는 클래스

⇒ 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것(상속을 활용한 프레임워크의 기능 제공)

클래스 변수명 - 테이블의 각 ‘필드(열) 이름’



Model Field

- 데이터 베이스 테이블의 열(column)을 나타내는 중요한 구성 요소
- 데이터 유형과 제약 조건을 정의

---

## Model Field

DB 테이블의 필드(열)을 정의하며, 해당  필드에 저장되는 데이터 타입(Field types)과 제약조건(field option)을 정의

<aside>
🔎

Model Field 구성

1. Field types(필드 유형)
- 데이터 베이스에 저장될 ‘데이터의 종류’를 정의

2. Field options(필드 옵션)
- 필드의 동작과 제약 조건을 정의
</aside>

### Field types

데이터베이스에 저장될 ‘데이터 종류’를 정의

(models 모듈의 클래스로 정의되어 있음)


- CharField()
    - 제한된 길이의 문자열을 저장(필드의 최대 길이를 결정하는 max_length는 필수 옵션)
    - id는 신경 쓸 필요 없음
- TextField()
    - 길이 제한이 없는 대용량 텍스트를 저장(무한대는 아니며 사용하는 시스템에 따라 달라짐)

<aside>
💡

**주요 필드 유형**

- 문자열 필드
    - CharField, TextField
- 숫자 필드
    - IntegerField, FloatField
- 날짜/시간 필드
    - DataField, TimeField, DataTimeField
- 파일 관련 필드
    - FileField, ImageField
</aside>

### Field options

필드의 ‘동작’과 ‘제약 조건’을 정의


제약 조건(Constraint)

- 특정 규칙을 강제하기 위해 테이블의 열이나 행에 적용되는 규칙이나 제한사항

→ 숫자만 저장되도록, 문자가 100자까지만 저장되도록 하는 등

<aside>
💡

주요 필드 옵션

- null
    - 데이터 베이스에서 Null값을 허용할지 여부를 결정(기본값 : False)
- blank
    - form에서 빈 값을 허용할 지 여부를 결정(기본값 : False)
- default
    - 필드의 기본값을 설정
</aside>

---

# Migrations

model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법



**핵심 명령어 2가지**

model class를 기반으로 최종 설계도(migration)작성



최종 설계도를 DB에 전달하여 반영



migrate 후 DB내에 생성된 테이블 확인

(앱이름_클래스 이름 → 테이블 이름)


**추가 Migrations**

추가 모델 필드 작성



auto_now : 데이터가 저장될 때마다 **자동**으로 현재 날짜 시간을 저장

auto_now_add : 데이터가 **처음 생성될때만** 자동으로 현재 날짜 시간을 저장

#아직 반영 안됨 → 최종 설계도로 반영해줘야 되기 때문

 

이미 기존 테이블이 존재하기 때문에 필드를 추가할 때 필드의 기본값 설정이 필요

1번은 현재 대화를 유지하면서 직접 기본값을 입력하는 방법

2번은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법


추가하는 필드의 기본 값을 입력해야하는 상황

날짜 데이터이기 때문에 직접 입력하기 보다 Django가 제안하는 기본값을 사용하는 것을 권장

아무것도 입력하지 않고 enter를 누르면 django가 제안하는 기본값으로 설정



migrations 과정 종료 후 2번째 migration파일이 생성됨을 확인

이처럼 Django는 설계도를 쌓아가면서 추후 문제가 생겼을 시 복구하거나 되돌릴 수 있도록 함(마치 git commit 과 유사)



2번 폴더는 1번 폴더에 의존한다 → 1번 설계도가 없다면 파일을 열 수 없음

migrate 후 테이블 필드 변화 확인



model class에 변경사항(1)이 생겼다면, **반드시 새로운 설계도를 생성(**2)하고, 이를 DB에 반영(3)해야한다

1. model class 변경 → 2. makemigrations → 3. migrate

#테이블에 새로고침 있으니까 새로고침하기

#데이터 연혁 쌓기

#실습할 때는 지우고 다시 migration해보기

---

# Admin site

## 관리자 인터페이스

### Automatic admin interface

Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스

- 장고는 관리자 계정이 구현되어있음

→ 데이터 확인 및 테스트 등을 진행하는데 매우 유용

1. admin 계정 생성
- email은 선택사항이기 때문에 입력하지 않고 진행가능
- 비밀번호 입력 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기
    - 빨간 글씨로 비밀번호가 username이랑 비슷하다고 나와도 그대로 쓸 것인지 y/N해서 물어봄

2. DB에 생성된 admin계정 확인
- 우리가 굳이 테이블을 만들지 않아도 진작에 생성할 때 생긴 곳

- password 암호화해서 나옴
- 로그인 한적이 없기 때문에 last_login → Null

3. admin에 모델 클래스 등록
- admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능


4. admin site로그인 후 등록된 모델 클래스 확인

5. 데이터 생성, 수정, 삭제테스트
- field 따로 만들어서


6. 테이블 확인
- 시간은 UTC 기준으로 저장됨


---

# 참고

## 데이터베이스 초기화

1. migration 파일 삭제
2. db.sqlite3

아래 파일과 폴더를 지우지 않도록!

- __ init __ . py
- migrations 폴더


### migrations 관련

migrations 기타 명령어



- migrations 파일들이 migrate됐는지 안됐는지 여부를 확인하는 명령어
- [X]표시가 있으면 migrate가 완료되었음을 의미



- 해당 migrations 파일이 SQL언어(DB에서 사용하는 언어)로 어떻게 번역 되어 DB에 전달되는지 확인하는 명령어

첫 migrate 시 출력 내용이 많은 이유는?

Django 프로젝트가 동작하기 위해 미리 작성되어있는 기본 내장 app들에 대한 migration파일들이 함께 migrate되기 때문

## SQLite

데이터베이스 관리 시스템 중 하나이며 Django의 기본 데이터베이스로 사용됨(파일로 존재하며 가볍고 호환성이 좋음)