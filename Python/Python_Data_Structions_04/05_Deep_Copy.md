## 깊은 복사(Deep Copy)

객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법

중첩된 객체까지 모두 새로운 객체로 생성됨

- copy 모듈에서 제공하는 deepcopy() 함수를 사용

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
