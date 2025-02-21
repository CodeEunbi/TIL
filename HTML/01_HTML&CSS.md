# HTML & CSS

# Web(웹)

## World Wide Web

인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간

## Web

Website, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

## Website

인터넷에서 여러 개의 Web page가 모인 것으로 사용자들에게 정보나 서비스를 제공하는 공간

## Web page

HTML, CSS 등의 웹 기술을 이용하여 만들어진, ‘Website’를 구성하는 하나의 요소

- HTML, CSS, Javascript

---

## 웹구조화

### HTML

Hyper Text Markup Language

웹 페이지의 의미와 구조를 정의하는 언어

프로그래밍 언어 X → 계산이 되지 않

Hypertext : 웹페이지를 다른 페이지로 연결하는 링크, 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

- 비선형성/상호연결성/사용자 주도적 탐색

Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 ex)HTML, Markdown

## Structure of HTML

### HTML 구조

- <!DOCTYPE html> - html 문서 시작
- <html> </html> : 전체 페이지의 콘텐츠를 포함
- <title> </title> : 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용

  - ’/’ → 닫는 꺽새

- <head> </head> : html 문서에 관련된 설명, 설정 등 컴퓨터가 식별하는 메타데이터를 작성

                                         : 사용자에게 보이지 않음

 - 메타 데이터 : 데이터의 데이터

- <body> </body>

 - HTML 문서의 내용을 나타냄

 - 페이지에 표시되는 모든 콘텐츠를 작성

 - 한 문서에 하나의 body 요소만 존재

### HTML Element(요소)

하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성

닫는 태그는 태그 이름 앞에 슬래시가 포함됨(닫는 태그가 없는 태그도 존재)
닫는 태그가 없는 태그의 특징

- 컨텐츠가 없음
- <meta charset = ‘UTF-8’> → 닫는 태그가 없음
- <title> my page </title> → 닫는 태그가 있음

### HTML Attributes(속성)

사용자가 원하는 기준에 맞도록 요소를 설정하거나 다양한 방식으로 요소의 동작을 조절하기 위한 값

목적

- 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
- CSS에서 스타일 적용을 위해 해당 요소를 선택하기 위한 값으로 활용

[규칙]

- 속성은 요소의 이름과 속성 사이에 공백이 있어야함
- 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분
- 속성 값은 열고 닫는 따옴표로 감싸야함 → 없으면 인식 X

<실습>

! 하면 바로 양식

title ⇒ 웹페이지 윗쪽

a 태그 ⇒ 누르면 다른 곳으로 갈 수 있게(우리가 보는 화면은 a태그에 디자인이 되어있는 것)

이미지는 닫는 태그 없음 이미지 자체가 콘텐츠, 경로를 통해 띄움

alt는 이미지를 띄우는데 크게 영향을 주지 않음

alt는 이미지에 문제가 있을 때 (경로가 다를 때) 대신 띄어주는 말 / 문제가 발생했을 때 대체할 텍스트

로컬 파일이 아니더라도 외부주소를 이용해 사진을 띄울 수 있음

크롬 → 검사(개발자도구) (f12 , ctrl + shift+i)→ 수정(디버깅)

## Text Structure

HTML Text Structure : 주요 목적 중 하나는 텍스트 구조와 의미를 제공

<h1>Heading</h1> : 단순히 텍스트를 크게 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여

Heading & Paragraphs : h1~6, p

Lists - ol, ul, li

Emphasis & Importance : em, strong

---

## 웹 스타일링

## CSS(Cascading Style Sheet)

웹 페이지의 디자인과 레이아웃을 구성하는 언어


CSS 적용방법

1. 인라인(Inline) 스타일
2. 내부(Internal) 스타일 시트
3. 외부(External)스타일 시트

### 인라인(Inline)스타일

HTML 요소 안에 style속성 값으로 작성

style = ‘color:blue; background-color:yellow;’

### 내부(Internal)스타일 시트

head 태그 안에 style 태그에 작성

```python
<style>
	h1{
		color : blue;
		background-color: yellow;
	}
```

### 외부 (External) 스타일 시트

별도 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기

## CSS 선택자

### CSS Selectors

HTML요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

### CSS Selectors 종류

기본 선택자

