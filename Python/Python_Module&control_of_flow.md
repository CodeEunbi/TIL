# 모듈( Module)

한 파일로 묶인 변수와 함수의 모음

특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

### math내장 모듈

- 파이썬이 미리 작성해둔 수학 관련 변수와 함수가 작성된 모듈

```python
import math  #import = 가져오다
print(math.pi)  #이미 내장된 모듈
print(math.sqrt(4)) #제곱근
```

### 모듈을 가져오는 방법

- import문 사용(권장)

```python
import math
print(math.sqrt(4))
```

- from 절 사용

        - 모듈에서 가져온 게 아니기 때문에 사용자가 만든 함수라고 오해할 수 있음

        - 이름 충돌이 날 수도 있음

        - 경로가 길면 ‘.’ 사용, from 여러 번X

```python
from math import sqrt #어디에서 ~을 가져오겠다
print(sqrt(4))  #모듈을 가져오지 않음
```

## 모듈 사용

### .(dot) 연산자

- 점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라 라는 의미

```python
#모듈명.변수명
print(math.pi)

#모듈명.함수명
print(math.sqrt(4))
```

### 주의 사항

- 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
- 마지막에 import된 이름으로 대체됨

```python
from math import pi, sqrt
from my_math import sqrt
#모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음

from math import *
```

- 모듈을 가져오고 함수 호출

### ‘as’키워드

- as 키워드를 사용하여 별칭(alias)을 부여
- 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결

```python
from math import sqrt
from my_math import sqrt as my_sqrt

sqrt(4)
my_sqrt(4)
```

## 사용자 정의 모듈

### 직접 정의한 모듈

다른 파일에 함수를 만들고 새로운 파일에 import 작성 후 불러오기

## 파이썬 표준 라이브러리(Python Standard Library)

파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

## 패키지(Package)

연관된 모듈들을 하나의 디렉토리에 모아 놓은 것

### 패키지 사용

- import할 필요가 없을 경우(상위폴더) from 사용 후 import하기

```python
from my_package.math import my_math
```

- 그 이후 import
- PSL 내부 패키지 : 설치 없이 바로import하여 사용
- 외부 패키지 : pip를 사용하여 설치 후 import 필요(더 많이 활용하게 됨)

### pip(파이썬 패키지 관리자)

외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

PyPI(Python Package Index)에 저장된 외부 패키지들을 설치

**패키지 설치**

- 최신 버전/ 특정 버전/ 최소 버전을 명시하여 설치할 수 있음

```python
$ pip install SomePackage           #최신버전
$ pip install SomePackage==1.0.5    #특정버전
$ pip install SomePackage>=1.0.4    #최소버전
```

- 패키지 삭제 uninstall
- requests : 외부 API  서버로 요청을 보냄(사용법 가이드 문서 존재)
- request 라이브러리에 있는 get함수

```python
$ pip install requests
import requests

url = ''
response = requests.get(url).json()

print(response)
```

### 패키지 사용 목적

모듈들의 이름공간을 구분하여 충돌을 방지

모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할

---

# 제어문(Control Statement)

코드의 실행 흐름을 제어하는 데 사용되는 구문

조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

### 조건문

- if, elif, else

### 반복문

- for, while

### 반복문 제어

- break, continue, pass

## 조건문(Conditional Statement)

주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

- if/elif/else
- elif/else는 필수가 아님

### ‘if’ statement

```python
#기본 구조
if 표현식 :                       
		코드블록
elif 표현식 :
		코드블록
else:
		코드블록
```

**복수 조건문**

- 조건식을 동시에 검사하는 것이 아니라 ‘순차적’으로 비교

**중첩 조건문**

- if ~밑에 중첩으로 if~ 를 한 번 더 적음

```python
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

## 반복문(Loop statement)

주어진 코드 블록을 여러 번 반복해서 실행하는 구문

### 반복 가능한 객체(iterable)

반복문에서 순회할 수 있는 객체(시퀀스 뿐만 아니라 dict, set 등도 포함)

→ 출력되는 순서는 보장을 해줘서 반복이 가능

### 사용되는 키워드

- for : 특정 작업을 반복적으로 수행
- while : 주어진 조건이 참인 동안 반복해서 실행 > 종료 조건이 필요

### for

임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

- for statement의 기본 구조

```python
for 변수 in 반복 가능한 객체:
		코드 블록
```

### for문 작동원리

- 리스트 내 첫 항목이 반복변수에 할당되고 코드블록 실행
- 컬렉션에 해당하는 것들 ⇒ 복수형으로 변수명 짓기

```python
items = ['apple', 'banana', 'coconut'] #3번 반복

for item in items:
		print(item)
		
"""
apple
banana
coconut
"""
```

**문자열 순회, range 순회**

**딕셔너리 순회**

- 딕셔너리 → key로 접근

**인덱스로 리스트 순회**

- 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경

## While statement

주어진 조건식이 참(True)인 동안 코드를 반복해서 실행 

== 조건식이 거짓(False)가 될 때까지 반복

```python
#while statement의 기본구조
while 조건식 :
		코드블록
```

- 횟수보다 해결이 되어야 끝나는 조건문
- 종료 조건에 가까워질 수 있도록 하는 것이 중요

**반드시 종료 조건이 필요하다!!**

### 적절한 반복문 활용

### for

- 반복 횟수가 명확하게 정해져 있는 경우 유용
- 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때

### while

- 반복횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
- 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

## 반복 제어

for, while 은 매 반복마다 본문 내 모든 코드를 실행하지만 때떄로 일부만 실행하는 것이 필요함

### 제어 키워드

- break : 반복을 즉시 중지
- continue :  다음 반복을 건너뜀
- pass : 아무런 동작도 수행하지 않고 넘어감

```python
# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass 아무런 작업도 하지 않음
for i in range(10):
    pass

def my_func(a):
    pass

```

break : 프로그램 종료 조건 만들기, 리스트에서 첫 번째 짝수만 찾은 후 반복 종료

```python
# break 예시 1 - "프로그램 종료 조건 만들기"
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')

```

```python
# break 예시 2 - "리스트에서 첫번째 짝수만 찾은 후 반복 종료하기"
numbers = [1, 3, 5, 6, 7, 9, 10, 11]

# 첫 번째 짝수를 찾았는지 여부를 저장하는 플래그 변수
# 초기값은 찾지 못했다(False)로 설정
found_even = False

for number in numbers:
    if number % 2 == 0:
        print(f'첫번째 짝수 {number}를 찾았습니다.')
        # 짝수를 찾은 상태이므로 True로 변경
        found_even = True
        break

# 반복문이 끝날 때까지 짝수를 찾지 못한 경우
if found_even == False:
    print('짝수를 찾지 못함')

```

continue : 현재 반복문의 남은 코드를 건너뛰고 다음 반복으로 넘어감

pass : 코드 작성 중 미완성 부분, 조건문에서 아무런 동작을 수행하지 않아야 할 때, 무한루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법

---

# List Comprehension

간결하고 효율적인 리스트 생성 방법

## List Comprehension 구조

append : 리스트 값 추가/ 리스트.append(값)

comprehension 남용하지 말자!

**활용예시**

- 2차원 배열 생성 시 (인접행렬 생성 시)

---

# 모듈 내부

내장 함수 help를 사용해 모듈에 무엇이 들어왔는지 확인 가능

## enumerate(iterable, start = 0)

iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

"""
0 apple
1 banana
2 cherry
"""

for index, fruit in enumerate(fruits, 3):
    print(index, fruit)

"""
3 apple
4 banana
5 cherry
"""
```