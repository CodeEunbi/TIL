# 함수와 Scope

## python의 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그외의 공간인 global scope로 구분

## 범위와 변수 관계

### scope

- global scope(전역변수) : 코드 어디에서든 참조할 수 있는 공간
- local scope(지역변수) : 함수가 만든 scope(함수 내부에서만 참조 가능)

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
- 전역변수라고 지정
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

## 메모리 주소
- 이미 주소가 있는 메모리에 이름만 붙임