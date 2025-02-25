# CSS Layout

# CSS Box Model

웹페이지의 모든  HTML 요소를 감싸는 사각형 상자 모델

- 원은 네모박스를 깎은 것
- 박스로 구성된 웹페이지 레이아웃

## 박스 타입

- 박스 타입에 따라 페이지에서 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

### Outer display type

박스가 문서 흐름에서 어떻게 동작할지를 결정

- block, inline

**Block**

- 항상 새로운 행으로 나뉨
- width, height 속성 사용 가능
- padding, margin, border로 인해 다른 요소로부터 밀어냄
- width 속성을 지정하지 않으면 박스는 inline방향으로 사용가능한 공간을 모두 차지

       : 상위 컨테이너 너비 100%로 채우는 것

- 대표적인 block type 태그 - h1~6, p, div

**inline**

- 새로운 행으로 넘어가지 않음
- width와 height 속성을 사용할 수 없음
- 수직 방향 → padding, margin, border가 적용되지만 다른 요소를 밀어낼 수는 없음
- 수평 방향 → padding margins, borders 가 적용되어 다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그 - a, img, span, strong, em

normal flow : 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹 페이지 요소가 배치되는 방식

# 박스 구성요소

## CSS Box Model

웹페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델

- 내용(content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성되어 요소의 크기와 배치를 결정
- Content box : 실제 콘텐츠가 표시되는 영역 크기, width 및 height 속성을 사용하여 크기 조정, width 및 height 속성을 사용하여 크기 조정
- padding box : 콘텐츠 주위에 공백, padding 관련 속성을 사용하여 크기 조정
- Border box : 콘텐츠와 패딩을 래핑, border 관련 속성을 사용하여 크기 조정
- Margin box : 콘텐츠, 패딩 및 테두리를 래핑, 박스와 다른 요소 사이의 공백, margin 관련 속성을 사용하여 크기 조정

## shorthand 속성

**border**

border - width, border-style, border-color를 한번에 설정하기 위한 속성

작성 순서는 영향을 주지 않음

**margin & padding**

4방향을 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성

상하/좌우 상/좌우/하 상하/좌우 */ 공통

### box sizing

**The standard CSS box model**

표준 상자 모델에서 width와 height 속성 값을 설정하면 이 값은 content box의 크기를 조정

CSS는 border box가 아닌 content box의 크기를 width 값으로 지정

**The alternative CSS box model**

대체 상자 모델에서 모든 width와 height는 실제 상자의 너비

실제 박스 크기를 정하기 위해 테두리와 패딩을 조정할 필요가 없음

### **기타 display 속성**

**inline block**

- inline과 block요소 사이의 중간 지점을 제공하는 display 값
- width 및 height 속성 사용 가능
- padding, margin 및 border로 인해 다른 요소가 상자에서 밀려남
- 새로운 행으로 넘어가지 않음

→ 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용

**none**

- 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

---

# CSS Position

## CSS Layout

각 요소의 위치와 크기를 조정하여 웹페이지의 디자인을 결정하는 것

→ display, position, flexbox 등

## CSS Position

요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것

→ 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등

z축 - 수직 방향

상 하 좌 우 수직 5가지 방향

### position 유형

- static(기본), relative(상대), absolute(절대), fixed(고정), sticky

**static**

요소를 Normal Flow에 따라 배치

top, right, bottom, left 속성이 적용되지 않음

기본값

**relative**

요소를 Normal Flow에 따라 배치

자신의 원래 위치(static)을 기준으로 이동

top, right, bottom, left 속성으로 위치를 조정

다른 요소의 레이아웃에 영향을 주지 않음(요소가 차지하는 공간은 static일 때와 같음)

**absolute**

요소를 Normal Flow에서 제거

가장 가까운 relative 부모 요소를 기준으로 이동

- 만족하는 부모 요소가 없다면 body 태그를 기준으로 함

top, right, bottom, left 속성으로 위치를 조정

문서에서 요소가 차지하는 공간이 없어짐

**fixed**

요소를 Normal Flow에서 제거

현재 화면 영역(viewport)을 기준으로 이동

스크롤해도 항상 같은 위치에 유지

top, right, bottom, left 속성으로 위치를 조정

문서에서 요소가 차지하는 공간이 없어짐

**sticky**

relative와 fixed의 특성을 결합한 속성

스크롤 위치가 임계점에 도달하기 전에는 relative처럼 동작

스크롤이 특정 임계점에 도달하면 fixed처럼 동작하여 화면에 고정

만약 다음 sticky요소가 나오면 다음 sticky요소가 이전 sticky요소의 자리를 대체

→ 이전 sticky요소가 고정되어있던 위치와 다음 sticky 요소가 고정되어야할 위치가 겹치게 되기 때문

---

# Z - index

요소의 쌓임 순서(stack order)를 정의하는 속성

정수 값을 사용해 z축 순서를 지정

값이 클수록 요소가 위에 쌓이게 됨

static이 아닌 요소에만 적용

**z-index 특징**

기본값은 auto

부모  요소의 z-index 값에 영향을 받음

같은 부모 내에서만 z-index 값을 비교

부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없음

z-index값이 같으면 HTML 문서 순서대로 쌓임

### position의 목적

전체 페이지에 대한 레이아웃을 구성하는 것보다 페이지 특정 항목의 위치를 조정하는 것

## CSS Flexbox

요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식 → 공간 배열 & 정렬 

### Inner display type

박스 내부의 요소들이 어떻게 배치될지를 결정

속성 - flex

### 구성요소

flex item들이 배치되는 기본축

main start에서 시작하여 main end 방향으로 배치(기본값)


main axis에 수직인 축

cross start에서 시작하여 cross end방향으로 배치(기본값) 

Flex Container


display : flex; 혹은 display: inline - flex; 가 설정된 부모 요소

이 컨테이너의 1차 자식 요소들이 flex item이 됨

flex box 속성 값들을 사용하여 자식 요소 flex item들을 배치하는 주체

Flex item

flex container 내부에 레이아웃 되는 항목


### Flexbox 속성

- Flex Container 관련 속성 : display, flex-direction, flex-wrap, justify-content, align-items, align-content
- Flex item 관련 속성 : align-self, flex-grow, flex-basis, order

**Flex Container 지정**

flex item은 기본적으로 행(주 축의 기본값인 가로 방향)으로 나열

flex item은 주 축의 시작 선에서 시작

flex item은 교차 축의 크기를 채우기 위해 늘어남

**Flex-direction**

flex item이 나열되는 방향을 지정

column으로 지정할 경우 주 축이 변겨오딤

‘-reverse’로 지정하면 flex item 배치의 시작 선과 끝 선이 서로 바뀜

**Flex-wrap**

flex item목록이 flex container의 한 행에 들어가지 않을 경우 다른 행에 배치할지 여부 설정

**Justify-content**

주 축을 따라 flex item과 주위에 공간을 분배

**align - content**

교차 축을 따라 flex item과 주위에 공간을 분배

- flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨
- 한 줄 짜리 행에는 효과 없음(flex-wrap이 nowrap으로 설정된 경우)

**align - items**

교차 축을 따라 flex item행을 정렬

**align-self**

교차 축을 따라 개별 flex item을 정렬

**목적에 따른 속성 분류**

배치 : flex-direction, flex-wrap

공간분배 : justify - content, align-content

정렬 : align-items, align-self

justify - 주축, align-교차 축

**flex-grow**

남는 행 여백을 비율에 따라 각 flex item에 분배 - 아이템이 컨테이너 내에서 확장하는 비율을 지정

flex grow의 반대는 flex-shrink

**flex-basis**

flex item의 초기 크기 값을 지정

flex-basis와 width값을 동시에 적용한 경우 flex-basis가 우선

### flex-wrap 응용

### 반응형 레이아웃

다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식

---

# 마진 상쇄

두 block타입 요소의 martin top과 bottom이 만나 더 큰 margin으로 결합되는 현상

- 복잡한 레이아웃에서 요소 간 간격을 일관되게 유지하기 위함
- 요소 간의 간격을 더 예측 가능하고 관리하기 쉽게 만듦

→ 일관성, 단순화

---

# 박스 타입 별 수평정렬

block 요소의 수평정렬

margin: auto사용

블록 요소의 너비를 지정하고 좌우 마진을 auto로 설정

Inline 요소의 수평정렬

text-align 사용 : 부모 요소에 적용

Inline-block요소의 수평 정렬

text-align 사용 : 부모 요소에 적용