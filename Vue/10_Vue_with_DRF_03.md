### CONTENT

# 인증 with Vue

<aside>
👉

시작 하기 전

1. DB 초기화
    - db.sqlite3  삭제
2. Migration 과정 재진행
3. 관리자 계정 생성 후 , 게시글 1개 이상 작성
    - 기존 fixtures 데이터는 user 정보가 없으므로 사용 불가능
    - 정상 작동하던 게시글 전체 조회가 작동하지 않음
        - 401 status code  확인
        
        → 게시글 조회 요청 시 인증에 필요한 수단(token)을 보내지 않고 있으므로 게시글 조회가 불가능해진 것
        
</aside>

## 회원가입

### 회원가입 로직 구현

- SignUpView route 관련 코드 주석 해제

```jsx
import SignUpView from '@/views/SignUpView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
  {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
  ]
```

- App 컴포넌트에 SignUpView 컴포넌트로 이동하는 RouterLink 작성

```jsx
<!-- App.vue -->

<template>
  <header>
    <nav>
      <RouterLink :to="{ name:'ArticleView' }">Articles</RouterLink> | 
      <RouterLink :to="{ name:'SignUpView' }">SignUpPage</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>
```

- 회원가입 form 작성

```jsx
<!-- views/SignUpView.vue -->

<template>
  <div>
    <h1>SignUpPage</h1>
    <form>
	    <label for="username">username : </label>
	    <input type="text" id=username" v-model.trim="username"><br>
	    
	    <label for="password1">password : </label>
	    <input type="text" id=password" v-model.trim="password1"><br>
	    
	    <label for="password2">password confirmation: </label>
	    <input type="text" id=password" v-model.trim="password2"><br>
	    
	    <input type="submit" value="SignUp"
    </form>
  </div>
</template>
```

- 사용자 입력 데이터와 바인딩 될 반응형 변수 작성

```jsx
<script setup>
  import { ref } from 'vue'
  
 const username = ref(null)
 const password1 = ref(null)
 const password2 = ref(null) 
</script>
```

- SignUpView 컴포넌트 출력 확인

- 회원가입 요청을 보내기 위한 signUp 함수가 해야할 일
    - 사용자 입력 데이터를 받아 서버로 회원가입 요청을 보냄

```jsx
export const useAccountStore = defineStore('account', () => {
  const signUp = function () {
	  ...
  }
  return { signUp }
}, { persist: true })
```

- 컴포넌트에 사용자 입력 데이터를 저장 후 store의 signUp 함수를 호출하는 함수 작성

```jsx
import { useAccoutStore } from '@/stores/account'

const accountStore = useAccountStore()

const signUp = function () {
	const payload = {
		username: username.value,
		password1: password1.value,
		password2: password2.value
	}
	accountStore.signUp(payload)
}
```

```jsx
<form @submit.prevent="signUp>
...
</form>
```

- 실제로 회원가입 요청을 보내는 store의 signUp 함수 작성

```jsx
const signUp = function (payload) {
		const username: payload.username,
		const password1: payload.password1,
		const password2: payload.password2
	}
	
	axios({
		method: 'POST',
		url: `${API_URL}/accounts/signUP/`,
		data: {
			username, password1, password2
		}
	})
	.then(res => {
			console,log('회원 가입이 완료되었습니다.')
	})
	.catch(err => console.log(err))
}
```

- 회원가입 테스트
- Django DB 확인

## 로그인

### 로그인 로직 구현

- LogInView route 관련 코드 주석 해제

```jsx
import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
	  {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
   ]
```

- App 컴포넌트에 LogInView 컴포넌트로 이동하는 RouterLink 작성

```jsx
<template>
  <header>
    <nav>
      <RouterLink :to="{ name:'ArticleView' }">Articles</RouterLink> | 
      <RouterLink :to="{ name:'SignUpView' }">SignUp</RouterLink> |
      <RouterLink :to="{ name:'LogInView' }">LogIn</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>
```

- 로그인 form 작성

