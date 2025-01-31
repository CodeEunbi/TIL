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
