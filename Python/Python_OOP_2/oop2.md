# OOP 2 & Exception(25.02.04)
# 상속(inheritance)

한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것

### 상속이 필요한 이유

1. 코드 재사용
- 상속을 통해 기존 클래스의 속성과 메서드를 재사용
- 기존 클래스를 수정하지 않고도 추가적인 기능을 확장할 수 있음

1. 계층 구조
- 상속을 통해 클래스들 간의 계층 구조를 형성
- 부모 클래스와 자식 클래스 간의 관계를 표현하고 더 구체적인 클래스를 만들 수 있음

1. 유지 보수 용이성
- 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이
- 코드의 일관성을 유지하고 수정이 필요한 범위를 최소화

```python
class Animal:
    def eat(self):
        print('먹는 중')

class Dog(Animal): # animal클래스를 인자로 받음
    def bark(self):
        print('멍멍')

#인스턴스 생성
my_dog = Dog()

#인스턴스 메서드 호출
my_dog.bark()  #멍멍

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat()
```

## 클래스 상속

### 상속 없이 구현하는 경우

- 정보를 별도로 표현하기 어려움
- 클래스를 분리 → 메서드가 중복될 수 있음
- 부모 클래스에 다 만들고 그 뒤에 재선언할 필요 없이

## 메서드 오버라이딩(Method Overriding)

부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의

```python
class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self):
        print('Dog가 먹는 중')

my_dog = Dog()

my_dog.eat()  # Dog가 먹는 중, 본인 걸 먼저 호출
```

[오버로딩(overloading)]

파이썬은 하나의 메서드만 인식하며, 인자의 형태가 다르다는 이유로 메서드를 여러개 구분하여 불러주지 않음.

## 다중 상속

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소를 활용 가능
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정


다이아몬드 문제
B, C → A / D → B, C에게 상속될 때 생기는 문제

```python
# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Mom, Dad):    #기준이 됨
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY, firstchild에서 Dad를 먼저 상속받음, 
                   #순서가 바뀌면 상속받는 순서가 바뀌기때문에 바뀜
```

### 해결책

- MRO(Method Resolution Order) 알고리즘 사용하여 클래스 목록 생성
- 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, 왼쪽에서 오른쪽으로, 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음
- D속성이 발견되지 않으면 B에서 찾고 C에서 찾고 이런식으로 진행

```python
class D(B, C):
			pass
```

### MRO(Method Resolution Order)

파이썬이 메서드를 찾는 순서에 대한 규칙, 메서드 결정 순서

## Super() 메서드

부모 클래스(상위 클래스)의 메서드를 호출하기 위해 사용하는 내장함수

### Super()기능

다중 상속 상황에서 특히 유용, MRO를 따르기 때문에 여러 부모 클래스를 가진 자식 클래스에서 다음에 호출해야할 부모 메서드를 순서대로 호출할 수 있게 함

### 사용 사례

1. 단일 상속 구조
- 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로, 코드를 더 유지 관리하기 쉽게 만들 수 있음
- 클래스 이름이 변경 되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 더 적게 필요

```python
# 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # super()를 통해 Person의 __init__ 메서드 호출
        # self는 이미 있어서 호출 안함
        super().__init__(name, age, number, email) #호출 가능, 부모 클래스의 이름이 바뀔 수도 있기 때문에 유용
        # Person.__init__(name, age, number, email) #호출 가능
        self.student_id = student_id

# super를 사용하지 않았을 때
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id

```

1. 다중 상속 구조
- MRO를 따른 메서드 호출
- 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지

(object = 클래스 위 최상위 클래스)

