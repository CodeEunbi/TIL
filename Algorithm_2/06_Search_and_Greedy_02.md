# 완전검색/그리디2(25.03.13)

# 부분 집합

집합에 포함된 원소들을 선택하는 것

부분집합에는 아무것도 선택하지 않은 경우도 집합에 포함된다


부분집합 예시

집합 {A,B,C}로 만들 수 있는 부분집합

아무것도 선택하지 않은 경우도 포함

(= 공집합)

### 집합에서 부분 집합을 찾아내는 구현 방법

1. 완전탐색
- 재귀호출을 이용한 완전탐색으로 부분집합을 구할 수 있다
- 실전보다는 완전 탐색 학습용
1. Binary Counting
- 2진수 & 비트연산을 이용하여 부분집합을 구할 수 있다
- 부분집합이 필요할 때 사용하는 추천방법

## 완전탐색
### 구현방법

- Branch : 2개
- Level : 3개

```python
arr = ['o', 'x']
path = []

def run(lev):
		if lev == 3:
				print(path)
				return
		
		for i in range(2):
				path.append(arr[i])
				run(lev + 1)
				path.pop()
				
run()
```

## 바이너리 카운팅(Binary Counting)


원소 수에 해당하는 N개의 비트열을 이용

0 0 1 이면 {A}임을 나타냄

1 1 0 이면 {B, C}임을 나타냄

집합의 총 개수

- 만들 수 있는 집합의 총 개수는 2^n이며  n = 3이기에 총 8개 집합이다
- 2^n은 1<<n 공식을 이용하여 빠르게 구할 수 있음

0b110이 주어지면 BC출력하는 함수

- 6(0b110)에서 비트연산을 이용하여 마지막 한자리가 1인지 0인지 검사

```python
arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
		for i in rang(n):
				if tar & 0x1:
						print(arr[i]. end='')
						tar >>= 1
						
get_sub(6)
```

- 검사한 한 자리를 제거한다(tar >>= 1)

---

# 조합

서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합(combination)이라고 부른다

### 순열과 조합 차이

- 순열 : {A, B, C, D, E} 5명 중 1등, 2등, 3등 뽑기 → A B C와 C B A 는 다른 경우
- 조합 : 5명 중 3명 뽑기 → A B C 와 C B A는 같은 경우이다

Q. For으로 조합 구현하기

- 5명 중 3명 뽑는 조합은 3중 for 문으로 구현이 가능
- n중 for로 구현이 가능 → 재귀 호출 구현이 필요
- branch → 최대 5개
- level → n

```python
arr = ['A', 'B', 'C', 'D', 'E']
n = 3

path = []

# 5명 중 3명을 뽑는 문제
def recur(cnt, start):
    # N명을 뽑으면 종료
    if cnt == n:
        print(*path)
        return

    # for i in range(이전에 뽑았던 인덱스 + 1부터, len(arr))
    # start : 이전 재귀로부터 넘겨받아야하는 값
    for i in range(start, len(arr)):
        path.append(arr[i])
        # i: i번째를 뽑겠다
        # i + 1을 매개변수로 전달 : 다음 재귀부터는 i + 1부터 고려
        recur(cnt + 1, i + 1)
        path.pop()
recur(0 ,0)

```

[도전]

주사위 눈금 N개를 던져서 나올 수 있는 모든 조합을 출력(구현) N = 3일 때!

```python
# 주사위 3개를 던져 나올 수 있는 모든 조합을 출력
# 종료조건: 주사위 3개를 던졌을 때
N = 3
path = []

def recur(cnt, start):
    if cnt == N:
        print(path)
        return
    for i in range(start, 7):
        path.append(i)
        # 중복 허용
        recur(cnt + 1, i)
        path.pop()

recur(0, 1)
```

---

# Greedy

## Greedy(욕심쟁이 기법, 알고리즘)?

결정이 필요할 때 현재 기준으로 가장 좋아 보이는 선택지로 결정하여 답으로 도축하는 알고리즘

<aside>
💡

### 어떤 문제가 그리디인가, 무조건 최적화만 하면 되나요?

조건을 확인하기 전에 선행 되어야 할 것

1. 규칙성을 찾아야 한다
- 규칙을 못 찾으면 못 푼다

-- **그리디로 풀 수 있는 조건**