```jsx
<template>
  <div>
    <form @submit.prevent="onlogIn">
	    <label for="username">username : </label>
	    <input type="text" id="username" v-model="username"><br>
	    
	    <label for="password">password : </label>
	    <input type="password" id="password" v-model="password"><br>
	    
	  
	    <input type="submit" value="logIn">
    </form>
  </div>
</template>
```

- 사용자 입력 데이터와 바인딩 될 반응형 변수 작성

```jsx
<script setup>
  import { ref } from 'vue'
  
  const username = ref(null)
  const password = ref(null)
 </script>
```

- LogInView 컴포넌트 출력 확인

- 로그인 요청을 보내기 위한 logIn 함수가 해야할 일
    - 사용자 입력 데이터를 받아 서버로 로그인 요청 및 응답 받은 토큰 저장

```jsx
export const useAccountStore = defineStore('account', () => {
	const logIn = function () {
		...
	}
	return { signUp, logIn }
}, { persist: true })
```

- 컴포넌트에 사용자 입력 데이터를 저장 후 store의 logIn 함수를 호출하는 함수 작성

```jsx
import { useAccountStore } from '@/stores/accounts.js'

const accountStore = useAccountStore()

const logIn = function () {
	const payload = {
		username: username.value,
		password: password.value	
	}
	accountStore.logIn(payload)
}

<form @submit.prevent="logIn">
...
</form>
```

- 실제 로그인 요청을 보내는 store의 logIn 함수 작성

```jsx
// stores/accounts.js

const logIn = function ({username, password}) {
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/login/`,
      data:{
        username, password
      }
    })
      .then(res => {
        // console.log(res)
        token.value = res.data.key
      })
      .catch(err => console.log(err))
  }
```

- 로그인 테스트
- 응답 객체 안에 Django가 발급한 Token이 함께 온 것을 확인

## 요청과 토큰

> Token을 store에 저장하여 인증이 필요한 요청마다 함께 보낸다

### 토큰 저장 로직 구현

- 반응형 변수 token 선언 및 토큰 저장

```jsx
export const useAccountStore = defineStore('account', () => {
	const token = ref(null)
	
	const logIn = function(payload) {
		...
			.then(res => {
				token.value = res.data.key
			})
			.catch(err => console.log(err))
	}
	return { signUp, logIn, token }
}, { persist: true })
```

- 다시 로그인 요청 후 store에 저장된 토큰 확인


### 토큰이 필요한 요청

1. 게시글 전체 목록 조회 시
2. 게시글 작성 시

### 게시글 전체 목록 조회  with  token

- 게시글 전체 목록 조회 요청 함수 getArticles에 token 추가

```jsx
import { useAccountStore } from './accounts'

export const useArticleStore = defineStore('article', () => {
  const accountStore = useAccountStore()
  
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        'Authorization': `Token ${accountStore.token}`
      }
    })
```

- 401 상태 코드가 사라지고 게시글이 정상적으로 출력되는 것을 확인


### 게시글 생성 with token

- 게시글 생성 요청 함수 createArticle에 token 추가

```jsx
import { useAccountStore } from '@/stores/accounts'

const accountStore = useAccountStore()

