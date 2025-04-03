## 회원가입

User 객체를 create하는 과정

- GET, POST 요청 두가지를 받음
    - GET → 페이지 응답
    - POST → 실제 유저 생성

### UserCreationForm()

회원가입 시 사용자 입력 데이터를 받는 built-in ModelForm

### 회원가입 페이지 작성



회원가입 페이지 확인(UserCreationForm임)

- [settings.py](http://settings.py) → language_code → ko-kr로 하면 한글로 바뀜


### 회원가입 로직 작성


### 회원 가입 로직 에러

회원 가입 시도 후 에러 페이지 확인

→ Manager isn’t available; ‘auth.User’has been swapped for ‘accounts.User’


회원가입에 사용하는 UserCreationForm이 대체한 커스텀 유지 모델이 아닌 과거 Django의 기본 유저 모델로 인해 작성된 클래스이기 때문



### 커스텀 유저 모델을 사용하려면 다시 작성해야하는 Form

**UserCreationForm /  UserChangeForm(회원정보 수정)**

⇒ 두 Form 모두 **class Meta: model = User** 가 작성된 Form이기 때문에 재작성 필요

### UsercreationForm과 UserChangeForm 커스텀

Custom User model을 사용할 수 있도록 상속 후 일부분만 재작성



### get_user_model()

‘현재 프로젝트에서 활성화된 사용자 모델(active user model)’을 반환하는 함수

<aside>
🚫

User 모델을 직접 참조하지 않는 이유

- get_user_model()을 사용해 User모델을 참조하면 커스텀 User모델을 자동으로 반환해주기 때문
- Django는 필수적으로  User클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야한다고 강조하고 있음

➡️ User model 참조에 대한 자세한 내용은 추후 모델 관계에서 다룰 예정

</aside>

### 회원가입 로직 완성

CustomUserCreationForm으로 변경



회원가입만 하고 로그인을 하지 않았기 때문에 ~님이 뜨지 않음

## 회원탈퇴

User 객체를 Delete 하는 과정

- delete할 때 유저 조회를 굳이 하지 않아도 됨
    - 애초에 탈퇴라는 건 로그인이 되어있는 상태에서 요청을 보내기 때문
    - 요청 객체 안에 이미 어떤 사용자가 요청을 보내는 건지 정보가 있음
    - request.user

### 회원 탈퇴 로직 작성



회원탈퇴 진행



## 회원 정보 수정

User 객체를 Update하는 과정

### UserChangeForm()

회원정보 수정 시 사용자 입력 데이터를 받는 built-in ModelForm

### 회원정보 수정 페이지 작성



회원정보 수정 페이지 확인


<aside>
⛔

UserChangeForm 사용시 문제점

- User 모델의 모든 정보들(fields)까지 모두 출력됨
- 일반 사용자들이 접근해서는 안되는 정보는 출력하지 않도록 해야함

⇒ CustomUserChangeForm에서 출력 필드를 다시 조정하기

</aside>

### CustomUserChangeForm 출력 필드 재정의

User Model의 필드 목록 확인


회원정보 수정 페이지 확인


괄호안에 넣어주지 않아서 데이터 저장이 되어도 페이지에서는 기존 데이터를 보여주지 않음

### 회원정보 수정 로직 완성



## 비밀번호 변경

인증된 사용자의 Session 데이터를 Update하는 과정

### PasswordChangeForm()

비밀번호 변경 시 사용자 입력 데이터를 받는 built-in Form

### 비밀번호 변경 페이지 작성

django는 비밀번호 변경 페이지를 회원정보 수정 form 하단에서 별도 주소로 안내

⇒ /user_pk/password/


비밀번호 변경 페이지 확인



### 비밀번호 변경 로직 완성



---

## 세션 무효화 방지

<aside>
💡

암호 변경 시 세션 무효화

- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어버려 로그인 사태가 유지되지 못하고 로그아웃 처리됨
- 비밀번호가 변경되면서 기존 세션과의 회원인증 정보가 일치하지 않기 때문
</aside>

### update_session_auth_hash(request, user)

암호 변경 시 세션 무효화를 막아주는 함수

⇒ 암호가 변경되면 새로운 password의 Session Data로 기존 session을 자동으로 갱신

### update_session_auth_hash 적용

- 비밀번호 변경 후 로그아웃이 되지 않음



## 인증된 사용자에 대한 접근 제한

<aside>
💡

로그인 사용자에 대해 접근을 제한하는 2가지 방법

1. is_authenticated 속성
2. login_required 데코레이터
</aside>

### is_authenticated 속성

사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성

⇒ 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성

⇒ 비인증 사용자에 대해서는 항상 False

### is_authenticated 적용하기

로그인과 비로그인 상태에서 화면에 출력되는 링크를 다르게 설정하기



인증된 사용자라면 로그인/회원가입 로직을 수행할 수 없도록 하기



### login_required 데코레이터

로그인 필수!!

인증된 사용자에 대해서만 view함수를 실행시키는 데코레이터

→ 비인증 사용자의 경우 /accounts/login/주소로 redirect 시킴

### login_required 적용하기

인증된 사용자만 게시글을 작성/ 수정/ 삭제 할 수 있도록 수정



인증된 사용자만 로그아웃/ 탈퇴/수정/비밀번호 변경 할 수 있도록 수정


---

# 참고

## is_authenticated 코드

### is_authenticated 속성 코드

메서드가 아닌 속성 값임을 주의


## 회원가입 후 자동 로그인

### 회원가입 후 로그인까지 이어서 진행하려면?

회원 가입 성공한 user객체를 활용해 login 진행



## 회원 탈퇴 개선

### 탈퇴와 함께 기존 사용자의 Session Data 삭제 방법

- 사용자 객체 삭제 이후 로그아웃 함수 호출
- 단 탈퇴 후 로그아웃의 순서가 바뀌면 안됨
- 먼저 로그아웃이 진행되면 해당 요청 객체정보가 없어지기 때문에 탈퇴에 필요한 유저 정보 또한 없어지기 때문



## PasswordChangeForm 인자 순서

### PasswordChangeForm의 인자 순서

- passwordchangeform이 다른 form과 달리 user객체를 첫번째 인자로 받는이유
- 부모 클래스인 SetPasswordForm의 생성자 함수 구성을 따르기 때문