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