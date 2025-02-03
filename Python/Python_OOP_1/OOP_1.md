## 프로그래밍 패러다임

### 절차 지향 프로그래밍(Procedural Programming)

프로그램을 함수와 로직(절차) 중심으로 작성, 데이터를 함수에 전달하며 순차적으로 처리

(계속 작성한 방식)

```python
# 절차 지향 사고
# 예: 변수와 함수를 별개로 다룸
name = 'Alice'
age = 25

def introduce(name, age):
    print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')

introduce(name, age)
```

- 입력을 받고, 처리하고, 결과를 내는 과정이 위에서 아래로 순차적으로 흐르는 형태
- 순차적인 명령어 실행
- 데이터와 함수(절차)의 분리
- 함수 호출의 흐름이 중요

⇒ 순서를 하나씩 밟아 나가는 방식

*데이터를 다시 재사용하기 보다는 처음부터 끝까지 실행되는 결과물이 중요

### 절차 지향적 프로그래밍의 한계

1. 복잡성 증가
- 프로그램 규모가 커질수록 데이터와 함수의 관리가 어려움
- 전역 변수의 증가로 인한 관리의 어려움

1. 유지 보수 문제
- 코드 수정 시 영향 범위 파악이 어려움

### 객체 지향 프로그래밍(Object Oriented Programming)

데이터와 함수를 하나의 단위(객체)로 묶어서 관리

객체들을 조합하고 재활용하는 방식으로 프로그램 구성

- 사람(객체)안에 name, age와 이와 관련된 기능(메서드)포함

```python
# 객체 지향 사고
# 예: 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')

alice = Person('Alice', 25)
alice.introduce()  # 객체가 자신의 정보를 출력

```

list.append()/ dict.items() - 앞 객체를 호출

- 프로그램을 데이터(변수)와 그 데이터를 처리하는 함수(메서드)를 하나의 단위(객체)로 묶어서 조직적으로 관리
- 데이터와 메서드의 결합
- 공통의 목표가 있고 그걸 하나의 객체로 묶음 → 순서X

| 절차 지향 | 객체 지향 |
| --- | --- |
| 데이터와 해당 데이터를 처리하느 ㄴ함수(절차) 분리

함수 호출의 흐름이 중요 | 데이터와 해당 데이터를 처리하는 메서드(함수)를 하나의 객체(클래스)로 묶음

객체 간 상호작용과 메세지 전달이 중요 |
| ‘어떤 순서로 처리할까?’ | ‘어떤 객체가 이 문제를 해결할까?’ |
|  | ‘ 이 객체는 어떤 속성과 기능을?’ |

객체 지향은 수동적인 데이터가 능동적인 객체로 변화

절차 지향에서는 데이터가 함수의 매개 변수로 전달되어 처리되는 수동적 존재 엿지만, 객체 지향에서는 데이터와 해당데이터를 처리하는 메서드가 하나의 객체로 통합되어 스스로 기능을 수행하는 능동적 존재가 됨

코드의 구조화와 재사용성을 높이는 동시에 실제 모델링 방식과 더 유사한 프로그래밍을 가능하게 함

절차 지향과 객체 지향은 대조되는 개념X

- 기존 절차 지향을 기반으로 보완하기 위해 객체라는 개념을 도입해 상속, 코드 재사용성, 유지 보수성 등의 이점을 가지는 패러다임
- 절차 + a

## 객체와 클래스

### 객체(Object)

실제 존재하는 사물의 추상화한 것, ‘속성’,  ‘동작’을 가짐

강아지라는 객체를 이름, 종, 나이와 짖기, 뛰기(행동) 등으로 표현

### 클래스(Class)

객체를 만들기 위한 설계도

데이터와 기능을 함께 묶는 방법을 제공

파이썬에서 타입을 표현하는 방법

>> 클래스로부터 여러개의 객체를 쉽게 찍어낼 수 있음

가수 라는 객체

속성(변수) = 생년월일, 국적

동작(메서드) = 랩, 댄스

→ 가수라는 클래스 ⇒ 객체(아이유, 방탄 등)

객체 특징

- 속성(Attribute) : 객체의 상태/데이터
- 메서드(method) : 객체의 행동/기능
- 고유성 : 각 객체는 고유한 특성을 가짐

## 클래스(Class)

데이터와 기능을 하나의 틀로 묶어 관리하는 방법

사용자 정의 객체를 만드는 수단이자 속성과 메서드를 정의

클래스 이름 : 파스칼 케이스(Pascal Case) : 대문자로 시작하고 띄어쓰기 후 다시 시작하는 단어도 대문자로 

__ init __ 메서드 : ‘생성자 메서드’, 새로운 객체를 만들 때 필요한 초기값을 성정, 새로운 객체를 만들 때 호출

언더바(_) : 개발자가 직접 호출을 진행하지 않음

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')

```

## 인스턴스(Instance)

클래스를 통해 생성된 객체

클래스가 설계도라면 인스턴스는 실제로 만든 물건

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')
        
     # Person('Alice', 25)라고 하면 Person이라는 설계도로부터 이름이 Alice이고 나이가 25인 '사람 객체'
     #p1, p2는 다름(코드 작성)

```

## 클래스와 인스턴스

아이유는 객체(o), 

아이유는 인스턴스이다(x,누구의 인스턴스인지 명확하게) 

아이유는 가수의 인스턴스이다(o)

클래스를 만든다 == 타입을 만든다

```python
name = 'Alice' #str의 인스턴스

print(type(name))   #<class 'str'>
```

→ 우리가 사용해왔던 데이터 타입은 모두 클래스 였다

‘hello.upper’

