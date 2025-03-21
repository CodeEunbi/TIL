# 분할정복 / 백트래킹(25.03.17)

## 분할정복

- 문제를 분할해서 해결하는 기법

유래

- 1805년 12월 2일 아우스터리츠 전투에서 나폴레옹이 사용한 전략
- 전력이 우세한 연합군을 공격하기 위해 나폴레옹은 연합군의 중앙부로 쳐들어가 연합군을 둘로 나눔
- 둘로 나뉜 연합군을 한 부분씩 격파

설계 전략

- 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다
- 정복(Conquer) : 나눈 작은 문제를 각각 해결한다
- 통합(Combine) : (필요하다면) 해결된 해답을 모은다

Top-down approach


거듭제곱

반복(iterative) 알고리즘 : O(n)



분할 정복 기반의 알고리즘 : O(log₂n)



---

## 병합 정렬

여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 ㅂ아식

분할 정복 알고리즘

- 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
- Top-down 방식

시간 복잡도 - O(n log n)

### 병합 정렬 과정

- {69, 10, 30, 2, 16, 8, 31, 22}를 병합 정렬하는 과정
- 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분 집합이 될 때까지 분할 작업을 계속 한다
- 병합 단계 : 2개의 부분 집합을 정렬하면서 하나의 집합으로 병합
- 8개의 부분 집합이 1개로 병합될 때까지 반복


---

# 퀵 정렬

주어진 배열을 두개로 분할하고, 각각을 정렬 → 병합 정렬과 동일X

다른 점 1: 병합 정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item)중심으로 분할

- 기준보다 작은 것은 왼편, 큰 것은 오른편에 위치

다른 점2: 각 부분 정렬이 끝난 후, 병합 정렬은 ‘병합’이란 후처리 작업이 필요하나 퀵 정렬은 필요로 하지 않는다

- Quick sort는 Partitioning 이라는 과정을 반복하면서 평균 시간 복잡도 O(nlogn)속도라는 빠른 속도로 정렬이 되는 sort

### 퀵 정렬 - partitioning

1. 작업영역을 정한다


2. 작업 영역 중 가장 왼쪽에 있는 수를 pivot이라고 하자.(pivot을 ‘기준’으로 해석)


3. Pivot을 기준으로 왼쪽에는 pivot보다 작은 수를 배치(정렬X)
    
    오른쪽에는 Pivot보다 큰 수를 배치 시킨다(정렬 X)
    

    

파티셔닝이 끝나고 Pivot의 위치는 확정(fix)된다

즉, 정렬이 다 되어있을 때에도 Pivot의 위치는 지금 위치 그대로 배정



---

# 이진 검색(Binary Search)

- 자료 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
    - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행
- 이진 검색을 하기위해서는 자료가 정렬된 상태여야한다

### 검색과정

- 자료의 중앙에 있는 원소를 고른다
- 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다
- 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다
- 찾고자 하는 값을 찾을 때까지 앞의 1~3번 과정을 반복

---

# 정리

<aside>
🙆‍♀️

병합정렬

- 외부 정렬(External sort)의 기본이 되는 정렬 알고리즘
- 멀티코어(multi-core) CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용
</aside>

<aside>
🙆‍♀️

퀵 정렬

매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘

</aside>

<aside>
🙆‍♀️

이진 검색

- 정렬된 데이터를 기준으로 특정 값이나 범위를 검색하는데 사용
- [이진 검색을 활용한 심화 학습 키워드] Lower Bound, Upper Bound
    - 정렬된 배열에서 특정 값 이상(이하)가 처음으로 나타나는 위치를 찾는 알고리즘
    - 특정 데이터의 범위 검색 등에서 활용
</aside>