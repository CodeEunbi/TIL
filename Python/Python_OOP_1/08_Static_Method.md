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