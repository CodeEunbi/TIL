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
    
    
