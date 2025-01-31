# Data Structure

여러 데이터를 효과적으로 사용, 관리하기 위한 구조

(str, list, dict 등)

### 자료 구조

- 컴퓨터 공학에서는 ‘자료 구조’라고 함
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것

### 데이터 구조 활용

- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 메서드를 호출하여 다양한 기능 활용

## 메서드(method)

객체에 속한 함수 → 객체의 상태를 조작하거나 동작을 수행

```python
print(type('1')) #<class'str'>
print(type([1,2]))
print(help(str))

#클래스 파트에서 이어서 진행할 예정
def add(a,b):
    return a+b

class Calculator:
    def add(self, a, b):
        return a+b
    
    
    
#함수 호출
add(1, 2)

#메서드 호출
a = Calculator()
a, add(1,2)
```

### 메서드 특징

- 메서드는 클래스(class)내부에 정의되는 함수
- 클래스는 파이썬에서 ‘타입을 표현하는 방법’이며 은연중에 사용
- help 함수를 통해 str을 호출해보면 class였다는 것을 확인 가능

💫 메서드는 어딘가(클래스)에 속해있는 함수, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재

### 호출 방법

데이터 타입 객체.메서드()

```python
#메서드 호출방법
'hello'.capitalize()
```
