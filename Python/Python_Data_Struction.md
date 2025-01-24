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

#클래스 파트에서 이어서 진행할 예정정
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

---

# 시퀀스 데이터 구조

## 문자열 조회/탐색 및 검증 메서드

s.find(x) : x의 첫 번째 위치를 반환. 없으면 -1을 반환

```python
# find
text = 'banana'
print(text.find('a'))  #1
print(text.find('z'))  #-1
```

s.index(x) : x의 첫 번째 위치를 반환. 없으면 오류 발생

```python
# index
print(text.index('a')) #1
# print(text.index('z')) #ValueError: substring not found
```

s.isupper() : 문자열 내의 모든 문자가 대문자인지 확인

```python
# isupper
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False
```

s.islower() : 문자열 내의 모든 문자가 소문자인지 확인

```python
# islower
print(string1.islower())  # False
print(string2.islower())  # False
```

s.isalpha() : 문자열 내의 모든 문자가 알파벳인지 확인
*단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)

```python
# isalpha
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False
```

.replace(*old, new[,count]*) : 바꿀 대상 글자를 새로운 글자로 반환

[count] :  선택, 바꿀 개수

```python
# replace
text = 'Hello, world! world world'

#.replace(old, new)
new_text1 = text.replace('world', 'Python')

#.replace(old, new, [count])
new_text2 = text.replace('world', 'Python', 1)

print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world
```

- 문자열은 불변이기 때문에 원본을 프린트하면 그대로 나옴
- .replace 변환된 값으로 출력

. strip(*[chars]*) : 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거

```python
# strip
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)            #'Hello, world!'
```

.split(*sep=None, maxsplit = -1*)

sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환

sep가 None이면 그걸 기준으로 구분

```python
# split
text = 'Hello, world!'
words1 = text.split(',')
words2 = text.split()
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']
```

*‘separator*’**.join**(*iterable*) : iterable의 문자열을 연결한 문자열을 반환

```python
# join
words = ['Hello', 'world!', 3, 100] 
#TypeError: sequence item 2: expected str instance, int found
#정수가 섞이면 안됨, 작성할 경우 문자열로 바꾸고 작성성
new_text = '-'.join(words)
print(new_text)  # Hello-world!
```

s.capitalize() : 가장 첫 번째 글자를 대문자로 변경

s.title() : 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환

s.upper() : 모두 대문자로 변경

s.lower() : 모두 소문자로 변경

s.swapcase() : 대 <>  소문자 서로 변경

## 리스트

### 값 추가 및 삭

**.append(x)** : 리스트 마지막에 항목x를 추가

```python
# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
print(my_list.append(4))  #None 리턴이 없음, append 자체 반환값X 
```

**.extend(*iterable*)** : 리스트에 다른 반복 가능한 객체의 모든 항목을 추가(+=와 같은 기능)

```python
# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# my_list.extend(5) #TypeError: 'int' object is not iterable, int를 넣을 수가 없음

# append와의 비교
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]
```

- append와 비교 : append는 그대로 추가, extend는 다 풀어서 추가 및 정수 X

**.insert(i, x)** : 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입

- append, extend는 끝에 추가

```python
# insert
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]

```

**. remove(x)** : 리스트에서 첫 번째로 일치하는 항목을 삭제

```python
# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]
```

**.pop(i) : 리스트에서 지정한 인덱스의 항목을 제거하고 반환, 작성하지 않을 경우 마지막 항목을 제거**

```python
# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  #5
print(item2)  #1
print(my_list)  #[2, 3, 4]
```

. clear() : 리스트의 모든 항목을 삭제

```python
# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []
```

### 탐색 및 정렬

**.index(x)** : 리스트에서 첫 번째로 일치하는 항목 x의 인덱스로 반환

```python
# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1

```

**.count(x)** : 리스트에서 항목x의 개수를 반환

```python
# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3
```

**.reverse()** : 리스트의 순서를 역순으로 변경(정렬X)

```python
# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list.reverse())  #None
print(my_list)  #[9, 1, 8, 2, 3, 1]
```

**.sort ()** : 원본 리스트를 오름차순으로 정렬

