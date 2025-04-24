‼️키값에 공백을 필요로 하다면 세미 콜론

# 객체

## object

키로 구분된 데이터 집합을 저장하는 자료형(data collection)

## 구조 및 속성

### 객체 구조

- 중괄호(’{}’)를 이용해 작성
- 중괄호 안에는 key:value 쌍으로 구성된 속성(property)를 여러 개 작성 가능
- key는 문자형만 허용
- value는 모든 자료형 허용

```jsx
const user = {
      name: 'Alice',
      'key with space': true,
      greeting: function () {
        return 'hello'
      }
    }
```

### 속성 참조

- 점(., chaining operator) 또는 대괄호(’[]’)로 객체 요소 접근
- key이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근 가능

```jsx
    // 조회
    console.log(user.name) // Alice
    console.log(user['key with space']) // true

    // 추가
    user.address = 'korea'
    console.log(user) // {name: 'Alice', key with space: true, address: 'korea', greeting: ƒ}

    // 수정
    user.name = 'Bella'
    console.log(user.name) // Bella

    // 삭제
    delete user.name
    console.log(user) // {key with space: true, address: 'korea', greeting: ƒ}
```

### ‘in’ 연산자

속성이 객체에 존재하는지 여부를 확인

```jsx
  // in 연산자
    console.log('greeting' in user) // true
    console.log('country' in user) // false
```

## 메서드(Method)

객체 속성에 정의된 함수

### Method 사용 예시

- object.method() 방식으로 호출
- 메서드는 객체를 ‘행동’할 수 있게 함

```jsx
  // 메서드 호출
    console.log(user.greeting()) // hello
```

## this

### Method

➡️ ‘this’ 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있음

### ‘this’ keyword

함수나 메서드를 호출한 객체를 가리키는 키워드

➡️ 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

### Method & this 사용 예시

```jsx
// Method & this 예시
    const person = {
      name: 'Alice',
      greeting: function () {
        return `Hello my name is ${this.name}`
      },
    }
    
     console.log(person.greeting()) // Hello my name is Alice
```

<aside>
🚨

JavaScript에서 this는 함수를 ‘호출하는 방법’에 따라 가리키는 대상이 다름

</aside>

| 호출 방법 | 대상 |
| --- | --- |
| 단순 호출 | 전역 객체 |
| 메서드 호출 | 메서드를 호출한 객체 |

### 1. 단순 호출 시 this

가리키는 대상 ⇒ 전역 객체

```jsx
    // 1.1 단순 호출
    const myFunc = function () {
      return this
    }
    console.log(myFunc()) // window
```

### 2. 메서드 호출 시 this

가리키는 대상 ⇒ 메서드를 호출한 객체

```jsx
   // 1.2 메서드 호출
    const myObj = {
      data: 1,
      myFunc: function () {
        return this
      }
    }
    console.log(myObj.myFunc()) // myObj
```

### 중첩된 함수에서의 this문제점과 해결책

```jsx
 // 2.1 일반 함수
    const myObj2 = {
      numbers: [1, 2, 3],
      myFunc: function () {
        this.numbers.forEach(function (number) {
          console.log(this) // window
        })
      }
    }
    console.log(myObj2.myFunc())
```

for Each의 인자로 작성된 함수는 일반적인 함수 호출이기 때문에 this가 전역 객체를 기리킴

```jsx
    // 2.2 화살표 함수
    const myObj3 = {
      numbers: [1, 2, 3],
      myFunc: function () {
        this.numbers.forEach((number) => {
          console.log(this) // myObj3
        })
      }
    }
    console.log(myObj3.myFunc())
```

화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수(myFunc)에서의 this값을 가져옴

### JavaScript ‘this’ 정리

- JavaScript의 함수는 호출 될 때 this를 암묵적으로 전달 받음
- JavaScript에서 this는 함수가 ‘호출되는 방식’에 따라 결정되는 현재 객체를 나타냄
- Python의 self와 Java의 this가 선언 시 이미 값이 정해지는 것에 비해 JavaScript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨(동적 할당)
- this가 미리 정해지지 않고 호출방식에 의해 결정되는 것
- 장점
    - 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
- 단점
    - 이런 유연함이 실수로 이어질 수 있다는 것

➡️ 개발자는 this의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는데에 집중

## 추가 객체 문법

### 1. 단축 속성

키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음

```jsx
// 1. 단축 속성
    const name = 'Alice'
    const age = 30

    const user = {
      name: name,
      age: age
    }

```

```jsx
// 1. 변화된 단축 속성
    const name = 'Alice'
    const age = 30

    const user = {
      name,
      age,
    }

```

