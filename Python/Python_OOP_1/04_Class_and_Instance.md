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

    p1 = Person('Alice', 25)
    p1.introduce() #안녕하세요. 저는 Alice, 나이는 25살입니다.

    p2 = Person('Bella', 30)
    p2.introduce() #안녕하세요. 저는 Bella, 나이는 30살입니다.
        
     # Person('Alice', 25)라고 하면 Person이라는 설계도로부터 이름이 Alice이고 나이가 25인 '사람 객체'
     #p1, p2는 다름

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

### 클래수 구조_01

위치 인자는 반드시 작성

## 클래스 변수와 인스턴스 변수

클래스 변수와 동일한 이름으로 인스턴스 변수 생성시 클래스 변수가 아닌 인스턴스 변수에 먼저 참조