```python
# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
#True로 바꾸면 역전이 된다, 원래 기본값은 False
print(my_list)  # [100, 3, 2, 1]
```

---

# 복사

## 객체와 참조

### 가변/불변 객체 개념

1. Mutable(가변)객체 : 생성 후 내용을 변경할 수 있는 객체
- ex) 리스트(list), 딕셔너리(dict), 집합(set)

2. Immutable(불변)객체 : 생성 후 내용을 변경할 수 없는 객체
- ex) 정수(int), 실수(float), 문자열(str), 튜플(tuple)

### 변수 할당의 의미

- 파이썬에서 변수 할당은 객체에 대한 참조를 생성하는 과정
- 변수는 객체의 메모리 주소를 가리키는 Label 역할을 함
- ‘=’연산자를 사용하여 변수에 값을 할당
- 할당 시 새로운 객체가 생성되거나 기존 객체에 대한 참조가 생성

### 메모리 참조 방식

- 변수는 객체의 ‘메모리 주소’를 저장
- 여러 변수가 동일한 객체를 참조할 수 있음

```python
#가변
a = [1, 2, 3, 4]
b = a 
b[0] = 100

print(a)  # [100, 2, 3, 4]
print(b)  # [100, 2, 3, 4]
print(a is b)  #True

#불변
print('\n불변(immutable) 객체 예시')
a = 20
b = a
b = 10

print(f'a의 값: {a}')  #20
print(f'b의 값: {b}')  #10
print(a is b)  #False
```

- 같은 주소를 봤던 것

### id()함수를 사용한 메모리 주소 확인

- id() 함수를 사용하여 객체의 메모리 주소를 확인 가능
- is 연산자를 통해 두 변수가 같은 객체를 참조하는 지 확인 가능

```python
print('\n메모리 주소 확인')
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f'x의 id: {id(x)}')
print(f'y의 id: {id(y)}')
print(f'z의 id: {id(z)}')
print(f'x와 y는 같은 객체인가? {x is y}') #True
print(f'x와 z는 같은 객체인가? {x is z}') #False
```

### 가변/불변 메모리 관리 방식

- 가변 객체

 - 생성 후에도 그 내용을 수정할 수 있음 

 - 객체의 내용이 변경되어도 같은 메모리 주소를 유지

- 불변 객체

   - 생성 후 그 값을 변경할 수 없음

  - 새로운 값을 할당하면 새로운 객체가 생성되고, 변수는 새 객체를 참조하게 됨

### 이러한 동작 방식 이유

1. 성능 최적화
- 불변 객체는 변경이 불가능하므로, 여러 변수가 같은 객체를 안전하게 공유할 수 있음
- 가변 객체는 내용 수정이 빈번한 경우 새 객체를 생성하지 않고 직접 수정하여 성능을 향상 시킴

2. 메모리 효율성
- 불변 객체는 동일한 값을 가진 여러 객체가 메모리를 공유할 수 있어 효율적
- 가변 객체는 크기가 큰 데이터를 효율적으로 수정할 수 있음

# 얕은 복사(Shallow Copy)

객체의 최상위 요소만 새로운 메모리에 복사하는 방법

내부에 중첩된 객체가 있다면 그 객체의 참조만 복사됨

## 구현 방법

- 리스트 슬라이싱
- copy()메서드
- list() 함수

### 얕은 복사의 한계

- 1차원 리스트에서의 얕은 복사

```python
# 1차원 리스트
a = [1, 2, 3]     
b = a[:]  # 슬라이싱
c = a.copy()  # copy() 메서드
d = list(a)  # list() 함수

b[0] = 100
c[0] = 999
d[0] = 8080
print(a)  #[1, 2, 3]
print(b)  #[100, 2, 3]
print(c)  #[999, 2, 3]
print(d)  #[8080, 2, 3] 
```

- 2차원 리스트와 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우

```python
# 다차원 리스트
print('\n다차원 리스트 얕은 복사의 한계')
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  #[1, 2, [3, 4, 5]]
print(b)  #[999, 2, [3, 4, 5]]

b[2][1] = 100
print(a)  #[1, 2, [3, 100, 5]]
print(b)  #[999, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  #a[2]와 b[2]가 같은 객체인가? True
```

