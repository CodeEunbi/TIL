# 연산자

(산술연산자는 pt.1)

[Python Basic Syntax 01](https://www.notion.so/Python-Basic-Syntax-01-25-01-20-181c18418666802d9150c69e61e2be47)

## 복합연산자

연산과 할당이 함께 이루어짐

| 기호 | 예시 | 의미 |
| --- | --- | --- |
| += | a += b | a = a+b |
| -= | a -= b | a = a - b |
| *= | a *= b | a =a * b |
| /= | a /= b | a =a/b |
| //= | a//=b | a = a//b |
| %= | a%=b | a =a%b |
| **= | a ** = b | a = a** b |

## 비교 연산자

| 기호 | 내용 |
| --- | --- |
| < | 미만 |
| < = (≤) | 이하 |
| > | 초과  |
| > = (≥) | 이상 |
| == | 같음 |
| ! = (≠) | 같지 않음 |
| is | 같음 |
| is not | 같지 않음 |

! → not/부정

### ==비교 연산자

- 값(데이터)가 같은지를 비교
- 동등성(equality)
- 예를 들어, 1 == True의 경우 파이썬이 내부적으로 True를 1로 간주할 수 있으므로 True결과가 나옴

### is 비교 연산자

- 객체 자체가 같은지를 비교
- 식별성(identity)
- 두 변수가 동일한 메모리 주소(레퍼런스)를 가리키고 있을 때만 True

#SynataxWarning : ‘is’ with a literal. Did you mean “==”?(경고)

### is 대신 == 사용

- is는 객체의 식별성을 비교하므로, 숫자나 문자열 같은 값 자체를 비교하려는 상황에서는 적절하지 않음
- is 연산자를 이용하면 코드 상에서 의도치 않게 False 가 나오거나 파이썬 버전에 따라 내부 구현 차이 때문에 기대하는 결과가 달라질 수 있음
- 예를 들어, is를 사용하면 항상 False가 나오지만 실제로 데이터 값은 논리적으로 같기 때문에 ==를 써야 의미가 맞음

```python
print(1 is True) #False
print(2 is 2.0) #False
print(1 == True) #True
print(2 == 2.0) #True
```

### is 사용 - None 비교

1. **None을 비교를 비교할 때**
- ‘같은 주소에 있는가’라는 질문에 답해야할 때
- 파이썬 공식 스타일 가이드에서는 None을 비교할 때 == 대신 is를 사용하라고 권장

1. **싱클턴 객체를 비교할 때**
- 싱글턴(Singleton)객체

  - 프로그램 전체에서 오직 1개만 존재하도록 만들어진 특별한 객체

  - None, True, False

- 이들은 파이썬 전체에서 딱 1개만 사용, 새로 만들어지는게 아니라 미리 정해진 하나의 객체가 재사용되기 때문에 여러 곳에서 쓰더라도 같은 메모리 주소를 가리킴

+) 리스트나 객체 비교

- 리스트 또는 다른 가변 객체를 비교, 값 자체가 같은 지 확인하려면 ==를 사용
- 두 변수가 완전히 동일한 객체를 가리키는지를 확인해야 한다면 is를 사용

### == 와 is 정리

- 값 비교에는 ==를 사용, 객체(레퍼런스)비교에는 is 사용
- 숫자나 문자열, 불리언 값 등 동등성(값)을 판단해야할 때 is를 쓰면 의도치 않은 결과(False)가 나올 수 있으며, 파이썬 내부적인 최적화나 타입차이로 인해 일관성이 깨질 수 있음
- is 는 주로None 비교나 싱글턴 객체(True or False)에 대한 정체성 체크에 사용

## 논리 연산자

| 기호 | 연산자 | 내용 |
| --- | --- | --- |
| and | 논리곱 | 두 피연산자 모두 True인 경우에만 전체 표현식을 True로 평가 |
| or  | 논리합 | 두 피연산자 중 하나라도 True인 경우 전체 표현식을 True로 평가 |
| not | 논리부정 | 단일 피연산자를 부정 |
- 비교 연산자와 함께 사용 가능

## 단축평가

논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

‘ ‘ → False / ‘?’ → True (문자열 안에 없으면 거짓, 있으면 참)

 

앞에 ‘0’이 나오면 평가 중단 무조건 ‘0’

```python
vowels = 'aeiou'

print(('a' and 'b') in vowels)  #False
print(('b' and 'a') in vowels)  #True

print(3 and 5)  #5
print(3 and 0)  #3
print(0 and 3)  #0
print(0 and 0)  #0

print(5 or 3)  #5
print(3 or 0)  #3
print(0 or 3)  #3
print(0 or 0)  #0
```

### and

- 첫번째 피연산자가 False 인 경우, 전체 표현식은 False

        → 두번 째 피연산자가 평가되지 않고 그 값을 무시

- 첫번째 피연산자가  True 인 경우 전체 표현식의 결과는 두 번째 피연산자에 의해 결정

        → 두번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환

### or

- 첫번째 피연산자가 True 인 경우 전체 표현식은 True

       → 두 번째 피연산자는 평가되지 않고 무시

- 첫번째 피연산자가 False인 경우, 전체 표현식의 결과는 두번째 피연산자에 의해 결정

        → 두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환

⇒ 코드 실행을 최적화하고 불필요한 연산을 피할 수 있도록 함

## 멤버십 연산자

특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부 확인

| 기호 | 내용 |
| --- | --- |
| in | 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인 |
| not in | 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인 |

## 시퀀스형 연산자

‘+’와 *는 시퀀스 간 연산에서 산술연산자 일 때와 다른 역할을 가짐

| 연산자 | 내용 |
| --- | --- |
| + | 결합 연산자 |
| * | 반복 연산 |


## Trailing Comma

- 컬렉션의 마지막 요소 뒤에 붙는 쉼표
- 일반적으로 ‘선택사항’
- 단, 하나의 요소로 구성된 튜플을 만들 때 필수
- 각 요소를 별도의 줄에 작성
- 마지막 요소 뒤에 trailing comma 추가
- 닫는 괄호는 새로운 줄에 배치

장점

1. 가독성 향상
- 각 줄이 동일한 패턴을 가짐
- 코드 리뷰 용이

2. 유지보수 용이성
- 항목 추가/ 제거 간단
- 실수로 인한 구문 오류 방지