const createArticle = function () {
	axios({
		method: 'POST',
		url: `${store.API_URL}/api/v1/articles/`,
		data: {
			...
		},
		headers: {
			'Authorization': `Token ${accountStore.token}`
		}
	})
}
```

- 게시글 작성 확인


## 인증 여부 확인

### 사용자의 인증(로그인) 여부에 따른 추가 기능 구현

1. 인증 되지 않은 사용자
    - 메인 페이지 접근 제한
2. 인증된 사용자
    - 회원가입 및 로그인 페이지에 접근 제한

### 인증 상태 여부를 나타낼 속성 값 지정

- token 소유 여부에 따라 로그인 상태를 나타낼 isLogin 변수 작성
- computed를 활용해 token 값이 변할 때만 상태를 계산하도록 함

```jsx
export const useAccountStore = defineStore('account', () => {
	const isLogin = computed(() => {
		return token.value ? true : false	
	})
	return { signUp, logIn, token, isLogin }
}, { persist: true }
```

### 1. 인증되지 않은 사용자는 메인 페이지 접근 제한

- 전역 네비게이션 가드 beforeEach를 활용해 다른 주소에서 메인 페이지로 이동 시 인증되지 않은 사용자라면 로그인 페이지로 이동시키기

```jsx
// router/index.js

import { useAccountStore } from '@/stores/accounts'

const router = createRouter({...})

router.beforeEach((to, from) => {
	const accountStore = useAccountStore()
	if (to.name === 'ArticleView' && !accountStore.isLogin) {
		window.alert('로그인이 필요합니다.')
		return { name: 'LogInView'}
	}
})
```

- 브라우저 local storage에서 token을 삭제 후 메인 페이지 접속 시도


### 2. 인증된 사용자는 회원가입과 로그인 페이지에 접근 제한

- 다른 주소에서 회원 가입 또는 로그인 페이지로 이동 시 이미 인증된 사용자라면 메인 페이지로 이동시키기

```jsx
// router/index.js

router.beforeEach((to, from) => {
  const accountStore = useAccountStore()
  if (to.name === 'ArticleView' && !accountStore.isLogin) {
	  window.alert('로그인이 필요합니다.')
    return { name: 'LoginView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (accountStore.isLogin)) {
	  window.alert('이미 로그인 되어있습니다.')
	  return { name: 'ArticleView' }
	  }
})
```

- 로그인 후 회원가입, 로그인 페이지 접속 시도

## User Customize

### 시작하기 전에

1. DB 초기화
    - db.sqlite3 삭제

# User Customize

### 1. User Model에 필드 추가

- 사용자의 나이 정보를 저장할 PositiveIntegerField 추가

```python
# accounts/model.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
```

- makemigrations, migrate 진행
- age 필드 추가 확인

### 2. Vue 회원 가입 기능 수정

- age 입력을 위한 input과 변수 및 payload data 수정

```jsx
<label for="age">age: </label>
<input type="number" id="age" v-model="age"><br>

<script setup>
const age = ref(0)
const signUp = function () {
	const payload = {
		...
		age: age.value
	}
}
</script>
```

- signUp 함수에 age 정보 추가

```jsx
 const signUp = function ({username, age, password1, password2}) {
  // const logIn = function ({username, password})
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    // const age = payload.age
    // console.log(payload)
    axios({
      method: 'POST',
      url:`${ACCOUNT_API_URL}/signup/`,
      data: {
        username, age, password1, password2
        // username: payload.username,
        // password1: payload.password1,
        // password2: payload.password2
        // age: payload.age
      }
    })
```

- 회원가입 요청 후, 응답 결과 확인

### 회원가입 성공?

- 요청 보낸 유저 명으로 잘 생성되었으나, age 정보는 누락되었음

### RegisterSerializer

- dj-rest-auth의 RegisterSerializer의 field 정보 확인
- username, email, password1, password2 필드만 정의 되어있음


# Customize RegisterSerializer

### 회원 가입 기능 수정

- Customize RegisterSerializer에 정의(RegisterSerializer 상속)
- age 필드 추가(필요하다면, first_name 등 기본 제공 필드 추가 가능)

```python
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=True)
```

- 유효성 검사를 위한 get_cleaned_data 함수 구조 확인
- 입력 받은 데이터의 유효성 검사 결과를 객체 형태로 반환 해야 함
- 새롭게 추가한 필드도 추가하여 동일하게 동작할 수 있도록 수정
- super()를 사용하여, 기존 필드에 대한 유효성 검사 실행 후, 추가 필드에 대해 동일한 작업을 진행한 결과를 반영하여 변환

```python
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['age'] = self.validated_data.get('age', '')
        return data 
```

- save 함수도 유효성 검사 함수와 같은 작업을 진행

```python
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['age'] = self.validated_data.get('age', '')
        return data 

    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get('age', '')
        user.save()
        return user
```

- dj-rest-auth가 CustomRegisterSerializer을 사용하도록 설정
- REST_AUTH_REGISTER_SERIALIZERS 주석 해제

```python
# settings.py

REST_AUTH = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}
```

### 회원 가입 요청 및 결과 확인

- 이전과 달리 정상적으로 age정보가 기입된 것을 확인

---

# 참고

## 로그아웃

### 로그아웃 구현

- logOut 작성

```jsx
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
	const router = useRouter()
	
	const logOut = function() {
		axios({
			method: 'POST',
			url: `${API_KEY}/accounts/logout/`
		})
		.then((res) => {
			token.value = null
			router.push({ name: 'ArticleView'})
		})
		.catch((err) => console.log(err))
	}
	return { signUp, logIn, tokjen, isLogin, logOut}
```

- App 컴포넌트에 로그아웃 form 요소 작성

```jsx
<form @submit.prevent="logOut">
	<input type="submit" value="Logout">
</form>

import { useAccountStore } from '@/stores/accounts'

const accountStore = useAccountStore()

const logOut = function () {
	accountStore.logOut()
}
```

## 기타 구현 능력

### 자연스러운 흐름을 위한 기타 기능 구현

1. 로그인 성공 후 자동으로 메인 페이지로 이동하기
2. 회원 가입 성공 후 자동으로 로그인까지 진행하기

### 1. 로그인 성공 후 자동으로 메인 페이지로 이동하기

```jsx
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
	const router = useRouter()
	
	const logIn = function(payload) {
		...
			.then(res => {
				token.value = res.data.key
				router.push({ name: 'ArticleView' })
			})
		} .catch(err => console.log(err))
}
```

### 2. 회원가입 성공 후 자동으로 로그인까지 진행하기

```jsx
const signUp = function (payload) {
	...
		.then(res => {
			const password = password1
			logIn({ username, password })
		})
		.catch(err => console.log(err))
}
```

## Django Signals

- “이벤트 알림 시스템”
- 애플리케이션 내에서 특정 이벤트가 발생할 때, 다른 부분에게 신호를 보내어 이벤트가 발생했음을 알릴 수 있음
- 주로 모델의 데이터 변경 또는 저장, 삭제와 같은 작업에 반응하여 추가적인 로직을 실행하고자 할 때 사용
    - 사용자가 새로운 게시글을 작성할 때마다 특정 작업을 수행하려는 경우(ex. 이메일 알림 보내기)

## 환경 변수(enviornment variable)

애플리케이션의 설정이나 동작을 제어하기 위해 사용되는 변수

### 환경 변수의 목적

- 개발, 테스트 및 프로덕션 환경에서 다르게 설정되어야하는 설정 값이나 민감한 정보(ex. API KEY)를 포함
- 환경 변수를 사용하여 애플리케이션의 설정을 관리하면, 다양한 환경에서 일관된 동작을 유지하면서 필요에 따라 변수를 쉽게 변경할 수 있음
- 보안적인 이슈를 피하고, 애플리케이션을 다양한 환경에 대응하기 쉽게 만들어줌

### Vite에서 환경변수를 사용하는 법

- env.local 파일 생성 및 API 변수 작성
- 주의 사항
    - 변수명은 반드시 VITE_접두어를 작성해야함
    - 변수명과 값 사이에 공백이 없어야 함
    

```jsx
const API_KEY = import.meta.env.VITE_TMDB_API_EKY
```

## Vue 참고 자료

- Awesome Vue.js
    - Vue와 관련하여 선별된 유용한 자료를 아카이빙 및 관리하는 프로젝트
    - https://github.com/vue.js/awesome-vue
    - https://awesome-vue.js.org/
    
- Vuetify
    - Vue를 위한 UI라이브러리(ex. ‘Bootstrap’)
    - https://vuetify.js.com/en/

## 설치한 라이브러리 정리

```jsx
$ npm i pinia-plugin-persistedstate
$ npm i axios

$ pip install djangorestframework
$ pip install django-cors-headers
$ pip install dj-rest-auth
$ pip install 'dj-rest-auth[with-social]'
```