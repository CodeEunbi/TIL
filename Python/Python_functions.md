# 함수(Functions)

특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

### 함수 사용하는 이유

- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
- **재사용성**이 높아지고 코드의 **가독성과 유지보수성** 향상

→ 계속 계산할 필요없이 함수 사용

### 함수 호출(function call)

함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드블록을 실행하는 것

```python
function_name(arguments)
```

## 함수 구조

함수의 input → function body(들여쓰기로 영역을 나눔), Docstring(document string, 주석) →  output(return)

### 함수 정의와 호출

**정의**

- 함수 정의는 def 키워드로 시작
- def 키워드 이후 함수 이름 작성
- 괄호 안에 매개변수를 정의할 수 있음
- 매개변수(parameter)는 함수에 전달되는 값을 나타냄

**함수 body**

- 콜론(:)다음에 들여쓰기 된 코드 블록
- 함수가 실행될 때 수행되는 코드를 정의

**Docstring**

- 함수 body 앞에 선택적으로 작성 가능한 함수 설명서

**함수의 반환값**

- 함수는 필요한 경우 결과를 반환(그러지 않는 경우도 있음)
- return 키워드 이후에 반환할 값을 명시
- return 문은 함수의 실행을 종료하고 결과를 호출 부분으로 반환
- 함수 내에서 return문이 없다면 None이 반환 → return None(강제)
- 반환값이 없는 함수 : print()(뒤에서 출력만 할 뿐)

```python
return_value = print(1)
print(return_value) #None
```

```python
def my_func():
		print('hello')
		
result = my_func()
print(result) #None
```

**함수 호출**

- 함수를 사용하기 위해서는 호출해야함
- 함수의 이름과 소괄호를 사용
- 필요한 경우 인자(argument)를 전달
- 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개 변수에 대입
- 이미 전에 사용한 적이 있으면 print를 하지 않는한 전에 사용했던 걸로 출력됨

## 함수와 반환값

### print()함수는 반환값이 없음

- print()함수는 화면에 값을 출력할뿐 반환값이 없음
- 파이썬에서 반환 값이 없는 함수는 기본적으로 None을 반환한다고 간주

     → 출력을 담당하는 함수는 결과를 반환(return)하지 않으므로 내부적으로 아무값도 반환하지 않는         함수와 마찬가지로 None이 나옴

---

# 매개변수와 인자

## 매개변수(parameter)

**함수를 정의**할 때, 함수가 받을 값을 나타내는 변수

def로 정의

## 인자(argument)

**함수를 호출**할 때, 실제로 전달되는 값

a와 b의 값이 인자

```python
def add_numbers(x, y): #x,y매개변수
		result = x+y
		return result
		
a=2
b=3
sum_result = add_numbers(a,b)  #a,b는 인자(argument)
print(sum_result)
```

## 인자 종류

### Positional Arguments(위치 인자)

- 함수 호출 시 인자의 위치에 따라 전달되는 인자

    → 위치 인자는 함수 호출 시 반드시 값을 전달해야 함

```python
def greet(name, age):
		print(f'안녕하세요, {name}님! {age}살이시군요.')
		
greet('Alice', 25) #안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice') #안녕하세요, 25님! Alice살이시군요.
greet('Alice') #TypeError: greet() missing 1 required positional argument: 'age'
```

- 위치 인자 개수가 맞지 않는 경우 타입에러

### Default Arguments Values(기본 인자 값)

- 함수 정의에서 매개변수에 기본값을 할당
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당
- ex) def greet(name, age=30) → 이름만 넣어도 age가 기본값 30으로 나옴

```python
def greet(name, age=30):
		print(f'안녕하세요, {name}님! {age}살이시군요.')
		
greet('Bob') #안녕하세요. Bob님! 30살이시군요.
greet('Charlie', 40) #안녕하세요, Charlie 님! 40살이시군요.
```

### Keyword Arguments(키워드 인자)

- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당
- 인자의 순서는 중요하지 않으며 인자의 이름을 명시하여 전달
- 단 호출 시 키워드 인자는 위치 인자 뒤에 위치

```python
def greet(name, age):
	  print(f'안녕하세요, {name}님! {age}살이군요.')
	
greet(name='Dave', age=35) #안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave') #안녕하세요, Dave님! 35살이시군요.

greet(age=35, 'Dave') #positional argument follows keyword argument
```

### Arbitrary Argument Lists(임의의 인자 목록)

- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 ‘*’를 붙여 사용
- 여러 개의 인자를 tuple로 처리

```python
def calculate_sum(*args):
		print(args)  #(1, 100, 5000, 30)
		print(type(args)) #<class 'tuple'>
		
calculate_sum(1, 100, 5000, 30)
```

