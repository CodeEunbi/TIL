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