- 전체(*) 선택자 : HTML 모든 요소를 선택
- 요소 (tag) 선택자 : 지정한 모든 태그를 선
- 클래스(class) 선택자 (’.’): 주어진 클래스 속성을 가진 모든 요소를 선택
- 아이디(id)선택자(’#’): 주어진 아이디 속성을 가진 요소 선택, 문서에는 주어진 아이디를 가진 요소가 하나만 있어야함
- 속성(attr)선택자 등

결합자(Combinators)

- 자손 결합자(” “(space)): 첫번째 요소의 자손 요소들 선택, p span 은 <p>아넹 있는 모든 <span>를 선택(하위 레벨 상관없이)
- 자식 결합자(”>”): 첫 번째 요소의 직계 자식만 선택, 부모 태그의 컨텐츠 안에 들어가 있어야함
- <ul > li은 <ul>안에 있는 모든 <li>를 선택(한단계 아래 자식만)
- 들여쓰기는 의미 없음, but 사람을 위해서 들여쓰기

---

## 명시도

### Specificity

CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정

동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있는 경우 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용

### CSS(Cascading Style Sheet)

웹 페이지의 디자인과 레이아웃을 구성하는 언어

### Cascade(계단식)

한 요소에 동일한 가중치를 가진 선택자가 적용될 때 CSS에서 마지막에 나오는 선언이 사용됨

**명시도가 높은순**

1. Importance - !important
2. Inline 스타일
3. 선택자 - id 선택자 > class 선택자 > 요소 선택자

선택을 하는 범위가 좁을수록 명시도가 좋아짐

4. 소스 코드 선언 순서

!important 다른 우선순위 규칙보다 우선하여 적용하는 키워드

- Cascade의 구조를 무시하고 강제로 스타일을 적용하느 ㄴ방식이므로 사용을 권장

## 상속

### CSS 상속

기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임

- 상속이 되는 속성

 - Text관련 요소(font, color, text-align), opacity, visibility 등

- 상속 되지 않는 속성

 - Box model 관련 요소(width, height, border, box-sizing)

    position 관련 요소(position, top/right, bottom/left, z-index)

## CSS Box Model

웹페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델

### 박스 타입

1. Block box
2. Inline box

박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

박스 표사

Outer displah typr

Innrt display type

### Outer display type

박스가 문서 흐름에서 어떻게 동작할지 결정 - block, inline

block특징

- 항상 새로운 행으로 나뉨
- width와 height 속성 사용 가능
- padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
- width 속성을 지정하지 않으면 박스는 inline방향으로 사용 가능한 공간을 모두 차지함
- 상위 컨데이너 너비 100% 모두 차지
- 대표적인 block 타입 - h1~6, p, div

inline특징

- 새로운 행으로 넘어가지 않음
- width와 height 속성을 사용할 수 없음
- 수직 방향 → padding, margin, border가 적용되지만 다른 요소를 밀어낼 수는 없음
- 수평 방향 → padding margins, borders 가 적용되어 다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그 - a, img, span, strong, em

normal flow : 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹 페이지 요소가 배치되는 방식

Inner display type

박스 내부의 요소들이 어떻게 배치될지를 결정

속성 : flex

---

Style Guide

대소문자 구분

- 구분하지는 않지만 소문자를 권장
- 태그명과 속성명 모두 소문자로 작성

속성 따옴표

- 속성 값에는 큰 따옴표를 사용하는 것이 원칙

코드 구조와 포맷팅

- 일관된 들여쓰기를 사용(보통 2칸 공백)
- 각 요소는 한 줄에 하나씩 작성
- 중첩된 요소는 한 단계 더 들여쓰기

공백 처리

- HTML은 연속된 공백을 하나로 처리
- Enter키로 줄바꿈을 해도 브라우저에서 인식하지 않음(줄바꿈 태그 사용)

에러 출력 없음

HTML은 문법 오류가 있어도 별도의 에러 메세지를 출력하지 않음

---

CSS 스타일 가이드

코드 구조와 포맷팅

- 일관된 들여쓰기를 사용(2칸)
- 선택자와 속성은 각각 새줄에 작성
- 중괄호 앞에 공백 넣기
- 속성 뒤에는 콜론과 공백 넣기
- 마지막 속성되에는 세미 콜론 넣기

선택자 사용

- class 선택자를 우선적으로 사용
- id, 요소 선택자 등은 가능한 피할 것

→ 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워지기 때문

속성과 값

- 속성과 값은 소문자로 작성
- 0 값에는 단위를 붙이지 않음

명명규칙

- 클래스 이름은 의미 있고 목적을 나타내는 이름을 사용
- 케밥 케이스(kebab case)를 사용
- 약어보다는 전체 단어를 사용

CSS 적용 스타일

- 인라인 스타일은 되도록 사용하지 말것
- CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드를 이해하기 어렵게 만듦

---

# MDN Web Docs

Mozilla Developer Network에서 제공하는 온라인 문서

웹 개발자와 디자이너를 위한 종합적인 참고 자료

→ 웹 기술에 대한 정보를 제공

정확성 및 신뢰성

- 모질라와 웹 커뮤니티의 전문가들에 의해 작성되고 유지 관리
- 웹 표준을 정확하게 반영하고 있으며, 신뢰할 수 있는 정보 소스를 제공

최신 웹 기술

- 최신 웹 표준과 기술을 다루고 있어, 웹 개발자들이 최신 정보를 쉽게 접할 수 있음

명확한 설명과 예제

- 복잡한 개념을 이해하기 쉽게 설명하고 실습 가능한 예제 코드를 제공