### Arbitrary Keyword Arguments Lists(임의의 키워드 인자 목록)

- 정해지지 않은 개수의 키워드 인자를 처리하는 인
- 함수 정의 시 매개 변수 앞에 ‘**’를 붙여 사용
- 여러 개의 인자를 dictionary로 묶어 처리

```python
def print_info(**kwargs):
		print(kwargs)
		
print_info(name='Eve', age=30) #{'name':'Eve', 'age':30}
```

### 함수 인자 권장 작성 순서

- 위치 → 기본 → 가변 → 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄임
- 단 모든 상황에서 적용되는 절대적인 규칙은 아니며 상황에 따라 유연하게 조정

```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
		print('pos1:', pos1)
		print('pos2:', pos2)
		print('default_arg:', default_arg)
		print('args:', args)
		print('kwargs:', kwargs)
		
		func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
		
		'''
		pos1 : 1
		pos2 : 2
		default_arg : 3
		args: (4, 5, 6) #튜플로 나옴
		kwargs : {'key1':'value1', 'key2':'value2'} #dict 으로 나옴
		'''
```

---

# 재귀함수

함수 내부에서 **자기 자신을 호출**하는 함수

ex) n!(팩토리얼)

- factorial함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
- 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
- 재귀 호출의 결과를 이용하여 문제를 작은 다누이의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출
- 자기 자신을 호출(특정한 종류 조건에 따라, 그렇지 않으면 무한정으로 호출되어 코드가 꺼짐)
- 작은 단위부터 쪼개서 풀 때 유용하게 사용 가능
- 종료 지점 : base case → base case로 수렴

```python
def facotrial(n):
		#종료 조건 : n이 0이면 1을 반환
		if n==0:
			return 1
		else:
			#재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과를 반환
			return n*factorial(n-1)
			
	#팩토리얼 계산
	print(factorial(5)) #120
```

### 재귀 함수 특징

- 특정 알고리즘 식을 표현할 때 변수 사용이 줄어들고 코드의 가독성이 높아짐
- 1개 이상의 base case가 존재하고 수렴하도록 작성

---

# 내장함수(Built-in-function)

파이썬이 기본적으로 제공하는 함수(별도의 import없이 바로 사용 가능)

외장함수는 없음

ex) print(), len(),max(), min(),sum(), sorted()

# map & zip

## map(function, iterable)