### 2. 단축 메서드

메서드 선언 시 function 키워드 생략 가능

```jsx
   // 2. 단축 메서드
    const myObj1 = {
      myFunc: function () {
        return 'Hello'
      }
    }
```

```jsx
    const myObj2 = {
      myFunc() {
        return 'Hello'
      }
    }

```

### 3. 계산된 속성(computed property name)

키가 대괄호([])로 둘러싸여 있는 속성

➡️ 고정 값이 아닌 변수 값을 사용할 수 있음

```jsx

    // 3. 계산된 속성
    const product = prompt('물건 이름을 입력해주세요')
    const prefix = 'my'
    const suffix = 'property'

    const bag = {
      [product]: 5,
      [prefix + suffix]: 'value'
    }

    console.log(bag) // {연필: 5, myproperty: 'value'}

```

### 4. 구조 분해 할당(destructing assignment)

배열 또는 객체를 분해하여 객체 속성을  변수에 쉽게 할당할 수 있는 문법

```jsx
// 4. 구조 분해 할당
    const userInfo = {
      firstName: 'Alice',
      userId: 'alice123',
      email: 'alice123@gmail.com'
    }

    const firstName = userInfo.name
    const userId = userInfo.userId
    const email = userInfo.email

```

```jsx
    const userInfo = {
      firstName: 'Alice',
      userId: 'alice123',
      email: 'alice123@gmail.com'
    }

    const { firstName } = userInfo
    const { firstName, userId } = userInfo
    const { firstName, userId, email } = userInfo

    // Alice alice123 alice123@gmail.com
    console.log(firstName, userId, email)

```

‘함수의 매개변수’로 객체 구조 분해 할당 활용 가능

```jsx
    // 구조 분해 할당 활용 - 함수 매개변수
    function printInfo({ name, age, city }) {
      console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
    }

    const person = {
      name: 'Bob',
      age: 35,
      city: 'London',
    }

    // 함수 호출 시 객체를 구조 분해하여 함수의 매개변수로 전달
    printInfo(person) // '이름: Bob, 나이: 35, 도시: London'
```

### 5. Object with ‘전개 구문’

- 객체 복사 : 객체 내부에서 객체 전개 가능
- 얕은 복사에서 활용 가능

```jsx
   // 5. 전개 구문
    const obj = { b: 2, c: 3, d: 4 }
    const newObj = { a: 1, ...obj, e: 5 }
    console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
```

### 6. 유용한 객체 메서드

- Object.keys()
- Objects. values

```jsx
// 6. 유용한 객체 메서드
    const profile = {
      name: 'Alice',
      age: 30
    }

    console.log(Object.keys(profile)) // ['name', 'age']
    console.log(Object.values(profile)) // ['Alice', 30]
```

### 7. Optional chaining(’?.’)

- 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환

```jsx
    const user = {
      name: 'Alice',
      greeting: function () {
        return 'hello'
      }
    }
```

```jsx
 // console.log(user.address.street) // Uncaught TypeError: Cannot read properties of undefined (reading 'street')
    console.log(user.address?.street) // undefined

    // console.log(user.nonMethod()) // Uncaught TypeError: user.nonMethod is not a function
    console.log(user.nonMethod?.()) // undefined

```

- 만약 Optional chaining을 사용하지 않는다면 다음과 같이 ‘&&’ 연산자를 사용해야함

```jsx
  const user = {
      name: 'Alice',
      greeting: function () {
        return 'hello'
      }
    }
    
     console.log(user.address && user.address.street) // undefined
```

**장점**

- 참조가 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때 더 짧고 간단한 표현식으로 작성할 수 있음
- 어떤 속성이 필요한지에 대한 보증이 확실하지 않는 경우에 객체의 내용을 보다 편리하게 탐색할 수 있음

**주의 사항**

1. Optional chaining은 존재하지 않아도 괜찮은 대상에만 사용해야함(남용X)
- 왼쪽 평가 대상이 없어도 괜찮은 경우에만 선택적으로 사용
- 중첩 객체를 에러없이 접근하는 것이 사용 목적이기 때문

```jsx
// 위 예시 코드 논리상 user는 반드시 있어야 하지만 address는 필수 값이 아님
    // user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문

    // Bad
    user?.address?.street

    // Good
    user.address?.street
```

2. Optional chaining 앞의 변수는 반드시 선언되어있어야함

```jsx
console.log(myObj?.address)  // Uncaught ReferenceError: myObj is not defined
```

<aside>
⚙

**Optional chaining  정리**

