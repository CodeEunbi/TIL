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

