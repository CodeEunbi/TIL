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
