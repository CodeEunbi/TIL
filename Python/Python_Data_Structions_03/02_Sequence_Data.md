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
