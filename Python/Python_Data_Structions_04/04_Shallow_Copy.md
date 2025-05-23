# 복사

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