1. obj?.prop
- obj가 존재하면 obj.prop을 반환하고 그렇지 않으면 undefined를 반환
2. obj?.[prop]
- obj가 존재하면 obj[prop]을 반환하고 그렇지 않으면 undefined를 반환
3. obj?.method()
- obj가 존재하면 obj.method()를 호출하고 그렇지 않으면 undefined를 반환
</aside>

## JSON

- JavaScript Objection Notation
- Key-Value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 ‘문자열’
- JavaScript자료형으로 변경해야함

### Object ↔ JSON 변환하기

```jsx
const jsObject = {
      coffee: 'Americano',
      iceCream: 'Cookie and cream'
    }

    // Object -> JSON
    const objToJson = JSON.stringify(jsObject)
    console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
    console.log(typeof objToJson)  // string

    // JSON -> Object
    const jsonToObj = JSON.parse(objToJson)
    console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
    console.log(typeof jsonToObj)  // object

```

---

# 배열

## Object

키로 구분된 데이터 집합을 저장하는 자료형(data collection)

➡️ 이제는 순서가 있는 collection이 필요

### Array

순서가 있는 데이터 집합을 저장하는 자료구조

### 배열 구조

- 대괄호([])를 이용해 작성
- 요소의 자료형은 제약 없음
- length 속성을 사용해 배열에 담긴 요소 개수 확인 가능

```jsx
const names = ['Alice', 'Bella', 'Cathy']

console.log(names[0]) // Alice
console.log(names[1]) // Bella
console.log(names[2]) // Cathy

console.log(names.length) // 3
```

## 배열 메서드

### 주요 메서드

| 메서드 | 역할 |
| --- | --- |
| push/pop | 배열 끝 요소를 추가 / 제거 |
| unshift/shift | 배열 앞 요소를 추가 / 제거 |

### push()

배열 끝에 요소를 추가

```jsx
const names = ['Alice', 'Bella', 'Cathy']

names.push('Dan')
console.log(names) // ['Alice', 'Bella', 'Cathy', 'Dan']
```

### pop()

배열 끝 요소를 제거하고 제거한 요소를 반환

```jsx
const names = ['Alice', 'Bella', 'Cathy']

    // pop
    console.log(names.pop()) // Cathy
    console.log(names) // ['Alice', 'Bella']
```

### unshift()

배열 앞에 요소를 추가

```jsx
    const names = ['Alice', 'Bella', 'Cathy']
    
    // unshift
    names.unshift('Eric')
    console.log(names) // ['Eric', 'Bella', 'Dan']
```

### shift()

배열 앞 요소를 제거하고 제거한 요소를 반환

```jsx
    // shift
    console.log(names.shift()) // Eric
    console.log(names) // [''Alice', 'Bella', 'Dan']
```

## Array Helper Methods

배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음

- ES6에 도입
- 배열의 각 요소를 순회하며 각 요소에 대해 함수(콜백함수)르 롷출
- 대표 메서드
    - forEach(), map(), filter(), every(), some(), reduce()  등

➡️ 메서드 호출 시 인자로 함수(콜백  함수)를 받는 것이 특징

## 콜백 함수(Call back Function)

다른 함수에 인자로 전달되는 함수

➡️ 외부 함수 내에서 호출되어 일종의 루틴이나 특정작업을 진행

### 예시

```jsx
// 1
    const numbers1 = [1, 2, 3]
    numbers.forEach(function (num) {
      console.log(num)
    })

    // 2
    const numbers2 = [1, 2, 3]
    const callBackFunction = function (num) {
      console.log(num)
    }

    numbers.forEach(callBackFunction)
    
    // 1
    // 2
    // 3

```

### 주요 Array Helper Methods

| 메서드 | 역할 |
| --- | --- |
| forEach | - 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출
-반환 값 없음 |
| map | - 배열 내의 모든 요소 각각에 대해 함수(콜백 함수)를 호출
- 함수 호출 결과를 모아 새로운 배열을 반환 |

### forEach()

배열의 각 요소를 반복하며 모든 요소에 대해 함수를 호출(콜백함수)

### forEach() 구조


콜백 함수는 3가지 매개변수로 구성

1. item : 처리할 배열의 요소
2. index : 처리할 배열 요소의 인덱스(선택 인자)
3. array :  forEach를 호출한 배열(선택 인자)

반환값

- undefined

```jsx
array.forEach(function(item, index, array) {
	// do something
})
```

```jsx
 const names = ['Alice', 'Bella', 'Cathy']

    // 일반 함수 표기
    names.forEach(function (name) {
      console.log(name)
    })

    // 화살표 함수 표기
    names.forEach((name) => {
      console.log(name)
    })

```