# 메서드(Method)

클래스 내부에 정의된 함수로 해당 객체가 어떻게 동장할지를 정의

## 메서드 종류

1. 인스턴스 메서드
2. 클래스 메서드
3. 스태틱 매서드

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