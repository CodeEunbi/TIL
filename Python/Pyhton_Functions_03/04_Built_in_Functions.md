# 내장함수(Built-in-function)

파이썬이 기본적으로 제공하는 함수(별도의 import없이 바로 사용 가능)

외장함수는 없음

ex) print(), len(),max(), min(),sum(), sorted()

# map & zip

## map(function, iterable)

**순회 가능한 데이터구조**(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

→ 반복문

### map활용()

```python
numbers1 = input().split()
print(numbers1) # ['1', '2', '3'] 문자열

numbers2 = list(map(int, input().split()))
print(numbers2) # [1, 2, 3] list 형변환
```

### zip(*iterables)

임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['Jane', 'Ashley']
boys = ['Peter', 'Jay']
pair = zip(girls, boys)

print(pair) #zip object at 0x000001C76DE58700
print(list(pair)) #[('Jane', 'Peter'),('Ashley', 'Jay')]
```

### zip() 활용

- 여러 개의 리스트를 동시 조회

```python
kr_scores = [10 ,20, 30 ,50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scors, math_scores, en_scores) :
		print(student_scores)

#(10, 20, 40) (20, 40, 20) (30, 50, 30)(50, 70, 50)
```

- 2차원 리스트의 같은 컬럼(열)요소를 동시에 조회

```python
scores = [
		[10, 20, 30],    #(10, 40, 20)
		[40, 50, 39],    #(20, 50, 40)    
		[20, 40, 50],    #(30, 39, 50) 
]

for score in zip(*scores):
		print(score)
```