### 1차원 리스트와 다차원 리스트의 차이

- 1차원 리스트 : 얕은 복사로 충분히 독립적인 복사본을 만들 수 있음
- 다차원 리스트 : 최상위 리스트만 복사되고, 내부 리스트는 여전히 원본과 같은 객체 참조

## 깊은 복사(Deep Copy)

객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법

중첩된 객체까지 모두 새로운 객체로 생성됨

- copy 모듈에서 제공하는 deepcopy() 함수를 사

```python
import copy

print('\n깊은 복사 예시')
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100
print(a)  #[1, 2, [3, 4, 5]]
print(b)  #[1, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  #a[2]와 b[2]가 같은 객체인가? False
```

- 중첩된 객체에서의 깊은 복사

```python
# 복잡한 중첩 객체 예시
print('\n복잡한 중첩 객체 깊은 복사')
original = {
    'a': [1, 2, 3],
    'b': {
        'c': 4,
        'd': [5, 6],
    },
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  #원본: {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
print(f'복사본: {copied}')  #복사본: {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
print(
    f'original["b"]와 copied["b"]가 같은 객체인가? {original["b"] is copied["b"]}'
)  #original["b"]와 copied["b"]가 같은 객체인가? False
```

- 모습만 똑같고 완전히 다른 객체

---

# 메서드 체이닝(Method Chaining)

여러 메서드를 연속해서 호출하는 방식

```python
# 문자열 메서드 체이닝
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l', 'z')
print(new_text)  # HEzzO, WOrLD!

```

swapcase() : 반환

반환한 값이 있어서 replace 실행 가능

앞에 반환이 있어야 함

- 코드 실행
1. text.swapcase() :대소문자를 반전시킴 ‘heLLo, woRld!’ → ‘HEllO, WOrLD’
2. .replace(’l’,’z’) : 소문자 ‘l’을 ‘z’로 교체 : ‘HEllo, WOrLD!’ → ‘HEzzO, WOrLD!’

```python
# 1. 단계별로 실행하기
text = 'heLLo, woRld!'
step1 = text.swapcase()
print('1단계 결과:', step1)  # HEllO, WOrLD!

step2 = step1.replace('l', 'z')
print('2단계 결과:', step2)  # HEzzO, WOrLD!

# 2. 한 줄로 실행하기 (위와 동일한 결과)
new_text = text.swapcase().replace('l', 'z')
print('최종 결과:', new_text)  # HEzzO, WOrLD!
```

리스트에서 메서드 체이닝 예시

- copy()로 리스트를 복사한 후, sorted 함수로 정렬

```python
# 리스트 메서드 체이닝 예시

# 잘못된 체이닝 방식 1
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.copy().sort()
print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)
print(result)  # None (sort()는 None을 반환하므로 체이닝이 중단됨)

#올바른 체이닝 예시
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]

# 잘못된 체이닝 방식 2
result = numbers.append(7).extend([8, 9])  # AttributeError

# 개선된 방식
# 리스트 조작에서 메서드 체이닝을 사용할 때는 각 메서드가 적절한 값을 반환하는지 확인하고,
# 필요한 경우 새로운 리스트 객체를 반환하는 함수를 사용하는 것이 좋음
sorted_numbers = sorted(numbers.copy()) #원본을 바꾸는게 아니라 값을 반환해줌
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
```

### 메서드 체이닝 주의 사항

- 모든 메서드가 체이닝을 지원하는 것은 아님 : 객체를 반환할 때만 체이닝 가능
- None을 반환하는 메서드는 메서드 체이닝이 불가능

  ex)리스트의 append(), sort()

- 메서드 체이닝을 사용할 때는 각 메서드의 반환값을 잘 이해하고 있어야함

---

## 문자 유형별 메서드

- isdecimal() : 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
- isdigit() : isdecimal()과 비슷하지만, 유니코드 숫자도 인식
- isnumeric() : isdigit()과 유사하지만 몇 가지 추가적인 유니코드 문자들을 인식 (분수, 지수, 루트 기호도 숫자로 인식)