```python
# 다중 상속
class ParentA:
    def __init__(self):
        super().__init__()   # Child -> a -> b   # B
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()
"""
Value from ParentA: ParentA
Value from Child: Child
"""

print(child.value_c)  # Child
print(child.value_a)  # ParentA
print(
    child.value_b
)  # AttributeError: 'Child' object has no attribute 'value_b'

"""
<ParentA에 super().__init__()를 추가하면?>
그 다음으로 ParentB의 __init__가 실행되어 value_b도 초기화할 수 있음
그러면 print(child.value_b)는 ParentB를 출력하게 됨

print(child.value_b)  # ParentB
"""

"""
<Child 클래스의 MRO>
Child -> ParentA -> ParentB

super()는 단순히 “직계 부모 클래스를 가리킨다”가 아니라, 
MRO 순서를 기반으로 “현재 클래스의 다음 순서” 클래스(또는 메서드)를 가리킴

따라서 ParentA에서 super()를 부르면 MRO상 다음 클래스인 ParentB.__init__()가 호출됨
"""

"""
1.1 Child 클래스의 인스턴스를 생성할 때 일어나는 일
    1.	child = Child() 호출 시, Child.__init__()가 실행
    2.	Child.__init__() 내부에서 super().__init__()를 호출
        - 여기서 Child의 super()는 MRO에 의해 ParentA의 __init__()를 가리킴
    3.	ParentA.__init__()로 진입

1.2. ParentA.__init__() 내부
	1.	ParentA.__init__()에는 다시 super().__init__()가 있음
	2.	ParentA를 기준으로 MRO에서 “다음 클래스”는 ParentB, 따라서 ParentA의 super().__init__()는 ParentB.__init__() 호출
    3.	ParentB.__init__()가 실행되면서 self.value_b = 'ParentB'가 설정됨
	4.	ParentB.__init__()가 종료된 후, 다시 ParentA.__init__()로 돌아와 self.value_a = 'ParentA'가 설정됨
	5.	ParentA.__init__() 종료 후, 다시 Child.__init__()로 돌아감
	6.	마지막으로 Child.__init__() 내에서 self.value_c = 'Child'가 설정되고 종료

1.3 결과적으로 child 인스턴스는 value_a, value_b, value_c 세 속성을 모두 갖게 됨
	- child.value_a → 'ParentA'
	- child.value_b → 'ParentB' 
	- child.value_c → 'Child'
"""

```

**Super()의 이점**

- 다중 상속 상황에서 super()는 MRO순서에 따라 결정하기 때문에 명시적으로 특정 부모 클래스를 가리키지 않고도 올바른 순서로 초기화나 메서드 호출 가능

→ 복잡한 상속 구조에서도 코드를 유연하고 깔끔하게 유지할 수 있음

**Super()정리**

- super()를 사용할 때는 MRO를 잘 이해하고 있어야함
- ClassName.__mro__또는 ClassName.mro()를 확인해 MRO순서를 파악한 뒤 적절히 활용하는 연습을 하면 보다 복잡한 상속 구조에서도 코드를 잘 관리할 수 있음

```python
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)
```

MRO 필요 이유

- 왼쪽에서 오른쪽으로 가는 순서롤 보존,  각 부모를 한번만 호출, 우선순위에 영향을 주지 않고 단조적인 구조 형성
- 프로그래밍 언어의 신뢰성과 확장성 있는 클래스 설계
- 메서드 호출 순서가 예측 가능, 코드의 재사용성과 유지보수성이 향상

---

# 에러와 예외

## 디버깅

## 버그(bug)

소프트웨어에서 발생하는 오류 또는 결함, 프로그램의 예상된 동작과 실제 동작 사이의 불일치

### 버그의 기원

- Mark2라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작한 것을 기록
- 이전부터 용어는 사용되어왔지만 위의 사건을 계기로 컴퓨터 시스템에서 발생하는 오류 또는 결함을 지칭하는 용어로 널리 사용

### Debugging

소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정

프로그램의 오작동 원인을 식별하여 수정하여 작업

### 디버깅 방법

1. print 함수 활용 : 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
2. 개발 환경(text editor, IDE)등에서 제공하는 기능 활용 : breakpoint, 변수 조회 등
3. Python tutor 활용(단순 파이썬 코드인 경우)
4. 뇌 컴파일, 눈 디버깅 등

## 에러(Error)

프로그램 실행 중에 발생하는 예외 상황

### 에러 유형

문법 에러(Syntax Error) : 프로그램의 구문이 올바르지 않은 경우 발생(오타, 괄호 및 콜론 누락 등의 문법 오류 → 실행이 되지 않음)

예외(exception) : 프로그램 실행 중 감지되는 에러 → 실행은 됨

## 예외(Exception)

프로그램 실행 중에 감지되는 에러

### 내장 예외(Built-in Exceptions)

예외 상황을 나타내는 예외 클래스들

