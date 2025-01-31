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
