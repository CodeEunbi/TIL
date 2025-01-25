# 형변환(Type Conversion)

한 데이터 타입을 다른 데이터 타입으로 변환하는 과정

암시적 형변환/명시적 형변환

## 암시적 형변환(Implict Type conversion)

파이썬이 자동으로 수행하는 형변

- 정수와 실수의 연산에서 정수가 실수로 변환
- Boolean과 Numeric Type에서만 가능

       - True = 1, False = 0

```python
print(3+0.5) #8.0

print(True + 3) #4

print(True + False) #1
```

## 명시적 형변환(Explicit Type conversion)

프로그래머가 직접 지정하는 형변환

암시적 형변환이 아닌 경우를 모두 포함

- str → int : 형식에 맞는 숫자만 가능

```python
print(int('1')) #1

#ValueError : invalid literal for int() with base 10 : 3.5
print(int('3.5'))

print(int(3.5)) #3

print(float('3.5')) #3.5
```

- int → str : 모두 가능

```python
print(str(1) + '등') #1등
```