1. 탐욕적 선택 조건(Greedy Choice Property)
- 각 단계의 최적해 선택이 이후 단계 선택에 영향을 주지 않는다
- 각 단계 규칙이 변하면 안된다
- 동전 문제 예시(증명)
    - 첫 번째 단계 : 500원을 고름
    - 두 번째 단계 : 남은 동전 중 가장 큰 동전인 100원
        - 각 단계를 진행하면서 규칙이 유지 → greedy 가능

2. 최적 부분 구조(Optimal Substructure)
- 각 단계의 최적해 선택을 합하면, 전체 문제의 해결책이어야 한다

→ 동전 문제 예시 ⇒ 명제(가장 큰 동전부터 고르면 최소 동전 수가 나옴

                           ⇒ 간접증명(가장 큰 동전부터 고르면 최적해가 안나온다고 가정, 작은 동전부터 골랐을 때 최적해가 나온다 라고 가정

더 작은 수로 나눴을 때 최소몫이 나올 수 있다 → 가정이 모순 발생

</aside>

### 대표적인 문제 해결

1. 완전 탐색(Brute - Force) : 답이 될 수 있는 모든 경우를 시도해보는 알고리즘
2. Greedy : 결정이 필요할 때 가장 좋아보이는 선택지로 결정하는 알고리즘
3. DP : 현재에서 가장 좋아보이는 것을 선택하는 것이 아니라 과거의 데이터를 이용하여 현재의 데이터를 만들어내는 문제해결 기법
4. 분할 정복 : 큰 문제를 작은 문제로 나누어 해결하는 문제해결 기법

[문제]

동전 교환

10, 50, 100, 500 총 네 종류의 동전이 있다

손님의 돈을 최소한의 동전 수를 사용하여 교환해주려 한다

1730원을 거슬러주기 위해 사용할 수 있는 최대 동전 수는 몇개?

```python
# 큰 동전부터 주기(500원)
coin_lst = [500, 100, 50, 10]
target = 1730
cnt = 0

for coin in coin_lst:
    possible_cnt = target // coin
    cnt += possible_cnt
    target -= coin*possible_cnt
print(cnt)
```

[문제]

기숙사에는 하나의 화장실만 존재

A - 15 B - 30 C - 50 D - 10분 사용

```python
people = [15, 30, 50, 10]
n = len(people)

# 규칙. 최소 시간인 사람부터 화장실로 들어가자
people.sort() # 오름차순 정렬

total_time = 0
remain_people = n - 1

for turn in range(n):
    time = people[turn]
    total_time += time * remain_people
    remain_people -= 1

print(total_time)
```

[문제]

도둑은 보물들이 있는 창고에 침입 + 최대 30kg까지 짐을 담아갈 수 있다

물건의 개수(N), 물건 별 무게(W)와 가격(P)이 주어질 때, 어떤 물건을 담아야 도둑이 최대 이득을 볼 수 있을 지 구하기(1개씩 밖에 없음)

|  | 무게 | 값 |
| --- | --- | --- |
| 물건1 | 5kg | 50만원 |
| 물건 2 | 10kg | 60만원 |
| 물건3 | 20kg | 140만원 |

그리디로 구현이 가능할까?

|  | 무게 | 값 | 값/kg |
| --- | --- | --- | --- |
| 물건1 | 5kg | 50만원 | 10만원/kg |
| 물건 2 | 10kg | 60만원 | 6만원/kg |
| 물건3 | 20kg | 140만원 | 7만원/kg |

```python
n = 3
target = 30
things = [(5, 50), (10, 60), (20, 140)] # (kg, price)

# kg 당 가격으로 어떻게 정렬?
# 정렬 : (price / kg)
# lambda : 재사용하지 않는 함수
things.sort(key=lambda x: (x[1] / x[0]), reverse=True)

total = 0
for kg, price in things:
    per_price = price / kg

    # 만약 가방에 남은 용량이 얼마되지 않는다면
    #  물건을 잘라 가방에 넣고 끝낸다
   if target < kg:
        total += target * per_price
        break

    total += price
    target -= kg
print(int(total))
```

[문제] 그리디(회의실 배정)

회의실이 하나인 회사가 있다

여러 팀들이 원하는 회의실 예약 시간이 주어질 때, 가능한 많은 회의가 열리기 위해서는 회의들을 어떻게 배정해야할까?