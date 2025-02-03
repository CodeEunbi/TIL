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