upper → str이라는 클래스 안에 있는 인스턴스

## 클래스 구성요소

### 클래수 구조 _ 01

위치 인자는 반드시 작성

## 클래스 변수와 인스턴스 변수

클래스 변수와 동일한 이름으로 인스턴스 변수 생성시 클래스 변수가 아닌 인스턴스 변수에 먼저 참조

---

# 메서드(Method)

클래스 내부에 정의된 함수로 해당 객체가 어떻게 동장할지를 정의

## 메서드 종류

1. 인스턴스 메서드
2. 클래스 메서드
3. 스태틱 매서드

## 인스턴스 메서드(instance method)

클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드

 → 인스턴스의 상태를 조작하거나 동작을 수행

### 내부 구조

- 클래스 내부에 정의되는 메서드의 기본
- 반드시 첫 번째 인자로 인스턴스 자신(self)을 받음
- 인스턴스의 속성에 접근하거나 변경 가능
- self는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능(권장X)

### self 동작원리

-upper메서드를 사용해 문자열 ‘hello’를 대문자로 변경

```python
'hello'.upper()

#실제 동작 원리
str.upper('hello')

#객체 지향 방식의 메서드로 호출하는 표현(단축형 호출)
```

str클래스가 upper 메서드를 호출했고 첫번째 인자로 문자열 인스턴스가 들어가거나

인스턴스 메서드의 첫번째 인자가 반드시 인스턴스 자신인 이유

‘hello’라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자로 활용되는 것이 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적인 표현

인스턴스는 독립적,

```python
class Counter:
    def __init__(self):
        self.count = 0  #자기 자신에 0을 가짐
    
    def increment(self):
        self.count += 1

c = Counter()
print(c.count)  #0
c.increment()
print(c.count)  #1

c2 = Counter()  #인스턴스는 서로 독립적
c.increment()   #c2는 increment를 호출한 적이 없음
print(c2.count)  #0
```

### 생성자 메서드(constructor method)

인스턴스 객체가 생성될 때 자동으로 호출되는 메서드 → 인스턴스 변수들의 초기값 설정

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population()
        #순서가 중요하지 않기 때문에 밑에꺼가 위로 가도 됨
    @classmethod
    def increase_population(cls):
        cls.population += 1

person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  # 2

Person.increase_population()
print(Person.population)

```

## 클래스 메서드(class method)

클래스가 호출하는 메서드 → 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

@classmehtod 데코레이터를 사용하여 정의

호출 시 첫번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달

클래스를 인자로 받아 클래스 속성을 변경하거나 읽는데 사용

- cls는 매개변수 이름일 뿐이며 다름 이름으로 설정 가능

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population()
        #순서가 중요하지 않기 때문에 밑에꺼가 위로 가도 됨
    @classmethod
    def increase_population(cls):
        cls.population += 1

person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  # 2

Person.increase_population()
print(Person.population)

```

## 스태틱 메서드(정적 메서드, static method)

클래스, 인스턴스와 상관없이 독립적으로 동작하는 메서드

@staticmethod 데코레이터를 사용하여 정의

호출 시 자동으로 전달받는 인자가 없음(self, cls를 받지 않음)

인스턴스나 클래스 속성에 직접 접근하지 않는 ‘도우미 함수’와 비슷한 역할

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a+b

print(MathUtils.add(1, 2))  # 3

```

## 메서드 활용

```python
# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현

class BankAccount:
    interest_rate = 0.02  # 이자율

    def __init__(self, owner, balance=0):    # 인스턴스 owner, balance
        self.owner = owner  # 계좌 소유자
        self.balance = balance  # 초기 잔액

    # 입금 #인스턴스 조작
    def deposit(self, amount):
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액이 부족합니다.')

    # 이자율 설정
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate        

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive(amount):
        return amount > 0

# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount('Alice', 1000)
print(alice_acc.owner)
print(alice_acc.balance)

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500)
print(alice_acc.balance)   #1500

# 잔액 확인 (인스턴스 변수 참조)
alice_acc.withdraw(3000)
print(alice_acc.balance)

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03) # 0.03
print(BankAccount.interest_rate)
# 잔액이 양수인지 확인 (정적 메서드 호출)
print(BankAccount.is_positive(alice_acc.balance))  # True

```

### 메서드 정리

- 인스턴스 메서드 : 인스턴스의 상태를 변경하거나 해당 인스턴스의 특정 동작을 수행
- 클래스 메서드 : 인스턴스의 상태에 의존하지 않는 기능을 정의, 클래스 변수를 조작하거나 레벨의 동작을 수행
- 스태틱 메서드 : 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

클래스 → 클래스 메서드, 스태틱 메서드/인스턴스 → 인스턴스 메서드

모든 메서드를 호출할 수 있지만 클래스 메서드와 스태틱 메서드만 사용해야함

```python
class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'

instance = MyClass()
# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance))
print(MyClass.class_method())
print(MyClass.static_method())

# 인스턴스가 할 수 있는 것
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())

```

---

# 클래스-인스턴스 이름 공간

클래스를 정의하면, 클래스와 해당하는 이름 공간 생성

인스턴스를 만들면 인스턴스 객체가 생성되고 독립적인 이름 공간 생성

인스턴스에서 특정 속성에 접근하면 인스턴스 → 클래스 순으로 탐색

독립적인 이름 공간

- 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적 접근이 불가능
- 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장
- 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작

        → 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌

---

# 매직 메서드(magic method)

‘ __’가 있는 메서드 : 특수한 동작을 하기 위함

특정 상황에서 자동으로 호출

- __str __(self)

  - 내장 함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경

---

# 데코레이터

다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

인자에 함수가 들어감