**순회 가능한 데이터구조**(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

→ 반복문

### map활용()

```python
numbers1 = input().split()
print(numbers1) # ['1', '2', '3'] 문자열

numbers2 = list(map(int, input().split()))
print(numbers2) # [1, 2, 3] list 형변환
```

### zip(*iterables)

임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['Jane', 'Ashley']
boys = ['Peter', 'Jay']
pair = zip(girls, boys)

print(pair) #zip object at 0x000001C76DE58700
print(list(pair)) #[('Jane', 'Peter'),('Ashley', 'Jay')]
```

### zip() 활용

- 여러 개의 리스트를 동시 조회

```python
kr_scores = [10 ,20, 30 ,50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scors, math_scores, en_scores) :
		print(student_scores)

#(10, 20, 40) (20, 40, 20) (30, 50, 30)(50, 70, 50)
```

- 2차원 리스트의 같은 컬럼(열)요소를 동시에 조회

```python
scores = [
		[10, 20, 30],    #(10, 40, 20)
		[40, 50, 39],    #(20, 50, 40)    
		[20, 40, 50],    #(30, 39, 50) 
]

for score in zip(*scores):
		print(score)
```

---

# 함수와 Scope

## python의 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그외의 공간인 global scope로 구분

## 범위와 변수 관계

### scope

- global scope : 코드 어디에서든 참조할 수 있는 공간
- local scope : 함수가 만든 scope(함수 내부에서만 참조 가능)

### variable

- global variable : global scope에 정의된 변수
- local variable : local scope에 정의된 변수

### Scope 예시

- num은 local scope 에 존재하기 때문에 global scope에서 사용할 수 없음

     → 변수의 수명 주기와 관련

```python
def func():
		num = 20
		print('local', num)  #local 20
		
func()

print('global', num) #NameError: name 'num'is not defined
```

### 변수 수명주기(lifecycle)

- 변수의 수명주기는 변수가 선언되는 위치와 scope에 따라 결정
1. built-in scope : 파이썬이 실행된 이후부터 영원히 유지
2. global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙(Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간에 저장
- LEGB Rule이라고 부름
1. Local scope : 지역범위(현재 작업중인 범위)
2. Enclosed scope : 지역 범위 한단계 위 범위
3. Global scope : 최상단에 위치한 범위
4. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)

- 함수 내에서는 바깥 scope 변수에 접근이 가능하지만 수정은 할 수 없음!
- 예를 들어, sum이라는 이름을 global scope에서 사용되게 되면서 기존에 built-in에 있던 sum을 사용하지 못함
- sum을 참조 시 룰에 따라 global에서 먼저 찾음
- sum변수 객체 삭제 → del sum

```python
print(sum) #<built-in function sum>
print(sum(range(3)))   #3

sum = 5

print(sum)  #5
print(sum(range(3)))   #TypeError: 'int' object is not callable
```

## Global 키워드

- 변수의 스코프를 전역범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

```python
num = 0  #전역변수

def increment():
		global num #num을 전역변수로 선언
		num +=1
		
print(num)  #0
increment()   
print(num)  #1
```

### 주의 사항

- global 키워드 선언 전에 참조 불가

```python
num = 0

def increment():
		#SyntaxError : name'num'is used prior to global declaration
		print(num)
		global num
		num +=1
```

- 매개 변수에는 global키워드 사용 불가

```python
num = 0

def increment(num):
		#'num' is assigned before global declaration
		global num
		num +=1
```

---

# 함수 스타일 가이드

## 함수 이름 작성

### 기본

- 소문자와 언더스코어(_)사용
- 동사로 시작하여 함수의 동작 설명
- 약어 사용 지양

### 함수 이름 구성 요소

- 동사 + 명사 : save_user
- 동사 + 형용사 + 명사 : calculate_total_price()
- get/set 접두사 : get_username(), set_username()

## 단일 책임 원칙(Single Responsibility Principle)

모든 객체는 하나의 명확한 목적과 책임만을 가져야함

### 잘못된 경우&올바른 경우

- 여러 책임이 섞인 함수

  → 하나가 잘못되면 모든 걸 바꾸어야 함

  → 책임을 분리한 함수로 만들기

### 함수 설계 원칙

1. 명확한 목적
- 함수는 한 가지 작업만 수행
- 함수 이름으로 목적을 명확히 표현

2. 책임분리
- 데이터 검증, 처리, 저장 등을 별도 함수로 분리
- 각 함수는 독립적으로 동작 가능하도록 설계

3. 유지보수성
- 작은 단위의 함수로 나누어 관리
- 코드 수정 시 영향 범위를 최소화

---

# Packing & Unpacking

## Packing

여러 개의 값을 하나의 변수에 묶어서 담는 것

- 한 변수에 콤마로 구분된 값을 넣으면 자동으로 튜플 처리

### ‘*’을 활용한 패킹(변수 할당 )

- ‘*변수명’을 사용하면 ‘나머지 모든 값’을 리스트로 묶어서 받을 수 있음

### ‘*’을 활용한 패킹(함수 매개변수 작성 시)

- ‘*매개변수’를 사용하면 호출 시 여러 개의 인자를 한 변수에 묶어서 받을 수 있음
- 이 때 함수 내부에서 해당 매겨변수는 튜플 형태로 취급

### print() 패킹

- 임의의 가변인자를 작성 → 인자 개수에 상관없이 튜플 하나로 패킹 되어서 내부에서 처리

## Unpacking

패킹된 변수를 풀어서 개별 변수나 함수 인자로 전달

- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당

### ‘*’을 활용한 언패킹(함수 인자 전달)

- 시퀀스(리스트, 튜플)를 함수에 전달할 때 각 요소를 풀어서 개별인자로 넘겨 줄 수 있음

### ‘**’을 활용한 언패킹(딕셔너리 → 함수 키워드 인자)

- 딕셔너리의 키-값 쌍을 분리해, 함수의 키워드 인자로 전달할 때 사용

### *, ** 패킹 / 언패킹 연산자 정리

- ‘*’

        - 패킹 연산자로 사용될 때, 여러개의 인자를 하나의 리스트나 튜플로 묶음

        - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인      

           자로 전달

- ‘**’

         - 언패킹 연산자로 사용될때, 딕셔너리의 키-값 쌍을 개별 키워드 인자로 전달

---

# 람다 표현식(Lambda expressions)

익명 함수를 만드는데 사용되는 표현식 → 한 줄로 간단한 함수를 정의

## 표현식 구조(lambda 매개변수 : 표현식)

- 매개변수 : 함수에 전달되고 여러개의 경우 쉼표로 구분
- 결과값을 반환하는 표현식
- 일회성이라고 생각하면 됨

### 예시

- 간단한 연산이나 함수를 한 줄로 표현
- 함수를 매개변수로 전달하는 경우
- map 함수와 사용 가능