→ 파이썬에 이미 정의되어 있고, 특정 예외 상황에 대한 처리를 위해 사용

ZeroDivisionError : 나누기 또는 모듈로 연산의 두 번째 인자가 0 일때

 NameError : 지역 또는 전역 이름을 찾을 수 없을 때

TypeError : 타입 불일치, 인자 누락, 인자 초과, 인자 타입 불일치, 

ValueError : 연산, 함수는 문제X, 부적절한 값을 인자로 받음

IndexError : 시퀀스 인덱스가 범위를 벗어날 때 발생

KeyError : 딕셔너리에 해당 키가 존재하지 않는 경우

ModuleNotFoundError : 모듈을 찾을 수 없을 때 발생

ImportError : import하려는 이름을 찾을 수 없을 때 발생

KeyboardInterrupt : 사용자가 ctrl c / del를 누를 때 발생 , 무한 루프 시 강제 종료

IndentationError : 잘못된 들여쓰기와 관련된 문법 오류

## 예외 처리(Exception Handling)

예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법

### 예외처리 사용 구문

try : 예외가 발생할 수 있는 코드 작성, 일단 실행해!

except : 예외가 발생했을 때 실행할 코드 작성

else : try에서 예외가 발생하지 않았을 때 실행할 코드 작성

finally : 예외 발생여부와 상관없이 항상 실행할 코드 작성

### Try & Except

```python
try:
	#예외가 발생할 수 있는 코드
except 예외: 
	#예외 처리 코드
	
	# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
```

[복수 예외 처리]

- int(’a’) 문자열을 int로 형변환 : ValueError
- 100/0 0으로 숫자를 나눔 : ZeroDivisionError
- 발생 가능한 에러를 모두 명시하거나 별도로 작성하기

### else & finally

- else 블록은 예외가 발생하지 않았을 때 추가 작업을 진행
- finally 블록은 예외가 발생 여부와 상관없이 항상 실행할 코드를 작성

## 예외처리 주의 사항

- 내장 예외의 상속 계층 구조 주의

→ 내장 예외 클래스는 상속 계층구조를 가지기 때문에 except 절로 분기 시 반드시 하위 클래스를 먼저 확인할 수 있도록 작성

## 예외 객체 다루기

### as 키워드

- 예외 객체 : 예외가 발생했을 때 예외에 대한 정보를 담고 있는 객체
- except 블록에서 예외 객체를 받아 상세한 예외 정보를 활용 가능

### try-except와 if-else

함께 사용할 수 있음

```python
try:
	x = int(input('숫자를 입력하세요 : '))
	if x < 0:
			print('음수는 허용되지 않습니다')
	else:
		  print('입력한 숫자:', x)
except ValueError :
		print('오류 발생')
```

## EAFP & LBYL

### EAFP “ Easier to Ask for Forgiveness than Permission”

예외 처리를 중심으로 코드를 작성하는 접근 방식(try-except)

일단 ㄱ

```python
# EAFP (Easier to Ask for Forgiveness than Permission, 허락보다 용서 구하기)
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')
```

### LBYL “Look Before You Leap”

값 검사를 중심으로 코드를 작성하는 접근 방식(if-else)

돌다리도 두들겨보고 건너!

```python
# LBYL (Look Before You Leap, 돌다리도 두들겨보고 건너기)
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```

| EAFP | LBYL |
| --- | --- |
| "일단 실행하고 예외를 처리” | “실행하기 전에 조건 검사” |
| 코드를 실행하고 예외가 발생하면 예외처리를 수행 | 코드 실행 전에 조건문 등을 사용하여 예외 상황을 미리 검사하고, 예외 상황을 피하는 방식 |
| 코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 니라, 예외가 발생한 후에 예외를 처리 | 코드가 좀 더 예측 가능한 동작을 하지만 코드가 더 길고 복잡해질 수 있음 |
| 예외 상황을 예측하기 어려운 경우 유용 | 예외 상황을 미리 방지하고 싶을 때 유용 |

---

# 클래스의 의미와 활용

- 구조를 명확히 할 수 있기 때문에 작성한 코드가 훨씬 깔끔해지고 나중에 수정하거나 기능을 추가할 때 더 쉽고 안전해짐